# -*- coding: utf-8 -*

#
# dict.get() => 找得到 key 返回對應 value, 找不到 key 則回傳傳入的第二個參數
#
dic = { 'a': 1 }
dic.get('a', 5)  # 1
dic.get('b', 5)  # 5


# 
# defaultdict() # 可傳入 int, list, dict, 
# 

from collections import defaultdict
cnt = defaultdict(int) # 當key沒有被指定value時，就會採用初始化時預設給進去的東西
cnt[5]
# 0
cnt[5] = 10
cnt[5]
# 10


#
# Counter # 用來計算什麼東西出現幾次
#

from collections import Counter
tl = [1,2,3,4,5,5,5,4]
ct = Counter(tl) # 變成 Counter 物件， 用 tuple 表示 
# Counter({5: 3, 4: 2, 1: 1, 2: 1, 3: 1})
ct.most_common() # most_common()會按由大到小的出現次數來排序 並轉成 list tuple 表示
# [(5, 3), (4, 2), (1, 1), (2, 1), (3, 1)]
ct.most_common(2) # 參數控制取前幾個 tuple
# [(5, 3), (4, 2)]

# P.S. 兩個Counter之間可以做加、減運算
ct1 = Counter([1,2,3,4,5])
ct2 = Counter([4,5])
ct1 - ct2
# Counter({1: 1, 2: 1, 3: 1})
# 也可以用 set 運算式如: &, | 


#
# OrderedDict
#
from collections import OrderedDict

scores = OrderedDict([('James', 80), ('Andy', 70), ('Curry', 100)]) # !!每組要用tuple處理
# OrderedDict([('James', 80), ('Andy', 70), ('Curry', 100)]) # 按進去的順

for k in scores:
	print(k)
# James
# Andy
# Curry


# stack(堆疊) 先進後出 ， 通常使用list即可

# queue(佇列 先進先出 ， 一般會使用deque


#
# deque # 一個雙向的序列，可以從開頭或結尾傳入或取出資料。
#

from collections import deque
s = 'abcde'
deque(s) # 直接將字換成deque
# deque(['a', 'b', 'c', 'd', 'e'])
d = deque(s)
d.popleft() # 從左邊取出
# 'a'
d.popleft()
# 'b'
d.pop() # 從右邊取出
# 'e'
d.append('XDFES')
# d
# deque(['c', 'd', 'XDFES'])
d.appendleft('YES')
# deque(['YES', 'c', 'd', 'XDFES'])



# 
# homework
# 
# 給定兩個字串s跟t，已經知道t的組成，
# 是將s的字母打亂以後進行重組，再隨機加上一個字母。
# 請用前面所學，找出被加上的那個字母。

# resolve 1

from collections import Counter

def findDiff(s, t):
	s = Counter(s)
	t = Counter(t)
	diff = t - s
	return diff.most_common()[0][0]


s = 'apple'
t = 'lzppea'
findDiff(s, t)



# 變數後面加冒號，再加資料型態，可以提示輸入的資料型態。
# 但實質上Python並不會強制檢查是否正確。
# "->" 後面接的則是回傳的資料型態

# resolve 2

def findTheDifference(s, t):
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('a')] -= 1
    for c in t:
        if cnt[ord(c) - ord('a')] == 0: return c
        cnt[ord(c) - ord('a')] += 1

findTheDifference(s = 'apple', t = 'applez')


# resolve 3

def findTheDifference(self, s: str, t: str) -> str:
    from collections import Counter
    cnt_s = Counter(s)
    cnt_t = Counter(t)
    # most_common(1)[0]取到了唯一的一組，再一個[0]取到key的部分
    return (cnt_t - cnt_s).most_common(1)[0][0]









