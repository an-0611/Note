# -*- coding: utf-8 -*

# 
# try...except
# 

# case1
from random import randrange
randrange(1, 101)

min = 1
max = 100
answer = randrange(1, 101)
mode = 0

while mode != answer:
	try:
		mode = int(input('請輸入終極密碼: ' + str(min) + ' 到 ' + str(max) + ' [請輸入數字]: '))
	except:
		# 第一次進來會直接執行 可以用來當 default remind
		# 如果沒輸入錯誤，except的部分就會被忽略
		print('請輸入數字ㄛ')
		continue
	if mode > max or mode < min:
		print('超過範圍，請重新選擇')
		continue
	if mode > answer:
		max = mode - 1
	else:
		min = mode + 1
else:
	print('恭喜，密碼是: ' + str(mode))

# case2
try:
	# raise Exception('讚讚')
	list(dsa)
except Exception as exc:
	# Exception 用於常規異常，所有異常判斷 https://www.runoob.com/python/python-exceptions.html
	print(exc)
except ValueError as exc:
	print(exc)

#
# 三元運算子 ( condition_is_true if condition else condition_is_false )
#

boo = range(0)
True if boo else False
# False

boo = range(1)
True if boo else False
# True



# 
# recursion
#

def cal(end):
    return end + cal(end - 1) if end != 1 else 1

import sys
print(sys.getrecursionlimit())
# 超過限制就爆了

# 「想更深入了解遞迴的運作的話，請參考他的解說及提供的參考資料：
# 有點雞蛋裡挑骨頭，但遞迴在Python裡面有深度限制是因為沒做tail-call optimization。
# 在其他有做tail-call optimization的語言裡面就不會有深度限制，
# 另外在某些語言裡面recursion也不一定比iteration慢。
# 甚至在Python裡面也可以用decorator達到tail-call效果：
# https://towardsdatascience.com/python-stack-frames-and-tail-call-optimization-4d0ea55b0542 」



#
# practice
#

# 假定有一個樓梯，你從第0階要爬到第n階，
# 每次你只能選擇爬1階或者爬2階，這樣稱做一步。
# 請寫出一個函式名為cs，給定n的値以後(n > 0)，
# 計算出從第0階爬到第n階的方法共有幾種不同的變化？
# 例：
# cs(1) = 1 (1)
# cs(2) = 2 (1+1, 2)
# cs(3) = 3 (1+2, 2+1, 1+1+1)
# cs(4) = 5 (1+1+2, 2+2, 1+2+1, 2+1+1, 1+1+1+1)
# 請分別給出遞迴解和迭代解。

# 遞迴解
def cs(n):
	if (n > 1):
		return cs(n-1) + cs(n-2)
	else:
		return 1


# 迭代解 - 1
def cs(n):
    if n == 1 or n == 2: return n
    s1, s2 = 1, 2
    for i in range(n - 2):
        # Python的賦值是會一起看開始前的值來計算
        # 所以不會因為s1的值變s2了, s2新的值就變成s2+s2
        s1, s2 = s2, s1 + s2
    return s2

for i in range(1, 101):
    print(cs(i))


# 迭代解 - 2
def cs(n):
	r = 0
	q = 1
  	p = None 
	if n <= 1:
		return n
	else:
		for i in range(n-1):
			p = r + q
			r = q
			q = p
		return p
# cs(5)


# optimize (use dict hash map property)
def cs(n, dic):
    # n在裡面就直接回傳(因為已經算過了!)
    if n in dic:
        return dic[n]
    # 先將n的結果算完再回傳，別忘了放到字典裡！
    dic[n] = cs(n-1, dic) + cs(n-2, dic)
    return dic[n]

dic = {1 : 1, 2 : 2} # 預設cs(1), cs(2)的結果
for i in range(1, 101):
	print(cs(i, dic))


# optimize lru_cache => lru_cache 可以記住函式已經計算過的內容，並存放起來，在maxsize=None的時候，我們就不會限制它最多可以記幾個，
import functools
@functools.lru_cache(maxsize=None) # 用@開頭的稱為裝飾器，

def cs(n):
    if n == 1 or n == 2:
        return n
    return cs(n-1) + cs(n-2)

for i in range(1, 101):
	print(cs(i))



#
# 測試運行時間. https://officeguide.cc/python-measure-execution-time-tutorial-examples/
#

import time
start = time.time()
for i in range(10000):
    "-".join(str(n) for n in range(100))
end = time.time()
print("執行時間：%f 秒" % (end - start))



#
# Cython https://buzzorange.com/techorange/2019/08/05/cython-raise-speed-of-python/
# 將 python 編譯成 C, C++ 執行，加快程式速度 
#




