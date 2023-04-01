# regexp note

```markdown
// regexp
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
https://www.itread01.com/content/1542429006.html

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
