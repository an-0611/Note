
### 概要
前端： Javascript
後端： Python Redis
Web Server： Nginx
CICD： Travis (暫定), Docker, Kubernetes (暫定)
Cloud： GCE (ubuntu)
<font color=#E10000></font>
在 GCE 上啟用 Nginx 作為 Web server,
建立路由分別將服務導向 前端靜態檔 和 後端 Flask api,
綁定 godaddy domain, 並建立負載平衡 建立 SSL.

# 注意
##### ubuntu
- ubuntu 環境需先執行 sudo apt update 並安裝相關套件
- 不同於 apt-get, apt 安裝套件時會先自動更新 apt-get
- ubuntu 內使用 vim 時需加上 sudo, 不然權限不夠

##### nginx
- location 要與 flask router 一致
- server_name 皆不可重複
- 每次修改完需重啟 sudo systemctl restart nginx
- 利用 nginx 將 http 轉到 https 時, 如果 SSL 是由負載均衡, 需要在 nginx.conf 判別是否來自 http 才執行轉址以避免進入無限迴圈
  (因負載均衡 https 接收的後端為 http, nginx 將其重定向為 https, 又觸發負載均衡 https 導致無限迴圈)
- 加入 server_name 的域名或 IP 才能透過 nginx 進行路由分配映射

##### GCE 
- 若使用 負載均衡 建立 SSL, vm 會有新的外部 ip, 若先前有綁定 DNS A 或是 api 中有檢查 referer 的功能需要更改


## 流程
#### VM 環境安裝
```
sudo apt update
sudo apt install python-setuptools python-dev build-essential
sudo apt install redis-server
sudo apt install python3-pip (python-pip) // 可以自己選要 python 還是 python3
sudo apt install python3-redis // (3)指令安裝Python的Redis模組。
sudo apt install redis  // 安裝 redis-server
sudo apt install gunicorn
sudo apt install python3-flask 
```
<br>

#### VM 安裝 nginx 作為 web 服務器
```
sudo apt install nginx
```
/etc/nginx/nginx.conf server location / 需與 VM 前端靜態檔路徑一致
(location 為 root 的相對位置, 可透過 pwd 指定查詢目前檔案位置)
<br>

#### 透過 scp 或 VM GUI 將靜態檔更新到 VM 上
```
透過 scp
scp /path/index.html user@vm-ip:/path/to/vm/webserver/directory/
// 把 index.html 文件複製到 VM 上的 /path/to/vm/webserver/directory/ 目錄中

透過 VM GUI
上傳按鈕上傳壓縮檔(ex: .tgz), 之後在 VM 進行解壓縮
壓縮： tar -cf frontend.tgz frontend
解縮： tar -xf frontend.tgz
```
<br>

#### 後端 api
後端 api server 設定為 8080, 避開 nginx 80, ssl 443, redis 6379 即可
將 nginx.conf location /api 指向 8080, flask 中建立一個 /api router
(透過 sudo vim /etc/nginx/nginx.conf 修改)
(可以執行 sudo nginx -t 檢查 nginx 修改是否能正常運作)
(修改完 nginx 需要重啟 ＝> sudo systemctl restart nginx)

```
server {
    listen 80;
    server_name xxx.xxx.xxx.xxx 你的域名; // 對外後 ip 記得拔掉

    root /home/an/project/static;
    index index.html;

    location / {
        proxy_pass http://localhost:8080;
    }
}
```

#### [Godaddy DNS設定](https://dcc.godaddy.com/control/dns?domainName={你的域名})
- 設定 名稱伺服器 (NameServe)
    設定新的名稱伺服器為 VM 的 4個 NS值，將網域 DNS server 轉為由 VM Cloud DNS 代理。
    (為了讓DNS解析服務能夠使用您在Cloud DNS中設置的A記錄，當用戶訪問該網址時，DNS解析系統會自動將其轉換為目標網域名稱的IP地址。)
<br>

#### [VM Cloud DNS 設定](https://console.cloud.google.com/net-services/dns/)
- 進入https://dcc.godaddy.com/control/dns?domainName={你的域名} 設定 A & CName.
    A：address，回傳網域名對應的 IP 位址。它允許你將網域名稱映射到一個IP地址 (即VM外部IP)
    CNAME：Canonical Name，正準名稱記錄。將網域名映射到另一個網域名稱的DNS紀錄類型。
    它允許你創建一個別名，這樣當用戶訪問該網址時，DNS解析系統會自動將其轉換為目標網域名稱的IP地址。
    (ex: www.{你的域名})
<br>

- 綁定域名小總結
```
(1) godaddy 名稱伺服器新增四個值 為 vm 的 NS, 改為 vm dns 作為此網址的 dns 代理
(2) VM A 設定成 vm ip
(3) VM CNAME 設定成 www.你的domain.
(4) 綁定成功後 dig domain 確認是否成功將 domain ip 修改成 vm 外部 ip
```
<br>


#### 將外部ＩＰ固定
- 因重開機就會換ＩＰ，需要將ＩＰ固定保留靜態位址
    https://console.cloud.google.com/networking/addresses/
<br>

#### 建立 SSL
[建立負載平衡器流程](https://medium.com/%E5%B7%A5%E7%A8%8B%E9%9A%A8%E5%AF%AB%E7%AD%86%E8%A8%98/gcp-vm-%E8%A8%AD%E5%AE%9A-https-%E5%8F%8A-ssl-41c2406afad4)

- (1) 執行個體群組, 選擇 New unmanaged instance group，右邊位置選擇 VM 所在位置，後面帶入相關設定。
- (2) 負載平衡, 建立負載平衡器並填入前後端設定
- (3) 安全資料傳輸層政策 建立政策


