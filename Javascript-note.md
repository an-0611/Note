### 前端

### Project

**React & Redux**<br />
[Official](https://www.settour.com.tw)<br />
[taiwan](https://trip.settour.com.tw/taiwan/search)<br>
[一日遊](https://trip.settour.com.tw/taiwan/product/GDP0000000867)
[多日遊](https://trip.settour.com.tw/taiwan/product/GDP0000000856)
[高鐵假期](https://trip.settour.com.tw/taiwan/product/HRP0000000290)<br />
[hotel](https://hotel.settour.com.tw/search)<br />
[car](https://trip.settour.com.tw/car/search)<br />
[租車飯店](https://trip.settour.com.tw/car/product/CPP0000000085/RNT0000001878/201911)
[租車](https://trip.settour.com.tw/car/product/CPP0000000182/RNT0000001723/201911)<br />
[member](https://member.settour.com.tw/b2c/dashboard)<br />

<!-- [todolist](https://an-0611.github.io/Vuex/#/Todolist)<br />
[60秒快速測驗](https://an-0611.github.io/Vuex/#/Testing_60s)<br />
[chatRoom(待更新 轉vue版本 調整express設定)](https://an-0611.github.io/Vuex/#/ChatRoom)<br />
[匯率交換(api待修)](https://an-0611.github.io/exchangeRate/)<br />
[數獨(待更)](https://an-0611.github.io/Vuex/)<br />
[卡片配對(待更)](https://an-0611.github.io/Vuex/)<br />
[電影牆字幕(待更)](https://an-0611.github.io/Vuex/)<br />
[Travis & mocha](https://travis-ci.org/an-0611/mocha-testing)<br /> -->

### React

```markdown
### Redux

https://chentsulin.github.io/redux/docs/basics/UsageWithReact.html

### Redux Thunk

https://medium.com/frochu/%E9%80%81%E8%AE%93%E4%BD%A0%E7%9A%84action%E8%83%BD%E4%BD%9C%E6%9B%B4%E5%A4%9A-redux-thunk-c07bc5488e48
https://juejin.im/post/5b035c0c51882565bd258f12
https://note.pcwu.net/2017/03/20/redux-thunk-intro/

### Redux Saga

https://medium.com/itsoktomakemistakes/%E5%AD%B8%E7%BF%92-redux-saga-%E7%9A%84%E8%B5%B7%E6%89%8B%E5%BC%8F-db4fd3a4dbce

### Redux Observable

https://blog.techbridge.cc/2017/12/08/rxjs/

### Immutability

https://zh-hant.reactjs.org/tutorial/tutorial.html#why-immutability-is-important

### Hook

https://zh-hant.reactjs.org/docs/hooks-intro.html

### memory leak

http://souffle77-blog.logdown.com/posts/396672-what-is-a-memory-leak-memory-leak
this.ismounted = true/false
```

### Vue

```markdown
### Vue cli

https://cn.vuejs.org/v2/guide/
https://www.slideshare.net/kurotanshi/vuejs-62131923
http://www.shouce.ren/api/view/a/11726

### Vuex

https://vuex.vuejs.org/zh/guide/
```

### Express

```markdown
**build Express server**

### Install

1. npm install express

### Build

1. create server.js file
2. edit server.js

   const express = require("express");
   let app = express();
   app.use(express.static('dist')); // to load static source
   app.get('/', function(req, res){ // index Page
   res.sendFile(`__dirname` + '/dist/index.html');
   });
   app.listen(port, () => {
   console.log('app listening on port: ' + port) // node app.js
   })

3. node server.js
```

### Travis CI

[with mocha](https://travis-ci.org/an-0611/mocha-testing)
[Reference](https://reurl.cc/mdyVKY)

### Mocha

[Reference](https://reurl.cc/mdyVKY)

### Websocket

```markdown

```

### Algorithm

http://www.csie.ntnu.edu.tw/~u91029/

### Memorize

https://stackoverflow.com/questions/20103739/javascript-memoization

### Leetcode

```markdown
### String

### Array

https://leetcode.com/problems/find-common-characters/submissions/
https://lakesd6531.pixnet.net/blog/post/349410781-leetcode%E8%A7%A3%E9%A1%8C%E7%B3%BB%E5%88%97%E2%94%80peak-index-in-a-mountain-array 二分法
https://blog.csdn.net/fuxuemingzhu/article/details/71412574
https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Array/sort

### Object

### Dynamic Programming
```

### WebApi

1. [MutationObserver](https://an-0611.github.io/WebApi/MutationObserver)
2. [new URL](https://an-0611.github.io/WebApi/Url)

### Browser work

url 送出<br />
=> browser newwork process<br />
=> ui thread (接收 url 字串 & 發出請求給 network thread)<br />
=> network thread 發 http 請求 ( 做 DNS 抬頭, 並與 server 建立連線, 牽涉 DNS 查詢 TCP/IP 請求 五層應特網協議棧)<br />
=> server (接收 networkThread 請求)<br />
=> 對應後台 (接收來自 server 請求) (server & 後台牽涉到負載均衡 安全攔截 後台內部狀態)<br />
=> 後台與前台 http 交互 (http header, 響應碼, 報文結構, cookie, 可提靜態資源的 cookie 優化及編碼解碼 如 gzip 壓縮)<br />
=> 說明緩存問題 (http cache, etag, catch-control)<br />
=> 瀏覽器接收 http 數據包(說明 equest code 200..304..404..)並進行解析<br />
(解析 html-詞法分析然後解析成 dom 樹、解析 css 生成 css 規則樹、合併成 render 樹，然後 layout、painting 渲染、複合圖層的合成、GPU 繪製、外鏈資源的處理、 loaded 和 domcontentloaded 等)<br />
=> network thread(notify data ready to)<br />
=> ui thread<br />
=> browser process(use IPC to send Data)<br />
=> Render process<br />
=> CSS 的可視化格式模型（元素的渲染規則，如包含塊，控制框，BFC，IFC 等概念<br />
=> JS 引擎解析過程（JS 的解釋階段，預處理階段，執行階段生成執行上下文，VO，作用域鏈、回收機制等等<br />
=> 其它（可以拓展不同的知識模塊，如跨域，web 安全，hybrid 模式等等內容<br />

ps: 每個 render process 有配置其獨立的記憶體空間，因此除了必要的資源外並不共享，安全性較高。<br />
目前 Chrome 可做 site isolation，意即每個 iframe 也是由獨立運作的 renderer process 來負責執行，<br />
而這些 render process 又有分配獨立的記憶體空間，對於安全性來說，隔離不同網站的記憶體使用的資訊，<br />
可說是同源策略（same-origin policy）的第二層保護機制。<br />

render process<br />
=> (main thread & worker thread)<br />
=>1.main thread => 解析 HTML 字串並產生 dom tree , 同時若發現需下載的資源，<br />
就會透過 IPC 通知 browser process 的 network thread 來發出網路請求以取得該資源,<br />
或使用加速的 preload scanner 方法，意即在剖析 HTML 的同時掃描是否有需要下載的資源，<br />
若有就透過 IPC 通知 browser process 的 network thread 來發出網路請求以取得該資源，剖析與下載檔案平行進行<br />
2.worker thread

[Browser work reference - 1](https://segmentfault.com/a/1190000013662126)<br />
[Browser work reference - 2](https://cythilya.github.io/2018/11/26/what-happens-when-you-type-an-url-in-the-browser-and-press-enter/#%E4%B8%80%E7%80%8F%E8%A6%BD%E5%99%A8%E7%9A%84%E5%85%A7%E9%83%A8%E9%81%8B%E4%BD%9C%E6%A9%9F%E5%88%B6)<br />

## 待整

### Data Structure

[Data structure](https://blog.kdchang.cc/2016/10/08/front-end-engineer-toolbox-data-structure/)<br />

### Html

[Semantic Elements](https://www.w3schools.com/html/html5_semantic_elements.asp)<br />

### Css

[flex-1](https://wcc723.github.io/css/2017/07/21/css-flex/)<br />
[flex-2](https://www.oxxostudio.tw/articles/201501/css-flexbox.html)<br />
[transform-Matrix-1](https://www.oxxostudio.tw/articles/201409/svg-20-transform-matrix.html)<br />
[transform-Matrix-2](http://www.eion.com.tw/Blogger/?Pid=1168)<br />
[Scss](https://blog.techbridge.cc/2017/06/30/sass-scss-tutorial-introduction/)<br />
[Style Components](https://medium.com/@shihKai/%E4%BB%8B%E7%B4%B9%E6%92%B0%E5%AF%ABreact-css%E7%9A%84%E7%A5%9E%E5%A5%97%E4%BB%B6styled-components-77455c849198)<br />
[css questions](https://h5bp.org/Front-end-Developer-Interview-Questions/translations/chinese-traditional/#css-questions)<br />
[clearfix 4 method](https://kknews.cc/zh-tw/code/z82bo8g.html)<br />

### Javascript

[JS questions](https://h5bp.org/Front-end-Developer-Interview-Questions/translations/chinese-traditional/#css-questions)<br />

```markdown
**prototype**
instance = new + 構造函式(同時 this 指向該生成對象)
prototype => 即實例的公有函式
**proto** => 即指向父層 prototype(公有函式)的鏈結
相當於 Object.getPrototypeOf()，其下的 constructor 屬性會指向一個構造函式，實例被創建時即建立其相關參考。
建立的實例對象因此可以參考其構造函式 prototype 作為使用。
ex:
function salaryman(name) {
this.name = name;
}
salaryman.prototype.introduce = function() { console.log ('hello my name is ' + this.name ) }
var b = new salaryman('b') // 創建實例時也會自動將該對象(b)的**proto**自動指向 salaryman.prototype
var an = {};
an.**proto** = new salaryman('an'); // 即可使用其構造函式 prototype // !!但基本絕對避免這種寫法!!
an.introduce();
// 此時呼叫 introduce()，js 會檢查此參考構造函式 salaryman 是否有 introduce 這個函式，
// 如果沒有在往 salaryman 上層追查，直到**proto** = null，再也沒有構造函式可以參考為止，
// 以此實現 js 的繼承，為原型鍊。

             // 注意!!!! 此種方法 an.__proto__是直接指向實例salaryman，不同於b.__proto__是指向的salaryman.prototype
             // b在建立實例的時候__proto__會自動指向salaryman.prototype
             // 而an本身(非an.__proto__)因為缺少建立實例 是其屬性__proto__在建立實例
             // 會造成an.__proto__的指向會是salaryman實例而非salaryman.prototype，
             // b.__proto__ == salaryman.prototype // true
             // an.__proto__.__proto__ == salaryman.prototype // true
             // 雖然an一樣可以繼承introduce這個函式並使用
             // 不過an本身少了執行建構函式這個動作( salaryman.apply(an) ) 造成 an.__proto__ !== salaryman.prototype


P.S.

1. prototype 新增的函式不會 hoist
2. 產生的實例對象(如 b)只會有**proto**(原型鍊)，構造函式(如 salaryman)才有 prototype，
   而 prototype 底下的 constructor 屬性指向其自身構造函式(ex: salaryman.prototype.constructor == salaryman)

**New 後面執行的動作**
ex: var b = new salaryman('b')
step 1: 創出一個新的 obj
step 2: 把 obj 的 **proto** 指向 salaryman 的 prototype 繼承原型鍊
step 3: 拿 obj 當作 context，呼叫 salaryman 此建構函式
step 4: return obj
實際程式碼:
function Salaryman(name) {
this.name = name;
}

Salaryman.prototype.introduce = function () {
console.log(this.name);
}

function newObj(Constructor, arguments) {
var obj = new Object();
// 讓 obj 繼承原型鍊
obj.**proto** = Constructor.prototype;
// 執行建構函式
Constructor.apply(obj, arguments);
// 回傳建立好的物件
return obj;
}

var an = newObj(Salaryman, ['an']);
an.log(); // an

[New 參考-1](https://blog.techbridge.cc/2017/04/22/javascript-prototype/)<br />
[New 參考-2](https://pjchender.blogspot.com/2016/06/javascriptprototypeprototype.html)<br />

**event loop(事件循環)**
需先了解 程式(program)、線程(process)、進程(thread)及堆疊(stack)、佇列(queue)的差異。
**一、程式**(program): 相當於一個沒運作的 VSCode，尚未進入記憶體也沒被 CPU 所執行。
**二、進程**(process): 相當於一個正在運作的 VSCode，每開啟一個 VSCode 都是一個獨立的程式，佔用記憶體並作為執行序的容器，
需要 CPU、記憶體、檔案及 I/O 裝置等相互配合才可執行。一個瀏覽器分頁就相當於一個進程。
**三、線程**(thread): 相當於一個功能，即所謂的執行緒。VSCode 有新增與刪除功能，兩個功能都能對同一行文字進行操作(共享記憶體&變數)
又可分為單線程(simgle thread)與多線程(mulriple thread)
P.S.(單線程 => 一個進程只有一個線程， 多線程 => 一個進程有多個以上線程)
單線程： 優點 1. 記憶體消耗少 2. 處理 Non-Blocking(非阻塞式處理)消耗少
缺點 1. 易 IO 阻塞 2. 無法有效利用 CPU
多線程： 優點 1. 提高 CPU 使用率加快程序 2. 共享記憶體及變數 3. 處理高併發(單一時間內訪問量爆增)
缺點 1. 記憶體消耗高 2.單一執行緒崩潰可能造成整個程序崩潰 3.兩個以上執行續出現同時存取、更新全域變數，或線程互相等待等情況發生時會造成死鎖 4.解決單線程大量 IO 操作阻塞問題，ex:負載均衡

                  Javascript主要也為了解決Non-Blocking、事件驅動及其渲染方式所為，屬於單線程語言。
                  reference : https://reurl.cc/9z3NK8

包含了兩種資料儲存型態，分別為 stack(堆疊)與 queue(佇列)
**堆疊**(後進先出) : 即棧(stack)，排越後面優先做，遇到問題就先解決
**佇列**(先進先出) : 即任務佇列(task queue)，一個一個問題按照順序解決

Javascript 開始執行程式碼流程:
ex: function b() {}
function a() { b() }
a(); 1.創建執行環境(Global Execution Context): 建立 this 與全域物件(window)，並將 this 指向 window 2.運作執行環境(executing progress): 進入執行進程，程式碼開始由上至下一行一行執行，跳過尚未被執行函式當中的程式碼(b)，
並將全域變數及函式提升(hoist)至程式碼頂端，如果途中有函式執行，在此途中對該函式(a)
重複 step1.動作(創建 a()執行環境)，並在執行棧(stack)上堆疊此(a)執行環境。
P.S. hoisting 只負責變數提升，不包含賦值，且需待賦值後，TDZ 才會完整結束。 3.當 a()執行時，途中遇到 b()要執行，此時重複 step1.動作，創建 b()執行環境，並在執行棧(stack)的(a)執行環境上堆疊 b()執行環境。 4.待 b()當中程式碼完整結束，將 b()的執行環境移出整個執行棧，a()因為 b()已經移出執行棧，可以繼續完成 a()未完成的任務。 5.如此重複到清除整個執行棧

上面的流程為調用棧，屬於同步進行的區塊，但整個瀏覽器的運作除了同步，還包含了非同步(異步)，而 javascript 異步任務的執行，
就需要仰賴 event loop(事件循環)這個機制來運作，異步操作同時也包含宏任務(Macro Task)與微任務(Micro Task)兩種模式。
瀏覽器接收程式碼運作流程
ex: function A() { console.log('A') }
function B() { console.log('B') }
function C() { console.log('C') }
function D() { console.log('D') }

        var global = () => {
            A();
            setTimeout(() => {
                B();
            }, 0)
            Promise.resolve().then(() => {
                C();
            })
            D();
        }
        global();


1.  創建全域執行環境與 this(指向 window)，並跳過所有函式程式碼，執行 global()。// stack = [global()];
2.  創建 global()執行環境，同樣將 global()中 this 指向 window，跳過函式程式碼，執行 A()。// stack = [global(), A()];
3.  創建 A()執行環境，跳過函式並執行打印，打印完畢將 A()從執行棧(stack)中脫離，繼續執行 global()未完成部分。
    // stack = [global()];
4.  執行 global()的 setTimeout()＆promise()，但兩者皆為異步任務，通過 webApi 機制先使其脫其原本 stack，分別進入 task queue
    的宏任務及微任務中，並執行 D()。 // stack = [global(), D()]; macro = [setTimeout] ; micro = [promise];
    // 所有同步任務結束後，開始執行異步任務。
5.  創建 D()執行環境，跳過函式並執行打印，打印完畢將 D()從執行棧(stack)中脫離，此時 global()也執行完畢，從 stack 脫離。
    // stack = []; macro = [setTimeout] ; micro = [promise];
6.  此時剩下 task queue 中的 macro task & micro task，又微任務執行優先權高，透過 event loop 將微任務加入 stack 中執行。
    // stack = [promise]; macro = [setTimeout];
7.  待 promise 及其他微任務執行完，event loop 才會繼續將宏任務加入，一個一個運行直到整個 stack 清空。

總結:
所有的程式碼都必須在 執行環境中運行。
全域執行環境 是默認的第一個執行環境。
JavaScript 只有在 函式呼叫 發生時，才會建立新的執行環境。
執行環境相互堆疊後，會形成 執行堆疊。
執行堆疊具有 順序性，越新的執行環境會被擺在越高處，反之亦然。
JavaScript 是 單執行緒 的程式語言，一次只能做一件事。
JavaScript 會優先執行堆疊中 最頂端 的執行環境。
執行環境會在函式 return 之後，自動從堆疊中 pop off 消失。
(參考: https://reurl.cc/8lXQKR)

**closure**

### closure characteristic

1.可儲存當下執行環境的外層變數(回傳的 function 亦同) 2.重新宣告即產生新的執行環境 3.可保留執行環境
4.example:
const card = (function() {
let price = 0;
function change(newPrice) {
price += newPrice;
}
return {
autoStore: function() {
change(500);
},
increment: function(val) {
change(val);
},
decrement: function(val) {
change(val);
},
remain: function() {
return price;
}
}
})();

card.remain(); // 0
card.autoStore(); // + 500
card.remain(); // 500
card.increment(600); // + 600
card.decrement(-300); // - 300
card.remain(); // 800

**currying**

1. 將一個接受 n 個參數的 function，轉變成 n 個只接受一個參數的 function
2. 利用 closure 特性(保存執行環境及變數)
3. 將函式當作回傳值(可為匿名函式，宣告函式，IIFE...)
4. 複用性及可讀性高
   ex1:
   function add(a) {
   return function (b) {
   return a + b
   }
   }
   var num = add(5) // return function (b) { ... }
   // 參數 a 及函式 b 的執行環境被保留在變數 num 內
   num(7) // 12

ex2:
function curriedFetchData(path) {
var xmlHttp = new XMLHttpRequest();
var result = {};
xmlHttp.open( "GET", path, false );
xmlHttp.send( null );
result = JSON.parse(xmlHttp.responseText);
return function(\_callback) {
\_callback(result.data);
}
}

function showResult(result) {
console.log('The result is: ' + result);
}

var path = 'http://www.json-generator.com/api/json/get/bPQMSaHjsi?indent=2';
var getData = curriedFetchData(path);
getData(showResult); // The result is: Hello, World!

reference:
https://cythilya.github.io/2017/02/27/currying-in-javascript/

**Event bubble & capture**

var ul = document.getElementById('ul');
var li = document.getElementById('li');
var a = document.getElementById('a');

// ul.addEventListener('click', function(e) {
// console.log('ul')
// }, false) // 只要是 ul 底下的元素都會觸發此 listener 不論 true false

// ul.addEventListener('click', function(e) {
// console.log('ul')
// e.stopPropagation(); // 阻止事件向下傳遞，不管 true/false 一樣先捕獲，但點 li 不會向上冒泡至 ul，冒泡及捕獲都算傳遞
// 可利用 e.target == e.currentTarget 判斷是否為作用元素，避免冒泡觸發不必要 listener
// event delegation 事件委派 在父層元素註冊事件 指定給特定子元素
// e.currentTarget = 永遠指向監聽者 ul
// }, false)

// li.addEventListener('click', function(e) {
// e.stopImmediatePropagation(); // 同一個節點若有多個 listener 可以讓其他 listener stopPropagation 只觸發一次
// console.log('li')
// }, true)

// a.addEventListener('click', function(e) {
// console.log('a')
// }, true) // 第三個參數 default = false
// true 代表把這個 listener 添加到捕獲階段(就不會有沒有冒泡階段的監聽註冊)
false 或是沒有傳就代表把這個 listener 添加到冒泡階段。 (再確認是否正確)
// true 指向下傳遞不冒泡 // false 先捕獲在冒泡 (再確認是否正確)

// Q: 子代的 stopPropagation 造成父元素失效
// A: 把子代 stopPropagation 拿掉 並用 e.target == currentTarget 判斷榜定觸發元素

// CAPTURING_PHASE = 1; // 捕獲階段
// AT_TARGET = 2; // 事件傳到要捕獲的目標本身 就算目標冒泡也都是 2 沒有分捕獲跟冒泡，不管 true/false // 會依照先執行的程式碼進行 可能變成先冒泡後捕獲
// BUBBLING_PHASE = 3; // 冒泡階段

// e.stopPropagation(); // 阻止事件向下傳遞 // 如果第三個參數是註冊在 false，則向上冒泡 stopPropagation
// (這邊只的向下傳遞是指流程向下走 不是只父與子相對位置關係)
// 剩下的 listener 都不會再收到任何事件

// e.preventDefault 父層使用會傳遞下去

document.getElementById('ul').addEventListener('click', (e) => {
console.log('ul bubbling', e.eventPhase);
}, false)

// ul 的捕獲
document.getElementById('ul').addEventListener('click', (e) => {
console.log('ul capturing', e.eventPhase);
}, true)

// li 的冒泡
document.getElementById('li').addEventListener('click', (e) => {
e.stopPropagation();
console.log('li bubbling', e.eventPhase);
}, false)

// li 的捕獲
document.getElementById('li').addEventListener('click', (e) => {

console.log('li capturing', e.eventPhase);
}, true)

// li_link 的冒泡
document.getElementById('a').addEventListener('click', (e) => {
console.log('list_item_link bubbling', e.eventPhase);
}, false)

// a_link 的捕獲
document.getElementById('a').addEventListener('click', (e) => {
console.log('a_link capturing', e.eventPhase);
}, true)

**async**
Promise
Async/Await
Generator
https://cythilya.github.io/2018/11/01/generator/

**this**
紀錄當前環境，即調用者所在的執行棧層
this = 使用者付費，誰用的 this 就是誰，找不到使用者，政府(window)付費。
bind apply call() 指定誰是使用者
在物件下呼叫產生的 this 才有意義(OOP)

可參考https://github.com/aszx87410/blog/issues/39

**hoist**
https://blog.techbridge.cc/2018/11/10/javascript-hoisting/

**函數聲明 & 函數表達式**
函數聲明: 1.可以 hoist 2.任何地方皆可使用 3.不返回指向函數的引用，而是創建一個和函數同名的變量，將指向函數的引用賦值給這個變量 4.代表一個完整的語句
函數表達式: 1.不能 hoist(因將函數採用賦值方式，但 hoist 只提升變數宣告不提升賦值動作)，
2.TDZ 範圍內不可使用 3.返回一個引用，直接指向函數表達式創建的函數 4.只是語句的一部分

**執行函式過程**
執行一個函式時，一個新的執行環境(execution context)會被建立，
接著 JS 引擎會替我們建立 Variable Environment 來保存我們的變數，
然後建立 Outer Environment 來判斷變數的 Scope Chain，然後產生關鍵字 "this"，
而 this 的內容則會根據執行函式方式的不同而指稱到不同的物件。
然後建立 Outer Environment 來判斷變數的 Scope Chain，然後產生關鍵字 "this"，
而 this 的內容則會根據執行函式方式的不同而指稱到不同的物件。

https://pjchender.blogspot.com/2015/12/javascriptscope-chainouter-environment.html

**outerEnvironmemt** 1.呼叫一個在該 exection context 中沒有的變項時，它會往它的 outer environment 去找。
ex:
function b() {
console.log(str)
}
function a() {
var str = 2
b();
}
var str = 1
a() // str: 1 , outer environment 是 global

https://pjchender.blogspot.com/2015/12/javascriptscope-chainouter-environment.html

**scope chain**
查找變數的過程中，從內層找到外層，若找到即停止，該層找不到則向外層一層一層至最外面的 global environment
ex:
function a() {
function b() {
console.log(str)
}
var str = 2
b();
}
var str = 1
a() //str: 2

p.s. 但呼叫的值若為 this.str，因 this 已經榜定該物件執行環境下(純呼叫 str 則不被 this 影響)，不像 scope chain 未指定會一直追查上去，
此時若找不到 str 則直接返回 undefined
ex:
var a = {
value: 'a',
f: function() {
console.log(this.value)
},
}
var b = a.f;
a.f(); // 'a'
b(); // 指向 window.value 但 window.value 沒有宣告則返回 undefined

https://pjchender.blogspot.com/2015/12/javascriptscope-chainouter-environment.html

**arguments**

1. 為函式保留字
2. 包含所有參數值，為集合參數的類陣列(array-like)，可迭代(iterable)
3. 建立 Array instance 方能使用 Array prototype ( ex: Array.prototype.slice.call(arguments) )

https://pjchender.blogspot.com/2016/04/javascriptparameterargumentsspread.html

**Apply & Bind & Call & Arrow function **
作用: 改變函式中 this 的指向

1. call、apply => 回傳 function 執行結果
2. bind => 回傳綁定 this 後的原函數，且榜定後無法在被更改
3. call = fun.call(thisArg[, arg1[, arg2[, ...]]]);
4. apply = fun.apply(thisArg, [argsArray]);
5. Arrow function => 拿到的都會是當前作用域的 this, obj1 呼叫即以 obj1 為當前作用域, obj2 呼叫即以 obj2 為當前作用域, 以此類推...<br />
   不管是誰呼叫他，或是被如何 bind、call、apply，arrow 裡面的 this 永遠都是語意上的 this,拿到的都會是當前作用域的 this<br />
   ex:
   function log(p1, p2, p3) {
   console.log(this.text, p1, p2, p3)
   }
   var obj = {
   text: '123'
   }
   log.apply(obj, [1,2,3]); // 將 obj 指定為 wtf 這個方法的 this, 並帶入 iterable 參數(若無則為 null)當作執行 log 這個函式的參數
   log.call(obj, 1,2,3);
   log.bind(obj)(1,2,3)

---

window.a = 20;
function wtf() {
console.log(this.a);
}
var wtf_bind_window = wtf.bind(window);
var obj = { a: 1, func: wtf_bind_window };
obj.func(); // 20
obj.func.call(obj); // 20
obj.func.apply(obj); // 20
obj.func.bind(obj)(); // 20
```

### Implement

[promise](https://jsfiddle.net/h1tqv8g6/)

### Sorting

bucketSort(easy) https://juejin.im/post/5853542c61ff4b006848e8bb
bucketSort(medium) http://marklin-blog.logdown.com/posts/1910182
quickSort http://shubo.io/quick-sort-quick-selection/

### Built In Funcion

1. [Array](https://an-0611.github.io/Built-In-Function/Array)
2. [String](https://an-0611.github.io/Built-In-Function/String)
3. [Number](https://an-0611.github.io/Built-In-Function/Number)
4. [Object](https://an-0611.github.io/Built-In-Function/Array)
5. [Date](https://an-0611.github.io/Built-In-Function/Date)
6. [Math](https://an-0611.github.io/Built-In-Function/Math)
7. [JSON](https://an-0611.github.io/Built-In-Function/JSON)
   11/08 update (先整完 firebase data)

### Built In Object

1. [Map](https://an-0611.github.io/Built-In-Function/Map)
2. [Set](https://an-0611.github.io/Built-In-Function/Set)

### call by reference & call by value & call by sharing

note. (儲存的是記憶體位址)
https://blog.techbridge.cc/2018/06/23/javascript-call-by-value-or-reference/

### copy & deepcopy

https://larry850806.github.io/2016/09/20/shallow-vs-deep-copy/

### RegExp

https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Guide/Regular_Expressions

### sideEffect & pure function

https://ithelp.ithome.com.tw/articles/10185780

### Data structure

https://blog.kdchang.cc/2016/10/08/front-end-engineer-toolbox-data-structure/

### Optimization

**Html**<br />
stylesheet<br />

**Css**
inline
preload(字體 圖片)<br />
prefetch<br />
preconnect<br />
寫法 minify<br />
延遲(js load css)<br />
字體 js 加載(但要避免 flash)<br />
loadcss lib<br />
置放<head><br />
subdomain: http1.0/1.1 支持同時發多個請求，並發請求多個資源當然比一個一個的請求快，<br />
可是在同一個域名下，瀏覽器並發請求的數量是有限制的（chrome 為 6 個），如果要突破限制，就只能使用不同域名來請求資源<br />

**Js**<br />
async/defer(p.s,. need src attibute)<br />
tree shake<br />
IIFE<br />
全局對象私有參數化<br />
reference<br />
lazyload<br />
cdn<br />
browser cache<br />
dns 預解析<br />
打包<br />
after DomContentLoader done, then load js<br />
progressive render<br />
寫法 minify<br />
置放</body><br />
subdomain(chrome limit 6 files)<br />
decrease http request<br />
global object to parameterize<br />

reference & other optimization: https://www.jishuwen.com/d/2IGR/zh-tw

**Image**<br />
快取靜態資源<br />
base64<br />
sprite<br />

### Session & cookie

若今天替某個 Client 端的 Request 建一個 Session 的時候，<br />
Server 會先檢查這個 Client 端的 Request 裡是否有包含了 Session 標識(Session id)，
如果已包含一個 Session id，表示這個發起 Request 的 Client 端是已經存放過的 id，<br />
Server 就按照 Session id，把這個 Session 找出來使用。<br />
但如果 Client 端請求不包含 Session id，則表示他是新臉孔，
那 Server 端就為此 Client 端創建一個 Session，並生成一個 Session id，並 Response 給 Client 端保存。<br />

[session & cookie - 1](https://kknews.cc/zh-tw/code/gglegle.html)<br />
[session & cookie - 2](https://medium.com/@hulitw/session-and-cookie-15e47ed838bc)<br />

### Http

[http request response dns](https://yakimhsu.com/project/project_w4_Network_http.html)<br />

### Http Cache

https://blog.huli.tw/2017/08/27/http-cache/

### Http Request & Request/Response Header

https://yakimhsu.com/project/project_w4_Network_http.html

### TCP/IP

OSI(Open System Interconnection Model)由 ISO 提出，將電腦網路結構劃分成七層<br />

OSI 模型(七層) TCP/IP 模型(四層) TCP/IP 協議棧 <br />

第七層 => 應用層(application Layer) 應用層(Application Layer)(傳輸的資料內容:HTTP、FTP) 7. dns<br />
第六層 => 表示層(Presentation Layer) (該應用層包含表示層 & 會話層) 5.6 在協議為同一層 如下<br />
第五層 => 會話層(Session Layer) ex:FTP/HTTP/TELNET NTP/TFTP/SNMP<br />
第四層 => 傳輸層(Transport Layer) 傳輸層(Transport Layer)(傳輸的方式:TCP/UDP) 4. TCP or UDP<br />

第三層 => 網路層(NewWord Layer) 網路互聯層(Internetwork Layer)(傳輸的地址: IP) 3. IP<br />

第二層 => 資料連結層(Data Link Layer) 網路訪問層(Newwork Access Layer)(實體傳輸:乙太網路、WIFI) 1. % 2. ex: 乙太網 <br />
第一層 => 實體層(Physical Layer) (該網路訪問層包含實體層) <br />

======================================================================================================================

實體層(Physical Layer) => 為硬體裝置，為資料端裝置提供傳送資料的通路。 ex: 數據機、網卡、乙太網、光纖纜線、區域網路、廣域網路、WIFI。<br />
資料連結層(Data Link Layer) => 兩個網路實體之間提供資料鏈路連接的建立、維持和釋放管理。建立資料鏈路資料單元（frame：資料框或訊框)，<br />
又可系分為 MAC/LLC 並對資料進行封裝。 ex: 區域網路，廣域網路<br />
網路層(Network Layer) => 提供路由(同一網路通訊不用網路層，但不同網路通訊則需要)，使用 IP 位址來唯一標識網際網路上的裝置，<br />
網路層依靠 IP 位址進行相互通訊。決定資料的路徑選擇和轉寄，將網路表頭（NetworkHeader）加至資料包，<br />
以形成封包。網路表頭包含了網路資料。 ex: IPv4(2 的 32 次方)，IPv6(2 的 128 次方)<br />
傳輸層(Transport Layer) => 可分為 TCP(大部分網路協定，穩定) & UDP(需求是傳輸快速，並不是穩定的情況下，有快速、重複傳送資料特性，如:視頻)<br />
兩種協議。 將 IP 的兩個終端機系統之間的傳送服務(即網路層封包)，延伸為在終端系統上執行的兩個行程之間的傳送服務<br />
(即串接網路與電腦實體)。<br />
  
 TCP : 1. 提供壅塞控制(避免一 TCP 連線用大流量塞滿主機間的連結與交換器)<br /> 2. 透過流量控制、序列編號、確認訊息、計時器來確保資料能夠正確、依序的傳送行程<br />
  
 UDP : 1.流量是不受規範<br />
TCP 穩定原因: 3 times handshake<br /> 1. client(發送一個帶 SYN 標誌的 TCP 報文到伺服器) => server<br /> 2. server(帶 ACK 標誌和 SYN 標誌。表示對剛才用戶端 SYN 報文的回應) => client<br /> 3. client(必須再次回應服務段一個 ACK 報文) => server<br />
!! TCP 是"全雙工"系統的，正常時候是需要雙方通道都要測試是否開啟成功才行<br />
而因為在第二次握手的時候，伺服器不僅發送了確認報文(ACK)，也發送了要與用戶端相關的報文 SYN,<br />
詢問用戶端是否準備資料通訊，這樣就省了一個報文的發送。<br />
p.s. 第四次 hankshake => 串連終止協議<br /> 1. client 端(TCP)發送一個 FIN，用來關閉客戶到伺服器的資料傳送 => server<br /> 2. server(接收 FIN 並且回傳 ACK 報文，接著關閉串連，同時也傳出一個 FIN 報文) => client<br /> 3. client(接收 server 回傳的 ACK & FIN 報文，確認 ACK 報文後確認序號設定+1) //確認序號 = 收到的序號(FIN)<br />

reference: 1. [3 times handshake](https://topic.alibabacloud.com/tc/a/interview-frequently-questions-tcp-three-times-handshake-and-four-times-handshake_8_8_20192249.html)<br />  
 2. [TCP / UDP compare - 1](http://dns2.asia.edu.tw/~wzyang/slides/info_net/info_B/CH10TCP.pdf)<br /> 3. [TCP / UDP compare - 2](https://sls.weco.net/node/10656)<br /> 4. [TCP / IP model - 1](https://www.geeksforgeeks.org/tcp-ip-model/)<br /> 5. [TCP / IP model - 2](http://ccnatiy.blogspot.com/2015/01/presentation-layer.html)<br />

會議層(Session Layer) => 負責在資料傳輸中設定和維護電腦網路中兩台電腦之間的通訊連接。<br />  
 client 端的應用程式提供了開啟、關閉和管理會話的機制，亦即半永久的對話。<br />  
 TCP/IP 模型中已被棄用，應用層的 HTTP 有類似機制。<br />  
 應用: 電視直播節目中，在那裡音訊和影片的串流串從一個到另一個合併或轉換時要無縫，以免出現無聲通話時間或過度重疊<br />

表達層(Presentation Layer) => 把資料轉換為能與接收者的系統格式相容並適合傳輸的格式，為不同終端的上層用戶提供資料和資訊正確的語法。<br />  
 負責資料語法轉換、加密解密、壓縮解壓縮、編碼及解碼等工作(簡單理解為格式轉換層)。<br />  
 TCP/IP 模型中已被棄用。應用層的 HTTP、FTP、Telnet 等協定有類似的功能。傳輸層的 TLS/SSL 也有類似功能。<br />

應用層(Application Layer) => 應用層直接和應用程式介面結合，並提供常見的網路應用服務。應用層也向第六層表現層發出請求。<br />  
 提供為應用軟體而設的通訊 ex: http、https、ftp、ssh、smtp、DNS<br />  
 // DNS 伺服器將名稱請求轉換為 IP 地址 控制使用者在 Web 瀏覽器中輸入網域名稱時要連接的伺服器。這些請求稱為查詢<br />

reference: https://yakimhsu.com/project/project_w4_Network_TCP_IP.html

### IP(固定 浮動 虛擬)

Port 連接埠（端口）=> 同一個電腦上可能有對應到不同的服務，所以用 Port 來區別，接收不同的服務請求<br />
[IP-1](https://yakimhsu.com/project/project_w4_Network_TCP_IP.html)<br />
[IP-2](https://ithelp.ithome.com.tw/questions/10000796)<br />

### Security

Csrf(Cross-site request forgery)
Xss(Cross Site Script)
SQL Injection
DDos
target \_blank noopener noreferrer
[OWASP](https://www.owasp.org/index.php/Main_Page)

### Coercion

https://cythilya.github.io/2018/10/15/coercion/

### Database

```markdown
**Firebase**
Realtime Database 為線上 NoSQL 資料庫，主要有幾個特性 1.即時更新 2.透過 JSON 進行資料存取 3.串接其他 google 服務 e.g. Google Analytics 4.可進行 A/B test 5.免費仔福音 (1GB DB 儲存空間， 10GB/月下載量)
如何使用
**step1: 初始化 firebase**

const config = {
apiKey: "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXX", // 網路 API 金鑰
authDomain: "專案名稱.firebaseapp.com", // 專案名稱
databaseURL: "https://專案名稱.firebaseio.com", // db url
messagingSenderId: "1234567890", // 寄件者 ID
projectId: "project-1234567890", // 公開名稱
storageBucket: "",
};
firebase.initializeApp(config);

**step2: Firebase 的 CRUD **
使用 Realtime Database 前需先了解其 built-in function
ref() => 資料庫的相對路徑 預設為根目錄(("/")) 基本所有操作接需先 ref 指定路徑
set() => 執行動作為"覆蓋"，需小心覆蓋掉原本檔案，且欄位皆為物件格式，不可為陣列
on() => 隨時監聽 db 資料，若有更新會即時回傳
once() => 僅讀取一次 db 資料，不同於 on()，若 db 有更新 需重新呼叫
push() => 與 set()相似，但 push()為隨機產生編號，set()則可以自定義編號
child() => 相對的子路徑
var db = firebase.database();

1.  C => db.ref("school").push({ count: '20'})
    格式如下 :
    project-name : {
    school: {
    隨機編號 1: {
    count: '20'
    },
    隨機編號 2: {
    count: '20'
    },
    }
    }
2.  R => db.ref("/").once("value").then(data => { return data.val() }) // 直接回傳資料即可取得
3.  U => db.ref("/school/classA").set({'child' : 20}).then(res => { console.log("成功更新 classA 人數"); })
    格式如下 :
    project-name : {
    school: {
    classA: {
    child: 20
    }
    }
    }
4.  D => db.ref("/").child('school/classA').remove(); // 移除整個 classA 物件
5.  listener => db.ref("/school/classA").on("value", (data) => { document.getElementById('child-count').textContent = data.val().child });

**step3: Firebase 的資料排序**
orderByChild("key") => 依照"key"欄位進行排序

使用下列條件過濾時 orderByChild() 需先經由排序過資料
startAt(n) => 取 n 以上的值
endAt(n) => 取 n 以下的值
equalTo(n) => 取等於 n 的
limitToFirst(n) => 從前面開始 取 n 筆資料
limitToLast(n) => 從後面開始 取 n 筆資料

example :
var school = {
"classA" : {
"childCount": 20
},
"classB" : {
"childCount": 30
},
"classC" : {
"childCount": 40
}
}
var db = firebase.database(); 1.資料依照欄位值排序
db.ref('school').orderByChild('childCount').once("value", (data) => {
data.forEach(childCount => {
console.log(childCount.val())
})
})

2.取出 N 筆資料
db.ref('school').orderByChild('childCount').startAt(20).once("value", (data) => {
data.forEach(childCount => {
console.log(childCount.kchildCount.val())
})
}) 3.取出的資料依照值排序 在設定條件篩選
db.ref('school').orderByChild('childCount').limitToLast(2).once("value", (data) => {
data.forEach(childCount => {
console.log(childCount.kchildCount.val())
})
})

**MySql**
```

### Firebase Reference

[firebase](https://kanboo.github.io/2017/12/26/Firebase-studynotes/)

### Git

[Reset commit](https://gitbook.tw/chapters/using-git/reset-commit.html)<br />
[Reset remote branch](https://blog.csdn.net/top_code/article/details/50381432)<br />
衝突<br />
[Refusing to merge unrelated histories](https://blog.csdn.net/wd2014610/article/details/80854807)<br />
merge 衝突<br />
https://cythilya.github.io/2018/05/27/git-merge-and-solve-conflict/<br />
本地不是最新 解衝<br />
Updates were rejected because the tip of your current branch is behind<br />
https://www.jianshu.com/p/004f47f908c5<br />
1.git pull origin master<br />
2.git pull origin master --allow-unrelated-histories<br />
https://blog.csdn.net/wd2014610/article/details/80854807<br />
3.git add .<br />
4.git commit -m 'first commit'<br />
5.git push origin master<br />

### Docker

[環境部署](https://blog.hellosanta.com.tw/%E7%B6%B2%E7%AB%99%E8%A8%AD%E8%A8%88/%E4%BC%BA%E6%9C%8D%E5%99%A8/%E6%95%99%E4%BD%A0%E4%B8%80%E6%AC%A1%E5%AD%B8%E6%9C%83%E5%AE%89%E8%A3%9D-docker-%E9%96%8B%E5%A7%8B%E7%8E%A9%E8%BD%89-container%C2%A0%E5%AE%B9%E5%99%A8%E4%B8%96%E7%95%8C)<br />

### Others

[immutable](https://github.com/kdchang/reactjs101/blob/master/Ch06/react-immutable-introduction.md)<br />
[get/post](https://medium.com/@totoroLiu/http-post-%E5%92%8C-get-%E5%B7%AE%E7%95%B0-928829d29914)<br />
[event delegation](http://cythilya.blogspot.com/2015/07/javascript-event-delegation.html)<br />
[event bubble](http://shubo.io/event-bubbling-event-capturing-event-delegation/)<br />
[Https(對稱非對稱)-1](https://www.itread01.com/content/1547119204.html)<br />
[Https(對稱非對稱)-2](https://medium.com/@RiverChan/%E5%9F%BA%E7%A4%8E%E5%AF%86%E7%A2%BC%E5%AD%B8-%E5%B0%8D%E7%A8%B1%E5%BC%8F%E8%88%87%E9%9D%9E%E5%B0%8D%E7%A8%B1%E5%BC%8F%E5%8A%A0%E5%AF%86%E6%8A%80%E8%A1%93-de25fd5fa537)<br />
[virtual memory-1](https://sls.weco.net/node/21329)<br />
[virtual memory-2](https://mropengate.blogspot.com/2015/01/operating-system-ch9-virtual-memory.html)<br />
[webpack-1](https://webpack.docschina.org/concepts/plugins/)<br />
[webpack-2](https://medium.com/i-am-mike/%E4%BB%80%E9%BA%BC%E6%98%AFwebpack-%E4%BD%A0%E9%9C%80%E8%A6%81webpack%E5%97%8E-2d8f9658241d)<br />
[webpack-3](https://www.yumingyuan.me/2017/02/06/Getting-Started-With-Reactjs-Using-Npm-Webpack.html)<br />
[webpack plugin](https://rhadow.github.io/2015/05/30/webpack-loaders-and-plugins/)<br />
[Tree shake](https://juejin.im/post/5a4dc842518825698e7279a9)<br />
[DOMContentLoaded](https://github.com/fi3ework/blog/issues/3)<br />
DOMContentLoaded stylesheet 載入並完成解析才會被觸發<br />
資料結構<br />
[binary tree-1](http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html)<br />
[binary tree-2](http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html)<br />
[Data structure](https://blog.kdchang.cc/2016/10/08/front-end-engineer-toolbox-data-structure/)<br />
[二維陣列](https://blog.kdchang.cc/2016/06/23/javascript-data-structure-algorithm-array/)<br />
[離散數學](https://www.slideshare.net/ccckmit/ss-57362287)<br />
[線性代數](https://web.math.sinica.edu.tw/math_media/d192/19208.pdf)<br />
[雜湊-1](https://ithelp.ithome.com.tw/articles/10208884)<br />
[雜湊-2](https://blog.m157q.tw/posts/2017/12/25/differences-between-encryption-and-hashing/)<br />
<br />
[Object.propertyDefine](https://imweb.io/topic/56d40adc0848801a4ba198ce)<br />
[AMD CMD UMD](https://segmentfault.com/a/1190000004873947)<br />
[three way handshake](https://notfalse.net/7/three-way-handshake)<br />
[框架比較](https://www.itread01.com/content/1549206362.html)<br />
[server side render(react)](https://blog.techbridge.cc/2016/08/27/react-redux-immutablejs-node-server-isomorphic-tutorial/)<br />
[operator](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Guide/Expressions_and_Operators)<br />
[spread operator & rest operator](https://pjchender.blogspot.com/2017/01/es6-spread-operatorrest-operator.html)<br />
[npm dev dep](https://chriskang028.wordpress.com/2017/07/05/%E5%BC%84%E6%87%82-npm-install-%E7%9A%84-dependencies-v-s-devdependencies/)<br />
[git 解衝](https://cythilya.github.io/2018/05/27/git-merge-and-solve-conflict/)<br />
[Create react app Build gf-page -1](https://reactgo.com/deploy-react-app-github-pages/)<br />
[Create react app Build gf-page -2](https://medium.com/@aaa24295234/%E5%B0%87create-react-app%E4%BD%88%E7%BD%B2%E5%88%B0github-pages-1a7ba468861a)<br />
[Create Vue gf-page](https://medium.com/@dean34520/vue%E7%B3%BB%E5%88%97%E6%96%87-%E5%B0%87vue%E6%AA%94%E6%A1%88%E9%83%A8%E7%BD%B2%E8%87%B3github-334951cadede)<br />
[遞迴](https://kopu.chat/2017/08/19/%E9%81%9E%E8%BF%B4-recursive-%E4%BB%8B%E7%B4%B9%E8%88%87%E7%B6%93%E5%85%B8%E9%A1%8C%E5%9E%8B/)<br />
[Redis](https://blog.techbridge.cc/2016/06/18/redis-introduction/)<br />
[Execution context & Scope](https://openhome.cc/Gossip/JavaScript/ScopeChain.html)<br />
[改變原陣列 method](https://ithelp.ithome.com.tw/articles/10194227)<br />
[jwt](https://mgleon08.github.io/blog/2018/07/16/jwt/)<br />
[]()<br />
[]()<br />

### 保留 README 語法參考

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1

## Header 2

### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/an-0611/an-0611.github.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

[Question - 1](https://gist.github.com/hanksudo/5873678)<br />
[Question - 2](https://h5bp.org/Front-end-Developer-Interview-Questions/translations/chinese-traditional/#css-questions)<br />
[Answer](http://bbandydd.github.io/blog/2015/07/23/f2e-question/)<br />
https://yakimhsu.com/project/project_w4_Network_http.html<br />
[Array, linked list 實作 stack](http://alrightchiu.github.io/SecondRound/stack-yi-arrayyu-linked-listshi-zuo.html#ll)<br />
[clearCode 中譯](https://github.com/AllJointTW/clean-code-javascript?fbclid=IwAR0M5O2SkWZRByLHuG-lV0u0sqN78SHugs7N5LLrNePeWpcKDhazZ0hP2O4)<br />

平攤分析
https://mropengate.blogspot.com/2015/06/algorithm-amortized-analysis.html

webpack ゼロから https://medium.com/html-test/%E5%BE%9E%E7%84%A1%E5%88%B0%E6%9C%89%E5%BB%BA%E7%AB%8B-webpack-%E8%A8%AD%E5%AE%9A%E6%AA%94-%E4%B8%80-42fbc76a2d37

webpack
https://medium.com/i-am-mike/webpack%E6%95%99%E5%AD%B8-%E5%9B%9B-javascript-%E8%88%87-babel-1d7acd911e63

bower
https://blog.wu-boy.com/2013/01/bower-is-a-package-manager-for-the-web/

http request response
https://yakimhsu.com/project/project_w4_Network_http.html

StringNumber => EnglishNumber
function trans(s) {
// if (!s) return '';
var arr = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'];
var arr1 = ['', 'ten', 'twenty', 'thirty','forty','fifty','sixty','senvety','eighty','ninety'];
for(let i = 21; i < 100; i++) { arr[i] = arr1[Math.floor(i/10)] + ' ' + arr[i%10] }
for(let i = 100; i < 1000; i++) { arr[i] = arr[Math.floor(i/100)] + ' hundred ' + arr[i%100] }

    var num = Number.parseInt(s);
    var str = '';
    if (num >= 1 && num < 1000) return arr[num];
    while(num > 0) {
    	if (num > 1000 && num < 1000000) {
    		str += arr[Math.floor(num/1000)] + ' thousand ' + arr[num - (1000 * Math.floor(num/1000))] // ex: 19000 arr[19000/1000] + 'thousand' + arr[剩餘數字%1000]
    		break;
    	}
    	if (num >= 1000000 && num < 100000000) {
    		str += arr[Math.floor(num/1000000)] + ' million '
    		num -= 1000000 * Math.floor(num/1000000);
    	}
    	if (num >= 100000000) {
    		str += arr[Math.floor(num/100000000)] + ' billion '
    		num -= 100000000 * Math.floor(num/100000000);
    	}
    	if (num < 1000) { // 避免上面三種case num直接變成<1000
    		str += arr[num];
    		break;
    	}
    }
    return str.split(' ').filter((el) => { return el }).join(' ');

}

trans('1123456789')

### Regexp

```markdown
常用正規
// https://jimmy0222.pixnet.net/blog/post/36958819
(1)手機驗證
(2)email
(3)onlyInt
(4)onlyEng
(5)onlyChinese
(6)only

正規符號代表
// http://ccckmit.wikidot.com/regularexpression
https://chentsu.wordpress.com/2014/03/03/javascript-%E6%AD%A3%E8%A6%8F%E8%A1%A8%E9%81%94%E5%BC%8F-regexp-%E5%AF%AB%E6%B3%95/

// example:
/[0-8]+/.test('9') // false
/^09\d{8}$/.test('0912345678') // 台灣電話正規
/^[a-z]{1}[1||2]\d{8}$/i.test('H121000000') // 身分證
/\w+\@\w+\.[a-z]+$/g.test('123@gmail.com') // email 驗證

// 其他參數
//g 進行全局比對 對大小寫敏感
//i 且大小寫不敏感 (預設接為對大小寫敏感)

exec 返回一個索引配對 找不到則回傳 null
var test = RegExp('foo*', 'g')
test.exec('foooooo foo');
console.log(test) // /foo*/g
console.log(test.lastIndex) // 7

var test = /foo\*/g.exec('foooooo foo');
console.log(test) // ["foooooo", index: 0, input: "foooooo", groups: undefined]
console.log(test.lastIndex) // undefined

!!!!!!!!!notice!!!!!!!!!
\b 代表邊界 但不代表空白 沒有空白也可以處於邊界

\ : 協助字元跳脫

\b : 代表邊界 !!!! 判斷該字元是否屬於邊界
/\bstr/.test('str') // true
/\bstr/.test(' str') // true
/k\bstr/.test('str') // false
/k \bstr/.test('k str') // true
/k\bstr/.test('kstr') // false // !!!!!! 代表 str 左邊需為邊界 但左邊又一定要連接 k 故不可能達成

^ : 比對開頭
/^A/.test('A') // true
/^An123/.test('An123') // true
/^An123/.test('An124') // false
other case
// more: https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Guide/Regular_Expressions#special-negated-character-set

$ : 比對結尾 與^相對
/gmail\.com$/.test('123.gmail.com') //true
/com$/.test('123.gmail.aaacom') // true // 只要結尾是 com 即可

- : 匹配前一個字元 0~多次
  /aaaa*/.test('aaa') // true
  /aaaa*/.test('aaaaaaaaa') // true
  /aaaa\*/.test('aaaaaaaaa') // true

* : 匹配前一個字元 1~多次 // equal {1,}
  /abcd+/.test('abcd') // true
  /abcd+/.test('abcddd') // true
  /abcd+/.test('abc') // false
  /\d+/.test('123abc') // \d = [0-9] /\d+\/代表 0-9 出現 1~多次, 123 皆可匹配
  /\d+?/.test('123abc') // true // 但只匹配 1 (+ : 1~\*, ? : 0~1)

? : 匹配'前一個字元' 0~1 // equal {0,1}
/e?le?/.test('angel') // true e.g. ['l','el', 'le', ele] all true

. : 匹配換行後(小數點逗號都可)的字串 換行前不配對 // e.g.比對第二次說過的相同自
/.hello/.test('hello. hello') // true // 換行為小數點.
/.hello/.test('hello, hello') // true // 換行為逗號,
/.hello/.test('hello, 123') // false
/.hello/i.test('hello, Hello') // true

(x) : 匹配 'x' 並記住此次的匹配
/(foo)(bar)\1\2/.test('foobarfoobar') // true
/(foo) (bar) \1 \2/.test('foo bar foo true') // true \1 = 重複第一組()內的字串, /(foo) (bar) \1 \2/ 相當於 (foo) (bar) (foo) (bar)
/(foo) (bar) \1 \2/.test('foo bar bar foo') // false
// replace 方法 可用於交換
'bar boo'.replace(/(...) (...)/, '$2 $1') // 'boo bar'

???????????????????????????
(?:x) : 找出 'x'，這動作不會記憶, ()為 group 的意思，檢查時會再 wrap 一次，若有 g flag 會無效， ?: 代表只要 group 就好，不要 wrap
有無 () 差別
'123 abcd'.match(/123 (abcd)/) // ["123 abcd", "abcd", index: 0, input: "123 abcd", groups: undefined] // 針對括號內會在比對一次
'123 abcd'.match(/123 abcd/) // ["123 abcd", index: 0, input: "123 abcd", groups: undefined]
有無 ?: 差別
'foo'.match(/(foo){1,2}/) // [ 'foo', 'foo', index: 0, input: 'foo' ]
'foo'.match(/(?:foo){1,2}/) // [ 'foo', index: 0, input: 'foo' ] 連()都沒有，則{1,2}只是適用在 foo 的第二個 o 的條件而已。 // 因為

x(?=y) : 符合'x'，且後接的是'y'。'y'為'x'存在的意義。
/Jack(?=Sprat)/ => 在後面是 Sprat 的存在下，Jack 才有意義。
/Jack(?=Sprat)/.test('JackSprat') // true
/Jack(?=123)/.test('JackSprat') // false

x(?!y) : 符合'x'，且後接的不是'y'。'y'為否定'x'存在的意義，後面不行前功盡棄(negated lookahead)。
/\d+(?!\.+)/.test('1.') // false
var result = /\d+(?!\.)/.exec("3.141") // 找到數字後面不為點的 數字為 1~多個且後面不是.
// result 執行出來為[ '141', index: 2, input: '3.141']，
// index:2，代表 141 從 index = 2 開始。 從 2 開始匹配

x|y : 符合「x」或「y」 // 可以多個|
/a|b|c/.test('a') // true
/a|b|c/.test('b') // true
/a|b|c/.test('c') // true
/a|b|c/.test('d') // false

{n} : 規定符號確切發生的次數，n 為正整數 // 超越 n 後的配對不匹配
/a{2}/.exec('aaapple') // ["aa", index: 0, input: "aaapple", groups: undefined] // 只配對到前面兩個
/a{1}/.test('apple') // true
/a{2}/.test('apple') // false

{n,m} : 搜尋條件：n 為至少、m 為至多，其 n、m 皆為正整數。若把 m 設定為 0，則為 Invalid regular expression。 // 只配對到前 n 個
/\d{3,4}(?=\.)/.test('1234.') // true 至少三個或最多四個數字 且後面為.

[xyz] : !!!!!!!!!!!!!!!字元的集合。此格式會匹配中括號內所有字元, including escape sequences。
!!!特殊字元，例如點（.） 和米字號（_），在字元集合中不具特殊意義，所以不需轉換。
!!!若要設一個字元範圍的集合，可以使用橫線 "-"。
/[a-x]/.test('z') // false
/[a-z]+/i.test('A') // true
/[abc]+/i.test('A') // true
/[a-z.]+/.test('a') // true // 此時 . 失效 (_ 一樣失效)

[^xyz] : !!!!!!! " ^ " 在[]內代表排除這些字
/[^a-z]/.test('1') // true
/[^abc]/.test('c') // false
/[^abc]/.test('d') // true

???????????????
[\b] : 吻合倒退字元 (U+0008). (不會跟 \b 混淆)

\b : 吻合文字邊界 !!!!!!!!!!沒有元素或空白都算是邊界 但空字串 test 會 return false
/\b/.test('a') // true 兩邊都是邊界
/\b/.test('') // false

\B : 吻合非文字邊界
/y\B./.test('y') // false
/y\B./.test('y ') // false // 空白也算是邊界
/y\B./.test('y y') // false // 兩個 y 的旁邊都不是邊界 !!!!!!!!!!沒有元素或空白都算是邊界
/y\B./.test('y ya') // true // y 的旁邊不是邊界 是 a
/y\B./.test('ya') // true; // y 的旁邊不是邊界 是 a
/y\B./.test('possibly yesterday')

???????????????
\cX : 匹配由 x 指明的控制字元。例如，\cM 匹配一個 Control-M 或回車符。x 的值必須為 A-Z 或 a-z 之一。否則，將 c 視為一個原義的“c”字元。

\d : 吻合數字，寫法等同於 [0-9]
/\d/.test('a') // false
/\d/.test('1') // true
/[0-9]/.test('1') // true

\D : 吻合非數字
/\D/.test('1') // false
/\D/.test('a') // true
/\D/g.test('a1') // true // 能找到 a
/\D/g.test(' ') // true // 空白也算非數字

\f : 匹配一個換頁符。等價於\x0c 和\cL。

\n : 匹配一個分行符號。等價於\x0a 和\cJ。

\r : 匹配一個回車符。等價於\x0d 和\cM。

\s : 匹配任何空白字元，包括空格、定位字元、換頁符等等。等價於[\f\n\r\t\v]。
/\s/.test(' ') // true
/\s/.test('') // false

\S : 匹配任何非空白字元。等價於[^\f\n\r\t\v]。
/\S/.test('') // 與/s 一樣為 false 無字串匹配
/\S/.test(' ') // false
/\S/.test('a') // true

\t : 匹配一個定位字元。等價於\x09 和\cI。

\v : 匹配一個垂直定位字元。等價於\x0b 和\cK。

\w : 匹配數字字母與底線，等同於[A-Za-z0-9_]。
/\w/.test('A') // true
/\w/.test('\_') // true

\W : 匹配任何非數字字母與底線，等同於[^a-za-z0-9_]。
/\W/.test('A') // false
/\W/.test('\_') // false
/\W/.test(' ') // true

\n : 用於查找換行符, 回換行符被找到的位置, 如果未找到匹配，則返回-1
如果 n 為數字 ????????????
var str = "Visit W3School. \n Learn JavaScript.";
var str1 = "Visit W3School. Learn JavaScript.";
var patt1=/\n/g;
str.search(patt1) // 16
str1.search(patt1) // -1
/\n/.test('\n') // true

\0 : 查找 NUL 字符
/\0/.test('\0') // true

\xhh : 查找以十六進制數 dd 規定的字符。

\uhhhh : 查找以十六進制數 xxxx 規定的 Unicode 字符。
```
