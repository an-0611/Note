### Life cycle

[diagram](https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/)

##### Mounting phase (component first building)

1. constructer()
2. render() render 後才可使用 dom
3. React 處理畫面到 DOM // dom mounted (ex: 元件被添加到 DOM )
4. componentDidMount() 大致等於 DOMContentLoaded = jquery document.ready

##### Updating phase (component updating)

當使用了 setState、或者 props 更新時

1. shouldComponentUpdate() (return true = execute, return false = no execute and break out function)
2. render()
3. React 處理畫面到 DOM
4. componentDidUpdate(prevProps, prevState)

p.s.: this.setState({ xxx: 123 }, callback); callback can ensure to get latest state value.

##### Unmounting phase (component destroying)

1. componentWillUnmount()
2. render()
3. React 處理畫面到 DOM

### Hook

##### useState (宣告 state 以及更改 state 的方法)

```javascript
import React, { useState } from "react";

function Example() {
  // 宣告一個新的 state 變數，我們稱作為「count」。
  const [count, setCount] = useState(0);
  //     state, updateStateFunc    initValue
  // state 變更後重新 render 元件
  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  );
}
```

##### useEffect

- 在元件 render 後被呼叫執行
- 使用場景： 用於處理異步數據獲取、訂閱管理、手動 DOM 操作等

```javascript
useEffect(
  () => {
    // 在此執行 side effect 操作
    console.log("Component rendered"); // 在每次元件 render 後執行
    const subscription = props.source.subscribe();

    // 如需要清除副作用, 可返回一個清理函式
    return () => {
      // 將在元件銷毀時執行 // !! 依賴數組發生變化時也將執行
      console.log("Component will unmount");
      subscription.unsubscribe();
    };
  },
  [props.source] // 第二個參數為依賴數組，當依賴數組的值發生變化，副作用會被重新執行, 即第一個參數內容
);
```

##### useContext

- 利用 Context API 來解決 Props drilling (ex: 中間元件可能並不需要 prop, 只有最內層元件會使用到)
- 用於存取上下文的 Hook, 可將父層資料給任意樹中的子層
- 使用場景： 用於全域配置、主題、認證狀態(登入等)、共享數據等

```javascript
// (1) 建立 context 物件
const MyContext = React.createContext();

// (2) 利用 context 物件建立 Provider, 並將資料傳入 Provider 提供上文數據, 利用 children 創造下文數據
// p.s. 通常，MyProvider 包裹在應用程式中最頂層，
function MyProvider({ children }) {
  const text = "hello world";
  return <MyContext.Provider value={text}>{children}</MyContext.Provider>;
}
```

```javascript
import React, { useContext } from "react";

// (3) 使用 useContext 存取上下文中的共用資料。
//     在任何需要存取共用資料的元件內部，只需使用 useContext(MyContext) 來取得上下文的值。
function MyComponent() {
  const text = useContext(MyContext);
  return <div>{text}</div>;
}
```

##### useReducer

- 使用場景： 表單驗證、購物車操作等 (可能涉及多個 reducer 的操作都可使用)

```javascript
import React, { useReducer } from "react";

// (1) 定義 reducer 函數，接受當前狀態 state 和 action.type 更新狀態
// ，並返回新狀態更新 state
const reducer = (state, action) => {
  switch (action.type) {
    case "INCREMENT":
      return { count: state.count + 1 };
    case "DECREMENT":
      return { count: state.count - 1 };
    default:
      return state;
  }
};

function Counter() {
  // 使用 useReducerHook 創建一個 state 和 dispatch 函數 (派發 action 已觸發狀態更新)
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  // useReducer(reducer function, initState)
  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: "INCREMENT" })}>增加</button>
      {/* dispatch({ type: 'INCREMENT' }) 呼叫 reducer 並根據其 action.type 更新狀態 */}
      <button onClick={() => dispatch({ type: "DECREMENT" })}>減少</button>
    </div>
  );
}

export default Counter;
```

##### useCallback

- ※ 記憶父元件記憶體位置，避免在重新渲染時被重新分配。
- 用於優化性能，特別是在處理函數回調時。
- 當需要將回調函數傳遞給子組件，並希望這些回調在父組件重新渲染時不會觸發子組件的不必要重新渲染。
- 使用場景： 如點擊按鈕時 count + 1, 若 count 不變則不觸發該 callback

```javascript
import { useState, useCallback } from "react";
const [count, setCount] = useState(0);

// 使用 useCallback 來優化函數
const handleClick = useCallback(() => {
  setCount(count + 1); // callback
}, [count]); // 依賴陣列改變才觸發 useCallback
```

##### useMemo

- ※ 元件重新渲染時，能避免複雜的程式被重複執行
- 優化計算結果, 特別是計算一些昂貴計算邏輯
- 類似 vue computed

```javascript
import { useState, useMemo } from "react";
const [count, setCount] = useState(0);

const expensiveCalculation = useMemo(() => {
  console.log("進行昂貴的計算...");
  // 這裡可以是一些昂貴的計算邏輯
  return count * 2;
}, [count]); // 依賴陣列改變才觸發 useMemo
```
