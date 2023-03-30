# Leetcode Note

- quick guide
  - [Array](#array)
  - [String](#string)
  - [Two Pointers](#two-pointers)
  - [Binary Tree](#binary-tree)
  - [Linked List](#linked-list)
  - [Dynamic Programming](#dynamic-programming)
  - [Others](#others)

## <h1 id="array">Array</h1>

<!-- ## <h1 id="string">String</h1>
## <h1 id="two-pointers">Two Pointers</h1>
## <h1 id="linked-list">Linked List</h1>
## <h1 id="dynamic-programming">Dynamic Programming</h1> -->

## <h1 id="binary-tree">Binary Tree</h1>

<a href="https://leetcode.com/problems/same-tree/description/" target="_blank">
  <font color=#228c22 size=5>100.Same Tree</font>
  <font color=#ffb84d size=5>100.Same Tree</font>
  <font color=#E10000 size=5>100.Same Tree</font>
</a>

###### Category: `binary tree`

[![binary tree](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)](https://leetcode.com/problems/same-tree/description/)

#### Description

>

- Given the roots of two binary trees p and q, write a function to check if they are the same or not.
- Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

#### Thinking

There are 4 cases for comparing two nodes,
(1) null & null => return <font color=#228c22>True</font>
(2) val & null => return <font color=#E10000>Flase</font>
(3) val1 & val1 => <font color=#ffb84d>continue to compare recursively down</font>
(4) val1 & val2 => return <font color=#E10000>Flase</font>
if neither node exists, it means both are the same.
if only one node exists, it means the two nodes are not the same.

#### Solution

```javascript .numberLines
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  if (p === null && q === null) return true;
  if (p === null || q === null) return false;
  if (p.val == q.val)
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
  return false;
};
```

## <h1 id="others">Others</h1>

<a href="#">
  <font color=#ffb84d size=5>Array digit anagrams</font>
</a>

#### Description

- Given an array of integers a, to count the no of pairs i, j , such that a[i] and a[j] are digit anagrams.

#### Examples

```
[25, 35, 872, 228, 53, 278, 872] return 4
```

#### Thinking

(1) Use Map( ) to calculate numeric anagrams of various numbers
(2) Accumulate all integer counts with nCr;

#### Solution

```javascript .numberLines
/**
 * @param {Array} arr
 * @return {number}
 */

var solution = (arr) => {
  let res = 0;
  let hm = new Map();
  for (let i of arr) {
    let sorted = i.toString().split("").sort().join("");
    if (hm.get(sorted)) {
      let count = hm.get(sorted);
      count += 1;
      hm.set(sorted, count);
    } else {
      hm.set(sorted, 1);
    }
  }
  for (let k of hm.values()) {
    let nCr = (k * (k - 1)) / 2;
    res += nCr;
  }
  return res;
};
solution([25, 35, 872, 228, 53, 278, 827]);
```

```javascript .numberLines
// 如果第一個數字能找到 抓左邊的最小值 如果第二個能抓到 抓右邊的最大值
// 有 overlaps 都先拿掉, 之後找 startIndex 決定要從哪邊插入 (抓第一個被 overlap 的左側數值, 抓最後一個 overlap 的右側數值)
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

var mergeInterval = function(val1, val2) {
  // find the maximun and minimun
  return [
    Math.min(val1[0], val2[0]),
    Math.max(val1[1], val2[1]),
  ]
}

var insert = function(intervals, newInterval) {
  // so in first step, we need to find that how many interval array is overlap with the newInterval
  // if we find the overlap elements, we need to remove it, and restart declare the new range with intervals
  let i = 0;
  while(i < intervals.length) {
    const [a, b] = intervals[i];
    const [c, d] = newInterval;
  if (
  (a >= c && a <= d) ||
  (b >= c && b <= d) ||
  (c >= a && c <= b) ||
  (d >= a && d <= b)
  ) {
  // if intervals and newInterval is overlap
  // in this way, we need to modify the original intervals
  newInterval = mergeInterval(intervals[i], newInterval);
  intervals.splice(i, 1);
  } else {
  i++
  }
  }

  intervals.push(newInterval);
  intervals.sort((a, b) => a[0] - b[0]); // it will be sort with ascending
  return intervals;
};

insert([[1,3],[6,9]], [2,5]) // [[1,5],[6,9]]
```

```javascript .numberLines
// solution 1
function countAndSay(n) {
  if (n === 1) return "1";
  const prevEl = countAndSay(n - 1);
  let alphabet = "";
  let count = 0;
  let str = "";
  for (let i = 0; i < prevEl.length; i++) {
    if (!alphabet) alphabet = prevEl[i];
    if (prevEl[i] === alphabet) {
      count += 1;
    } else {
      alphabet = prevEl[i];
      count = 1;
    }
    if (i === prevEl.length - 1 || prevEl[i + 1] !== alphabet) {
      str += String(count) + alphabet;
    }
  }
  return str;
}

countAndSay(10);

// solution 2
// contraints
// 1 <= n <= 30
var countAndSay = function (n) {
  let start = "1";
  for (let i = 1; i < n; i++) {
    start = generateStr(start);
  }

  return start;

  function generateStr(str) {
    let pointer = 0;
    let result = "";
    for (let ind = 1; ind <= str.length; ind++) {
      if (str[pointer] !== str[ind]) {
        let len = ind - pointer;
        result = result + len + str[pointer];
        pointer = ind;
      }
    }
    return result;
  }
};
```
