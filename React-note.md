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
