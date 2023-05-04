### Hoist with var & let

```javascript
function hoistWithVarLet() {
  if (true) {
    // console.log(V) // V = undefined, var hoisted, got var V = undefined (only hoist variable, will not hoist value);
    // console.log(v) // referencError, can't access 'v' before initialization
    var V = 1;
    let v = 2;
  }
  console.log(V); // V = 1,                      var is 'function scope'
  console.log(v); // referencError(not defined), let is 'block    scope', in this case only can use it in "if" block.
}

hoistWithVarLet();
```

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
// solution1
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

// solution2 (more strict, consideration with not given initial value & arrow function)
Array.prototype.reduce2 = function (callback, init, ctx) {
  if (typeof callback !== "function") throw "callback should be function!";
  var initVal = typeof init == "undefined" ? this[0] : init;
  var startI = init ? 0 : 1;
  for (let i = startI; i < this.length; i++) {
    initVal = callback.call(ctx, initVal, this[i]);
  }
  return initVal;
};

var arr = [1, 2, 3];
arr.reduce2((acc, cur) => acc + cur);

var arr = [3, 4, 5];
var magnification = {
  value: 5,
};
var callback = function (acc, cur) {
  console.log(acc, cur);
  return acc + cur * this.value;
};

arr.reduce2(callback, 0, magnification);
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

### Debounce (距離上次執行經過 x 秒才能執行一次, 執行時間會根據冷卻期間是否重複執行而刷新冷卻時長)

```javascript
var debounce = function (fn, t) {
  let timeout;
  let isFirst = true;
  return function (...args) {
    if (isFirst) {
      fn(...args);
      isFirst = false;
    } else {
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        fn(...args);
      }, t);
    }
  };
};

var a = debounce(console.log, 1000);
a(1); //
```

### Throttle (每 x 秒最多執行一次)

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

```javascript
注意 bind 綁定 this 後, 即便再用 bind 也無法再次更換 this, bind() 屬於 hard binding
```

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

限制：
1. 沒有自己的 this 值，箭頭函數的 this 是在它被定義的時候綁定的，而不是在它被呼叫的時候綁定。
2. 無法使用 arguments 變數，取而代之的是使用剩餘參數 (...)。
3. 不能用作構造函數，因為沒有自己的 this。
4. 不能使用 yield 關鍵字，因為箭頭函數不是生成器函數。
5. 無法使用 call、apply、bind 方法來改變 this 指向。
6. 箭頭函數內部的 arguments 對象是指向外部作用域中的 arguments 對象，而不是箭頭函數本身的 arguments 對象。
7. 無法使用 new 關鍵字來創建實例。

e.g. (參考上面 arguments 限制)
// 1
var a = (...args) => console.log(args)
a(1,2,3) // [1,2,3]
// 2
function a() { console.log(arguments) }
a(1,2,3) // Arguments[1,2,3.....]
// 3
var a = () => console.log(arguments);
a(1,2,3) // arguments not defined
// 4
function b() {
    var a = () => console.log(arguments);
    a(); // Arguments[1,2,3.....], 指向外部 b 的 arguments 對象
}
b(1,2,3);

var profile = {
    firstName: '',
    lastName: '',
    setName: function(name) {
      console.log(this) // this = profile
      let splitName = function(n) {
          console.log(this) // window; 在 splitName 函數中，this 的值是由函數的調用方式所決定的，而不是由它在哪裡聲明的決定的。
          // 當 splitName 函數在 setName 函數中被調用時，它是作為簡單的函數調用被調用的，因此 this 的值被設置為全局對象，也就是 window。
          // 如果你想讓 splitName 函數中的 this 指向 profile 對象，可以使用 bind、call 或 apply 方法來顯式地指定 this 的值。
          let nameArray = n.split(' ');
          this.firstName = nameArray[0];
          this.lastName = nameArray[1];
      } // .bind(this), 將 splitName this 由 window 指向與 setName 相同的 profile 即可
      splitName(name);
    },
    // setName: function(name) {
    //     let splitName = (n) => {
    //         console.log(this) // this = profile, 找上文最近 this, 上文 this = 一般 fn,
    //         // this 以呼叫對象是誰做為 this 代表
    //         let nameArray = n.split(' ');
    //         this.firstName = nameArray[0];
    //         this.lastName = nameArray[1];
    //     }
    //     splitName(name);
    // },
    // setName: (name) => {
    //     let splitName = (n) => {
    //         console.log(this) // this = window, 找上文最近 this, 上文又是 arrow fn, 繼續往上, 找到 window
    //         let nameArray = n.split(' ');
    //         this.firstName = nameArray[0];
    //         this.lastName = nameArray[1];
    //     }
    //     splitName(name);
    // }
}

profile.setName('John Doe');
console.log(profile.firstName);
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

設計 callback 且 callback 中使用到 this 時
(1) callback = arrow function, 如果直接註冊在外部會綁定 window, 如果想使用某個對象的值盡量在其 ctx 內宣告
(2) callback = normal function, 以此設計會比較簡單, 隨時可以使用 call, apply, bind 綁定 this.
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

### Class and super() (子類繼承父類的屬性和方法, ex: extend 的子類也需要 name 這個屬性)

在 JavaScript 的 class 中，super() 是一個關鍵字，它的作用是調用父類別的建構子，也可以在子類別的方法中調用父類別的同名方法。

當子類別的建構子函數中沒有使用 super() 呼叫父類別的建構子，那麼就無法獲得父類別中定義的實例屬性和方法，也無法透過 this 存取到父類別中的屬性和方法。如果在子類別的建構子中使用了 this 來定義一些實例屬性或方法，那麼這些屬性和方法就只能在子類別中被使用，無法在父類別中被訪問或使用。

在呼叫 super() 的時候，可以傳遞任意參數到父類別的建構子中，這些參數將會作為父類別建構子的引數。如果子類別中沒有定義建構子，那麼 JavaScript 引擎會自動生成一個空的建構子，相當於 constructor() {}，這時在子類別中也可以直接使用 super() 調用父類別的建構子。

需要注意的是，super() 必須在使用 this 之前被呼叫，否則就會報錯。在 ES6 中，繼承是使用 class 和 extends 來實現的，使用 super() 來呼叫父類別的建構子可以繼承父類別中的屬性和方法，使得子類別可以擁有父類別的所有特性。

```javascript
// case 1 以 arrow fn 宣告 showA & showB 差別
class A {
  constructor() {
    this.value = 100;
    console.log(this);
  }
  showA() {
    // 定義在 prototype 上, this 指向 A classes, 若今天想要被繼承用此方法
    console.log(this);
  }
  showB = () => {
    // 相當於 property showB = undefined, 在被賦值變成 arrow function
    // 定義在被創建出來的實例上, 如果不是想被繼承且想讓外部某個變數 = new A().showB 則不用再次綁定 this, 同時不會被覆蓋, 各有不同優點
    console.log(this);
  };
}

// function B() { 建構函式的 this.show 也是綁在實例上 要繼承一樣要綁在 如上面 showB = () => {}
//     this.show = function() {}
// }

class B extends A {
  constructor(value) {
    super(value);
    super.showA(); // (O) // 定義在 prototype 上 可繼承
    // super.showB(); // (X) // 定義在實例上, 效果跟 showA 相同但僅 實例 自己使用, 不能調用父層的 showB
  }
}

var a = new A(); // A {value: 100, showB: ƒ} 但一樣可以使用 showA
var b = new B(); // B {value: 100, showB: ƒ} 但一樣可以使用 showA

// case 2, 將 prototype showA 綁定到 property 上
class A {
  constructor() {
    this.value = 100;
    this.showA = this.showA.bind(this); // 與 case 1 些微不同, 確認 bind(this) 會不會造成 this 綁死在 A 上
    // !!! 將 prototype 註冊到 property 上, 可以避免外部某變數套用其方法時 this 失去上下文導致 this 變成 undefined,
    // 也能夠作為 子class中 直接 super 後用 this.showA 調用, 而不用 super.showA()調用; // Q: 這樣 this 會不會綁死在Ａ上 (不會, this 會依照實例做綁定)
    // 如 var a = new A(); var c = a.showA; 執行 c() 時 this 就不會 undefined
  }
  showA() {
    console.log(this);
  }
}

class B extends A {
  constructor() {
    super();
    this.value = 200;
    this.showA();
    super.showA(); // 與上面 this.showA() 功能相同
  }
}

var a = new A(); // A {value: 100, showA: ƒ}
var b = new B(); // B {value: 200, showA: ƒ}

// case 3 為什麼一樣採用 prototype, 但 class showA (this = undefined), 而建構函式 showA (this 指向 window),
!!!! conclusion: 定義方式不同 下面例子中(指普通函式不討論 arrow fn), class showA 定義方法為 "實例方法", function B showA 為 "原型方法"
!!!!             class 和 建構函式 一樣都是 function, 但 class 並不會註冊到 window 上("局部變數"), 而 function 會 ("全局變數"),
!!!!             所以 class showA 的 this 抓全局抓不到 window 所以 this == undefined, function 則可以抓到 this = window

// 在 class A 中，showA 方法是作為該類的實例方法定義的，當它被單獨引用時，this 指向 undefined。這是因為單獨引用時，方法與類的實例沒有關聯。
// 而在 function B 的原型中定義 showA 方法，當它被單獨引用時，this 指向 window。這是因為 showA 方法是在 B.prototype 上定義的，當被單獨引用時，this 會指向全局對象 window。
// 簡而言之，this 的指向取決於函數是如何被調用的。當函數作為對象的方法調用時，this 指向該對象；當函數作為獨立的函數調用時，this 指向全局對象（在瀏覽器中是 window）。
class A {
  constructor() {
    this.value = 100;
    // this.showA = this.showA.bind(this); // 一樣可以綁定 this 解決, 但主要是判別 this = undefined || window 的差別
  }
  showA() { // showA 作為該類的 "實例方法" 定義，當它被單獨引用時，this 指向 undefined。 這是因為單獨引用時，方法與 class 的實例沒有關聯。
    console.log(this);
  }
}

function B() {
  // this.showA = function () {
  //   console.log(this);
  // };
}
B.prototype.showA = function() { // showA 作為原型中定義 showA 方法 ("稱原型方法")，當它被單獨引用時，this 指向 window。
  console.log(this);
}

var a = new A();
var b = new B();

var c = a.showA;
console.log("c(): ", c()); // this = undefined

var e = b.showA;
console.log("e(): ", e()); // this = window
```

### Diff between declare func in constructor func with using this.fn & return { fn }

```javascript
function A() {
  this.value = 100;
  this.show = function () {
    // 這邊跟使用 arrow func 容易搞混 不管這邊是不是 arrow function 只要不是在 return 內註冊就都能訪問其他 properties
    // this = A {show: ƒ}, when create object 'this' will point to the "A instance" that can use all properties in A, this.value = 100
    console.log(this);
    console.log(this.value);
  };
  return {
    show: function () {
      // register in global variables, 'this' point to the window, can't access all perperties in A
      console.log(this);
      console.log(this.value);
    },
  };
}

var a = new A();
a.show();
```

### Implicit conversion rules

https://javascript.plainenglish.io/interviewer-can-a-1-a-2-a-3-ever-evaluate-to-true-in-javascript-d2329e693cde

### Garbage collection & Memory leak

JavaScript 的垃圾回收機制主要是基於自動內存管理的概念。
JavaScript 引擎會跟踪內存中的所有對象，當一個對像不再被引用時，即它的引用計數為 0 時，這個對象就會被認為是垃圾。
JavaScript 引擎會自動回收這部分內存，以便給其他對像或變量使用。這個過程被稱為垃圾回收。

內存佔用過高可能會導致應用程序出現各種問題，比如緩慢或卡頓，甚至可能導致崩潰。
當內存中的對象佔用的內存過多時，垃圾回收機制會嘗試回收這些內存。
在 JavaScript 中，當一個對像不再被引用時，它佔用的內存就可以被回收。

然而，如果程序中存在無法訪問的對象（即沒有被引用到但佔用著內存），垃圾回收機制就無法回收這部分內存，從而導致內存洩漏（memory leak）。
內存洩漏通常會導致應用程序的內存佔用越來越高，最終可能會導致程序崩潰。

內存洩漏的原因可能有多種，比如：

被遺忘的定時器或回調函數。
意外創建了全局變量。
持續向數組或對像中添加元素，導致數組或對像不斷增大，佔用越來越多的內存。
持續創建新的對像或實例，但沒有及時釋放它們佔用的內存。

避免 memory leak

- 避免在全局作用域聲明變數和函數，這樣容易導致變數無法被回收
- 盡量減少使用匿名函數，因為這樣的函數會產生額外的作用域
- 盡量避免對 DOM 進行直接操作，因為 DOM 元素通常是很占用記憶體的
- 盡量避免產生循環引用，例如將一個對象設為自己的屬性值
- 及時釋放不需要的對象和變量 (ex: 數組和對象)。
- 使用閉包和模塊化編程來避免創建不必要的全局變量。 (如果使用閉包但在內部直接使用變數名稱不透過 var let const 宣告 會在全域註冊一個全域變數, 也可能導致 memory leak)
- 盡可能複用已有的對像或實例，避免頻繁創建新的對像或實例。

p.s. 若移除註冊 addEventListener 的 dom 元素被移除 註冊事件會一起被移除且回收

### Xss

指攻擊者通過注入惡意腳本代碼，使之在受害者的瀏覽器上執行。攻擊者可以在網頁上顯示自己的內容，或者竊取受害者的敏感資訊，如 Cookie 等。XSS 攻擊常見的方式是在網站表單、留言板等地方輸入 JavaScript 代碼，攻擊者的代碼隨後被存儲在網站的資料庫中，當其他使用者訪問該網站時，攻擊者的代碼就會在使用者的瀏覽器上執行。

https://medium.com/hannah-lin/%E5%B9%BC%E5%B9%BC%E7%8F%AD%E4%B9%9F%E8%83%BD%E6%87%82%E7%9A%84-owasp-top-10-692764c51f61#dd52
https://medium.com/hannah-lin/%E5%BE%9E%E6%94%BB%E6%93%8A%E8%87%AA%E5%B7%B1%E7%B6%B2%E7%AB%99%E5%AD%B8-xss-cross-site-scripting-%E5%8E%9F%E7%90%86%E7%AF%87-fec3d1864e42

處理方法：

Frontend:
(1) 輸入驗證：對用戶輸入的數據進行驗證，過濾掉不合法的輸入，例如特殊符號等。

(2) 輸出轉義：可使用 encodeURI，在顯示用戶輸入的數據時，對敏感字符（如 <, >, ", ', &）進行轉義，例如將 < 轉為 &lt;，> 轉為 &gt;，" 轉為 &quot;。

(3) 在 React 和 Vue 等前端框架中，可以使用相應的內置函數來實現輸出轉義。在 React 中，可以使用 dangerouslySetInnerHTML 屬性來插入原始 HTML，但是應該儘量避免使用它，而是使用 React 提供的 createElement 或 JSX 語法生成元素，因為它們會自動進行 HTML 轉義。在 Vue 中，可以使用 v-html 指令來插入原始 HTML，但同樣應該儘量避免使用它，而是使用 {{ }} 語法或 v-text 指令來顯示文本。

Backend:
(1) HttpOnly Cookie：在服務端設置 HttpOnly 屬性，使得 Cookie 無法通過 JavaScript 訪問，防止攻擊者竊取用戶的 Cookie。
(2) Content Security Policy（CSP）：在 HTTP Header 中添加 CSP，限制網頁載入的資源，限制腳本的執行。
(3) 使用 HTTPS：使用 HTTPS 協議加密數據傳輸，從而防止數據被攔截和竊取。

實際範例：

### Csrf (偽造身份發送請求)

在不同的 domain 底下卻能夠偽造出「使用者本人發出的 request」。
因為瀏覽器的機制，你只要發送 request 給某個網域，就會把關聯的 cookie 一起帶上去。
如果使用者是登入狀態，那這個 request 就理所當然包含了他的資訊（例如說 session id），這 request 看起來就像是使用者本人發出的。

指攻擊者通過偽造請求，使受害者在不知情的情況下執行一些操作，如修改密碼、刪除資訊等。
攻擊者通常會通過社交等手段引誘受害者點擊連結或打開惡意網站，進而實現 CSRF 攻擊。
舉例來說，攻擊者可以在自己的網站上放置一個圖片標籤，圖片 URL 指向受害者要攻擊的網站，並且在圖片 URL 中携帶了修改密碼的請求。
當受害者訪問攻擊者的網站時，攻擊者的請求就會被發送到受害者的網站上，進而修改受害者的密碼。

處理方法：

(1) 在 HTTP 標頭中加入 token：當用戶訪問網站時，可以生成一個隨機的 token，並在後端和前端都保存這個 token。當用戶提交表單時，將 token 作為表單數據的一部分一同提交到後端。後端可以檢查表單中的 token 是否與保存在後端的 token 相同。如果不同，則證明這是一個 CSRF 攻擊。

backend:
(1) 驗證請求來源：可以在後端檢查 HTTP Referer 標頭，檢查請求來源是否為正確的網域。然而，這種方式容易受到偽造 Referer 的攻擊，因此不是非常可靠。

(2) 使用同源策略：由於 CSRF 攻擊利用的是網站的 cookie，如果網站不允許跨域訪問，那麼攻擊者就無法通過跨域請求來利用網站的 cookie。因此，使用同源策略可以有效避免 CSRF 攻擊。

### cors Access-Control-Allow-Origin

### Event bubble

### Event loop 詳解 (含 heap 如何儲存 primitive & object type, stack, queue)

### Service worker

(3) Service Worker 是一個瀏覽器 API，用於在 Web 應用程序和瀏覽器之間建立一個獨立的代理層。
它可以在瀏覽器和網絡之間建立一個中間層，可以緩存應用程序所需的資源，並在網絡不可用時提供離線體驗。
Service Worker 可以讓 Web 應用程序實現像原生應用程序一樣的離線瀏覽體驗，可以提高應用程序的性能和可用性。

https://ithelp.ithome.com.tw/articles/10187529

### Vue & React API, compare, diff

| 項目 |      Vue       |                          React                           |                        Replenish                        |
| :--: | :------------: | :------------------------------------------------------: | :-----------------------------------------------------: |
|      | ref, reactive  |                          useRef                          |
|      |    computed    |                   useMemo, useCallback                   |
|      |    mounted     |                    componentDidMount                     |                   組件掛載後立即調用                    |
|      |    updated     |                    componentDidUpdate                    |                在 Vue 組件更新後立即調用                |
|      |   unmounted    |                   componentWillUnmount                   |
|      | no mapping api | React.memo, shouldComponentUpdate(nextProps, nextStates) | React.memo 是 shallow compare, 如果傳物件一樣會觸發渲染 |
|      |                |                                                          |
|      |                |                                                          |

補充：

- React & Vue 都使用 Virtual DOM(以下縮寫為 V-DOM) 以及 diff 算法,
  但有稍微不同：
  Vue 的 V-DOM 是透過 Template Compiler, 即生成的 V-DOM 是由 Template Compiler 產生, (即 V-DOM 包含編譯後的模板)
  因為 Template Compiler 通常會連帶生成一些靜態節點 (static nodes, 可理解為 Template Compiler 將一些 靜態文本 或 不受外部影響的狀態樣式視為靜態節點)
  這些節點更新時不需要透過 diff 比較, 相對來說是一種優化 V-DOM 的手段.

React 則是拿原始資料生成 V-DOM, diff 比較上也是直接拿原始資料做比較,所以兩者在緩存和實作上就會略有不同

- Vue lifecycle  
  beforeCreate：在 Vue 實例 創建之 前 觸發，此時還未初始化 data 和 methods。
  created：在 Vue 實例創建完成 後 觸發，此時已經初始化了 data 和 methods。 // (Vue3 的 setup 相當於 beforeCreate + created 的融合)
  beforeMount：在 Vue 實例掛載到 DOM 之前觸發，此時模板已編譯完成，但尚未渲染到 DOM 中。
  mounted：在 Vue 實例掛載到 DOM 之後觸發，此時模板已編譯完成且已渲染到 DOM 中。

##### useMemo (like computed) 主要用在當元件重新渲染時，減少在元件中複雜的程式重複執行。

```jsx
// useMemo 會在渲染時計算一個 memoized 值，只有當其中一個依賴值有所更改
// 才會重新計算 memoized 值，避免不必要的重複計算。
// 一般適用於計算成本較高的值或有較多計算運算的值。
import React, { useMemo } from "react";

function MyComponent({ a, b }) {
  const memoizedValue = useMemo(() => {
    // 計算成本較高的值或有較多計算運算的值
    return a * b;
  }, [a, b]);

  return <div>{memoizedValue}</div>;
}
```

##### useCallback

```jsx
// useCallback 與 useMemo 相似，只有當其中一個依賴值有所更改時才會重新計算 callback，避免不必要的重複計算。
// 一般適用於 callback function 較複雜或傳入的 props 較多的情況。

- useCallback 可與 React.memo 一起使用， memo 用來偵測 props 有沒有修改 (use shallow compare 傳入 prop = object 時必渲染)，減少不必要渲染；
  useCallback 則讓 props 的 Object 能夠在父元件重新渲染時，不重新分配記憶體位址，讓 memo 不會因為重新分配記憶體位址造成渲染。

import React, { useCallback } from "react";

function MyComponent({ onClick }) {
  const handleClick = useCallback(() => {
    // 如放入複雜的 callback function
    onClick("some data");
  }, [onClick]);

  return <button onClick={handleClick}>Click me</button>;
}
```

##### useRef

```jsx
// useRef 會返回一個可變的 ref 物件，可用於保存任何可以改變的值，並且在重新渲染時保持該值的穩定。

import React, { useRef } from "react";

function MyComponent() {
  const inputRef = useRef(null);

  function handleButtonClick() {
    inputRef.current.focus();
  }

  return (
    <div>
      <input type="text" ref={inputRef} />
      <button onClick={handleButtonClick}>Focus input</button>
    </div>
  );
}
```

immetable.js 是 Facebook 开发的一个 js 库，可以提高对象的比较性能，像之前所说的 pureComponent 只能对对象进行浅比较，,对于对象的数据类型,却束手无策,所以我们可以用 immetable.js 配合
shouldComponentUpdate 或者 react.memo 来使用。immutable 中 我们用 react-redux 来简单举一个例子，如下所示 数据都已经被 immetable.js 处理。

<!-- React.memo 是用 shallowly compare 的方法確認 props 的值是否一樣， shallowly compare 在 props 是 Number 或 String 比較的是數值，當 props 是 Object 時，比較的是記憶體位置 (reference)。

因此，當父元件重新渲染時，在父元件宣告的 Object 都會被重新分配記憶體位址，所以想要利用 React.memo 防止重新渲染就會失效。

React.memo(Component, (prevProps, nextProps) => { // compare values as you want }); -->

##### vue3 proxy

```javascript
var an = {
  age: 28,
};

var pAn = new Proxy(an, {
  get(target, key, receiver) {
    return Reflect.get(...arguments); // = return target[key];
  },
  set(target, key, value) {
    return Reflect.set(target, key, value); // return true
  },
});

pAn.age = 29;
```

// receiver: 通常是 proxy 對象本身或者是它的原型對象, 在 get 攔截器中, 如果 receiver 參數被傳入，則可使用 receiver 來修改屬性讀取操作的上下文。
可以把調用對象當作 target 參數，而不是原始 Proxy 構造的對象。

##### vue2 object.defineProperty

##### react reconciliation

syntax: template, jsx
data flow: 2 way, 1way(父->子)
reactive: Dependency Tracking, vnode

Vue 將虛擬 DOM 的概念與模板語法相結合，可以更直觀地進行模板開發。
Vue 的模板語法在模板編譯成虛擬 DOM 之前，就已經將數據和模板進行了綁定，
當數據發生變化時，Vue 會通過虛擬 DOM 來計算出需要更新的節點，再將這些節點進行更新。
因此，Vue 也是一個基於虛擬 DOM 實現的響應式框架，但是它的響應式系統與 React 不同，Vue 使用了一個叫做“依賴追踪”的技術，
通過收集組件的依賴關係，在數據變化時直接通知組件進行重新渲染，從而實現響應式更新。

React reconciliation 是 React 的一個核心算法，用於比對 Virtual DOM 中的新舊節點，決定哪些部分需要更新並且如何更新。當 React 組件的狀態或屬性發生改變時，React 會根據新的狀態和屬性計算出新的 Virtual DOM 樹，並通過與上一次渲染的 Virtual DOM 樹進行比較，找出需要更新的節點，然後進行最小化的更新操作，最終反映到實際的 DOM 上。

Vue 和 React 都使用 diff 算法來比對 Virtual DOM，找出需要更新的節點，但是兩者的實現方式略有不同。
Vue 在 diff 時會對比新舊 VNode 的 tag 和 key 屬性，而 React 則是比較 VNode 的 type 屬性以及 key 屬性。
此外，Vue 還有一個優化手段叫做“靜態提升”，可以將一些不會變化的節點在 diff 過程中排除，以進一步提升性能。

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

https://juejin.cn/post/6844903960650711054
https://github.com/babel/babel/tree/master/packages/babel-core/src
https://www.babeljs.cn/docs/babel-core

### Service worker

Service Worker 是一種 JavaScript Worker 的，""獨立運行在主瀏覽器進程外""，負責處理 Web 應用的網絡請求和緩存資源。

Service Worker 可以在 Web 應用的生命週期中被註冊、安裝和啟用，當 Service Worker 成功安裝並啟用後，就會開始攔截網絡請求，
並且可以透過緩存來加快網頁的加載速度，甚至可以離線使用 Web 應用。Service Worker 的另一個優點是它可以在後台執行，即使使用者關閉了網頁，也能夠持續運行。

以下是 Service Worker 的一些主要作用：

- 網路請求攔截：Service Worker 可以攔截網頁中的網路請求，並對這些請求進行處理。例如，Service Worker 可以根據請求的網址、網址參數或者請求方法來判斷是否要從緩存中獲取資源，或者重新向網絡發送請求獲取最新資源。

- 資源緩存：Service Worker 可以將網頁中常用的資源（例如 HTML、CSS、JavaScript 和圖像等）緩存到本地，這樣就可以加快網頁的加載速度。在使用 Service Worker 的情況下，即使網絡斷開，用戶也可以通過緩存資源繼續使用 Web 應用。

- 背景同步：Service Worker 可以在後台執行，並且可以與網頁進程通信，從而實現後台同步資料、更新緩存等功能。例如，當用戶處於離線狀態時，Service Worker 可以在網絡恢復連接後同步用戶資料。

- 推送通知：Service Worker 可以與推送通知 API 搭配使用，實現 Web 應用的推送通知功能。當用戶訂閱了推送通知後，Service Worker 就可以接收到推送通知，並在用戶關閉網頁或者離線的情況下向用戶發送通知。

當使用者關閉網頁後，網頁中的 JavaScript 代碼通常會停止運行。但是 Service Worker 可以在後台持續運行，這意味著即使使用者關閉了網頁，Service Worker 仍然可以持續運行。這樣可以讓 Service Worker 執行一些非常有用的任務，例如在後台更新快取，處理推送通知等。這對於提高網站的性能和可靠性非常有幫助。

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

### Effect

```javascript
// effect with typing each skill
var arr = ["Javascript", "React", "Python"].map((el) => el + "   "); // 在每個字串後面多加三個空白 等於讓整個單字有延遲效果
for (let i = 0; i < arr.length; i++) {
  let curStr = arr[i];
  let VocabularyTime = 2600;
  setTimeout(() => {
    // 每個字串 2 秒
    if (curStr) {
      let temp = [];
      let isMinus = false;
      for (let j = 0; j < curStr.length; j++) {
        let delayTime = (VocabularyTime / (curStr.length * 2)) * (j + 1);
        let basicDelay = VocabularyTime / 2;
        setTimeout(() => {
          temp.push(curStr[j]);
          console.log(temp.join(""));
        }, delayTime); // 字串越長顯示越快, *2 原因是要把 minus 時間也算進去
        setTimeout(() => {
          temp.pop();
          console.log(temp.join(""));
        }, basicDelay + delayTime); // VocabularyTime / 2 = delay time， 要在所有字串加完才顯示
      }
    }
  }, VocabularyTime * i);
}

// 創造 wave, createWave(3, 100) 會創造三波 wave, wave 高會達到 [3,6,9] 並隨之遞減,並以 100ms 輸出一次當前 wave
function createWave(wave, ms) {
  var arr = [];
  for (let i = 0; i < wave; i++) {
    let height = wave * (i + 1); // [3, 6, 9]
    setTimeout(() => {
      for (let j = 0; j < height; j++) {
        // [3, 6, 9]
        let totalTime = height * 2 * ms; // * 2 是把 pop 時間也算進去
        let delayTime = ms * (j + 1);
        let basicDelay = totalTime / 2;
        setTimeout(() => {
          arr.push("1");
          console.log(arr.join(""));
        }, delayTime);
        setTimeout(() => {
          arr.pop();
          console.log(arr.join(""));
        }, basicDelay + delayTime);
      }
    }, height * ms * i);
  }
}

createWave(3, 100);
```
