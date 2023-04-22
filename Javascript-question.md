### Memoize

```javascript
function memoize(fn) {
  const cache = {};
  return function (...args) {
    const key = JSON.stringify(args);
    if (cache[key] === undefined) {
      cache[key] = fn(...args);
    }
    return cache[key];
  };
}

var cacheTimes = 0;
var sum = (a, b) => {
  console.log("cacheTimes: ", ++cacheTimes);
  return a + b;
};
var memoizeFn = memoize(sum);
memoizeFn(1, 2); // cacheTimes: 1
memoizeFn(1, 2); // use cache data
memoizeFn(2, 3); // cacheTimes: 2
```

### Tail recursion

```javascript
// solution 1 -> recursion
function factorial(n) {
  if (n === 1 || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(5)); // 120

// solution 2 -> cache version (stack might overflow, use large memorize)
function factorial(n, cache = {}) {
  if (n === 1 || n === 0) {
    return 1;
  } else if (cache[n]) {
    return cache[n];
  } else {
    cache[n] = n * factorial(n - 1, cache);
    return cache[n];
  }
}

console.log(factorial(5)); // 120

// solution 3 -> tail recursion version (return execute value directionly, prevent stack overflow)
function factorial(n, result = 1) {
  if (n === 0) {
    return result;
  } else {
    return factorial(n - 1, result * n);
  }
}

console.log(factorial(5)); // 120
```

### Curry

```javascript
var curry = function (fn) {
  return function curried(...args) {
    // 當 args >= 執行 fn 的參數時 才執行 fn, 代表參數都到齊了
    if (args.length >= fn.length) return fn(...args);
    // 否則將 當前參數 與下一個傳入的參數 concat, 繼續進行 curried 直到參數湊齊
    return function (...args2) {
      return curried(...args.concat(args2));
    };
  };
};

var sum = (a, b, c, d) => a + b + c + d;
var currySum = curry(sum);
console.log(currySum(1)(2)(3)(4)); // 10
console.log(currySum(1, 2)(3, 4)); // 10
console.log(currySum(1)(2, 3, 4)); // 10
console.log(currySum(1)(2, 3)(4)); // 10
```

### Reduce

```javascript
function myReduce(callback, initialValue) {
  let result = initialValue;
  for (let i = 0; i < this.length; i++) {
    result = callback(result, arr[i]);
  }
  return result;
}

Array.prototype.myReduce = myReduce;

var arr = [1, 2, 3, 4, 5];
var callback = (acc, cur) => acc + cur;
arr.myReduce(callback, 5); // 20
```

### Compose

```javascript
// first compose
var compose = function (funcs) {
  return function (...param) {
    if (funcs.length === 0) return (...args) => args; // 即便傳入空陣列, 也會回傳一個可執行的 function
    var len = funcs.length - 1;
    while (len >= 0) {
      param = funcs[len](...param);
      len--;
    }
    return param;
  };
};
var fn = compose(
  (x) => x + 1,
  (x) => 2 * x
);
fn(4); // 9
// or
var compose = (...fns) => {
  return function (...args) {
    // 如果 arg 是固定傳入的 這樣就沒辦法用嵌套的方式把上一個結果當成參數傳下去, 如 second solution
    return fns.reduceRight(
      (acc, fn) => (Array.isArray(acc) ? fn(...acc) : fn(acc)),
      args
    );
  };
};

var result = compose(
  (x) => x * x,
  (x, y) => x + y
)(5, 2);
console.log(result); // 49
```

```javascript
// second compose,
var compose = (...fns) =>
  fns.reduce(
    (acc, fn) =>
      (...args) => {
        return acc(fn(...args));
        // acc 是上一次結果返回值為一個箭頭函式, acc 相當於變成一個 (...args) => double(fn(...args)) 函式給下一層使用
        // 即便 double 有傳入參數但參數不是馬上執行而是執行另一個函式, 所以又進行堆疊需等內部 fn(...args) 執行完成
        // 才能確定 double 的 args 是什麼, 最後變成 (...args) => double(multiply(...args))
        // 又變成 (5,3) => double(multiply(5,3)), stack 後進先出所以先運算 multiply(5, 3)
      },
    (x) => x // x => x 是一個默認的回傳函式, 會在沒有傳入任何函式時被使用, 它接收一個值作為參數，並直接返回這個值。這樣即使沒有傳入任何函式，也會返回一個可執行的函式，避免了程式出錯。
  );

// function compose(...args) {
// 	return args.reduce((acc, fn) => (...params) => {
// 		if (args.length === 0) return params[0];
// 		return acc(fn(...params));
// 	}, initValue => initValue);
// }

var flatten = (arrs) => arrs.reduce((acc, item) => acc.concat(item), []);
var concat = (arrA, arrB) => arrA.concat(arrB);
compose(flatten, concat)([[2], [4]], [[6, 8], 10]); // [2, 4, 6, 8, 10]

var f = (str) => str.toUpperCase();
var g = (str) => str.concat("!a");
compose(g, f)("fp"); // 'FP!a'

var multiply = (a, b) => a * b;
var double = (a) => 2 * a;
compose(double, multiply)(5, 3); // 30
```

### Debounce

```javascript
var debounce = function (fn, t) {
  let timeout;
  return function (...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      fn(...args);
    }, t);
  };
};
```

### Throttle

```javascript
function throttle(fn, delay) {
  let lastCall = 0;
  return function (...args) {
    const now = new Date().getTime();
    if (delay > now - lastCall) return;
    lastCall = now;
    return fn(...args);
  };
}

var sayHi = () => console.log("sayHi");
const throttledSayHi = throttle(sayHi, 3000);
throttledSayHi();
```

### Sleep

```javascript
var sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));
// var sleep = time => new Promise((resolve, reject) => setTimeout(() => resolve(), time));

async function delay() {
  console.log("1");
  await sleep(3000);
  console.log("2");
}

delay();
```

### Symbol

具有 Symbol.iterator 屬性的對象並不一定是迭代器，它只是定義了迭代的接口。
要想創建一個代器，需要一個現實對象的 next()，該方法返回一個 value & done 的對象，
分别表示迭代器的當前值以及是否迭代完所有值。

Symbol 還有很多其他的用途，比如在對象中使用 Symbol 作為屬性名衝突，提高代碼可維護性。
同时，由於 Symbol 是不可變的，因此可以確保每個屬性名都是唯一的，避免了字符串屬性名的一些問題。

```javascript
// judge is iterable
function isIterable(obj) {
  return typeof obj[Symbol.iterator] === "function";
}
```

### Promise (implement Promise.all, Promise.race)

```javascript
// (1) Promise.All
// Promise.resolve is static function in constructor
// New Promise(resolve) , resolve is a call back function
Promise.newAll = (promises) => {
  return new Promise((rs, rj) => {
    var count = 0;
    var result = [];
    var len = promises.length;
    if (len == 0) return promises;

    // traverse promises
    promises.forEach((p, i) => {
      Promise.resolve(p)
        .then((res) => {
          // promise ssuccess executed
          count++;
          result[i] = res;
          // it means all promise executed success
          if (len == count) rs(result);
        })
        .catch(rj);
    });
  });
};

var p1 = Promise.resolve(1);
var p2 = new Promise((resolve, reject) =>
  setTimeout(() => {
    resolve(2);
    // reject(2)
  }, 1000)
);
var p3 = Promise.resolve(3);

var t = Promise.newAll([p1, p2, p3]).then(console.log);

console.log(t);

// (2) Promise.race(iterable)
Promise.newRace = function (promises) {
  var isIterable = (obj) => typeof obj[Symbol.iterator] === "function";
  if (!isIterable(promises)) return;
  return new Promise((re, rj) => {
    for (const p of promises) {
      Promise.resolve(p)
        .then((res) => {
          re(res);
        })
        .catch(rj);
    }
  });
};

var p1 = new Promise((resolve, reject) => setTimeout(resolve, 3000, "p1"));
var p2 = new Promise((resolve, reject) => setTimeout(resolve, 5000, "p2"));

Promise.newRace([p1, p2]).then(console.log);
```

### implement setTimeout

```javascript
function settimeout(handler, ms, val) {
  if (typeof handler !== "function") return;
  function trampoline(f) {
    while (f && f instanceof Function) {
      f = f();
    }
    // return f
  }
  var delay = ms;
  var firstTime = Date.now();
  return new Promise((resolve) => {
    function handle() {
      // 一秒執行 2760w 次
      var t = Date.now();
      if (t - firstTime >= delay) {
        resolve(handler(val));
      } else {
        return handle;
      }
    }
    trampoline(handle);
  });
}
settimeout(console.log, 2000, "11");

// requestAnimationFrame(callback)
function settimeout(handler, ms, val) {
  if (typeof handler !== "function") return;
  // function trampoline(f){
  //   while(f && f instanceof Function){
  //     f = f()
  //   }
  // }
  var delay = ms;
  var firstTime = Date.now();
  return new Promise((resolve) => {
    function handle() {
      // 一秒 16 楨
      var t = Date.now();
      if (t - firstTime >= delay) {
        resolve(handler(val));
      } else {
        requestAnimationFrame(handle);
      }
    }
    requestAnimationFrame(handle);
  });
}

settimeout(console.log, 2000, "11");
```

### async await, yield \* generator

### Bfs

### Dfs

### Apply bind call

### This

```javascript
This 的指向是在函數被調用時確定的 而不是在函數定義時 (哪個對象調用函數, this 就指向誰)

var a = {
    value: 1,
    getVal: () => {
        console.log(this);
        return this.value;
    }
}

var b = {
    value: 2,
    getVal: function() {
        console.log(this);
        return this.value;
    }
}

// console.log(a.getVal()) // this = window, // window.value = undefined
// console.log(b.getVal()) // this = b, // b.value = 2
// var c = a.getVal;
// var d = b.getVal;
// console.log(c()) // this = window, // window.value = undefined
// console.log(d()) // this = window // window.value = undefined
// var d = b.getVal; => 函數丟失了它的上下文，也就是 b 對象，此時 this 不再指向 b，而是指向全局作用域，即 window
// 此時的 d 也註冊在 window.d 上, 當調用函數時自然指向 this.
var e = () => b.getVal(); // this = b, // val = 2,
// e 這邊的 arrow func this 是執行被 "b" 定義時的 getVal, 故 this 指向 b
```

### Arrow function (this 取決於定義時 ctx 最近的 this)

```javascript
指向在定義函數時的上下文環境（lexical context），而不是在執行函數時的上下文環境。
也就是說，箭頭函數的this值是在定義時確定的，而不是在運行時確定的。
一般函數的this值是在函數被調用時確定的，並且取決於函數調用時的上下文。

箭頭函式沒有自己的 this，它的 this 是繼承自包含它的最近的非箭頭函式的 this 值。
因此，在箭頭函式內無法使用 call、apply、bind 等方法來改變 this 的指向。
箭頭函式的 this 是靜態的，指向該箭頭函式所在的作用域的 this，一旦綁定就無法再被更改。
```

### Implement Array map function (Using reduce)

```javascript
Array.prototype.MAP = function (callback, ctx = null) {
  if (typeof callback !== "function")
    throw new Error("callback should be Function!");
  console.log(ctx);
  return this.reduce((acc, cur, i, array) => {
    return acc.concat(callback.call(ctx, cur, i, array));
  }, []);
};

// callback 不使用 this
var callback = (el) => el * 5; // this = window, 利用傳入 ctx 來指定上下文讓 this 修改為其他對象避免抓不到值
var newArr = [1, 2, 3].MAP(callback);
console.log(newArr); // [5,10,15]

// callback 使用 this, 且不綁定 ctx
var callback1 = (el) => el * this.value; // window.value = undefined
var callback2 = function (el) {
  return el * this.value;
}; // window.value = undefined
var newArr = [1, 2, 3].MAP(callback1);
console.log(newArr); // [NaN, NaN, NaN]

// callback 使用 this, 且綁定 ctx, 分別測試 arrow function & normal function
var obj = {
  value: 5,
};
var newArr1 = [1, 2, 3].MAP(callback1, obj); // [NaN, NaN, NaN]
var newArr2 = [1, 2, 3].MAP(callback2, obj); // [5,10,15]
console.log("newArr1: ", newArr1); // [NaN, NaN, NaN] => callback = arrow func => 宣告時已經綁定, 且無法使用 call, apply, bind 修改
console.log("newArr2: ", newArr2); // [5,10,15]
```

### Symbol

### NaN

```javascript
NaN 的全名是 Not-a-Number，是 JavaScript 中一種特殊的數值型別，表示不是一個合法的數字。

NaN 有以下特性：

NaN 是一個數值型別的值，但是它和任何其他值（包括它自己）都不相等，包括 NaN !== NaN。
在任何涉及 NaN 的操作中，結果都是 NaN，比如 1 + NaN、NaN + NaN、Math.sqrt(-1)、parseInt("abc") 等。
NaN 與任何值的比較都返回 false，包括 NaN > 1、NaN < 1、NaN == 1、NaN === 1 等。
因為 NaN 的這些特性，它通常被用來表示一個無效的或者未知的數值，比如在一些數學計算中可能出現錯誤導致結果為 NaN，或者用戶輸入錯誤的數據導致解析失敗也會返回 NaN。因此，在編寫 JavaScript 程序時，需要注意對 NaN 的處理。
```

### Class && super (子類繼承父類的屬性和方法, ex: extend 的子類也需要 name 這個屬性)

### Prototype (構造函式的屬性, 可讓所有 instance 共用函式), **proto** // 能使用繼承來的哪些屬性

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.say = function () {};
}

Person.prototype.go = function () {};

var person1 = new Person("Tom", 20);

console.log(person1.constructor === Person); // true, 構造函式指向本身, constructor 代表由什麼構造函式產生
console.log(person1.__proto__ === Person.prototype); // true, __proto__ 指向構造函式 Person.prototype
console.log(Object.getPrototypeOf(person1) === Person.prototype); // true, 所有構造函式皆隸屬 object,
// 可使用 Object.getPrototypeOf(obj) 獲取其 構造函式的 prototype, 如 Person.prototype

console.log(person1.prototype); // undefined, 宣告的 person1 為 instance, 非一個建構函式 不具備 prototype 屬性
```

## Implicit conversion rules

https://javascript.plainenglish.io/interviewer-can-a-1-a-2-a-3-ever-evaluate-to-true-in-javascript-d2329e693cde

### Compare json

### Xss

### Csrf

### cors Access-Control-Allow-Origin

### Event bubble

### Event loop 詳解 (含 heap 如何儲存 primitive & object type, stack, queue)

### window opener & session storage

```
window.open 的 noreferrer 和 noopener 可以用來避免新開啟的網頁能夠訪問到來源頁面的 window 對象。
但是這兩個選項不會直接影響 sessionStorage 的行為。

當使用 window.open 新開一個頁面時，新開的頁面可以通過 window.opener 訪問到原來頁面的 window 對象。這種訪問行為可以被利用來竊取敏感數據，如在原頁面使用 sessionStorage 存儲用戶登錄信息，然後在新開的頁面中通過 window.opener 訪問到這些信息。

使用 noreferrer 或 noopener 選項可以防止這種訪問行為。
noreferrer 會同時防止新開的頁面訪問 document.referrer 屬性，
noopener 只是防止新開的頁面訪問 window.opener 對象。
!!! 通常建議使用 noopener，因為這樣不會影響 document.referrer 的正常使用。

但是 noreferrer 或 noopener 選項並不能直接影響 sessionStorage 的行為，
sessionStorage 仍然可以在新開的頁面中訪問到，前提是這個頁面和原頁面都在同一個瀏覽器進程中。
(只有透過 window opener 開啟的網頁能訪問到前一 tab 的 sessionStorage, 其餘情況 sessionStorage 不能跨 tab 互通)
如果需要在新開的頁面中避免訪問到原頁面中的 sessionStorage，可以考慮在頁面跳轉時清空 sessionStorage，
或者使用 localStorage 代替 sessionStorage。
```

### AST

### Service worker

### Design Pattern

##### Singleton

##### collaborated code

### Array amortization resize

### Linked list

https://pjchender.dev/dsa/dsa-array-linked-list/
https://ithelp.ithome.com.tw/articles/10217537

### Git

https://backlog.com/git-tutorial/tw/stepup/stepup2_4.html

### SOLID

https://ithelp.ithome.com.tw/articles/10252738?sc=rss.iron
