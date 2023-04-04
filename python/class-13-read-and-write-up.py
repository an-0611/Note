# -*- coding: utf-8 -*

# 
# open(name, mode)   (檔案名, 指令)
# 

# mode模式是一個字串，通常狀況下會有1~2個字母，其代表涵義如下：
# 第一個字母：
# 'r' -> 讀取(read)
# 'w' -> 寫入(write)(但不給r預設還是會可讀)
# 'x' -> 新增檔案(exclusive creation)，如果檔案已存在則回傳錯誤
# 'a' -> 在結尾處寫入(append)
# 第二個字母：
# 'b' -> 用二進位的方式來處理
# (預設則是當成文字來處理)
# '+'號： -> 更新(updating) (可讀可寫)
# 通常會用'r+'，代表可讀可寫。


# 方法一
# file = open(name, mode)
# ... (使用file來處理檔案)
# file.close() # 用完要關閉檔案

# file = open('test.txt', 'w')

# file.write('院子落葉\n跟我的思念厚厚一疊')

# file.close()


# 方法二
# with open(name, mode) as file:
    # ...(使用file來處理檔案)
# 離開這個with的區塊以後，file自動關閉。

# with open('test.txt', 'w') as file:
# 	file.write('院子落葉\n跟我的思念厚厚一疊')


# 
# print 也可以當成 write (python 2.X 似乎不能用)
# 

# f = open('poem.txt', 'w')
# # print('院子落葉\n跟我的思念厚厚一疊', file = f, sep = '', end = '')
# print('院子落葉\n跟我的思念厚厚一疊', file = f)
# f.close() # 要先close()以後，才會真的寫入完畢！



# 
# 讀寫有可能發生錯誤 要用相關函式包起來
# 

# import sys
# import os
# from sacred.utils import FileExistsError

try:
	f = open('test.txt', 'w')
	f.write('窗外的麻雀\n窗外的小麻雀\n窗外的雖小麻雀')
except Exception: # 想直接全包也行啦XD!
	print('檔案已存在!')



#
# read(), readline(), readlines()。
#

#
# read() 限制每次 read 的字元
#

# f = open('test.txt', 'r')
# poem = f.read(12)
# print(poem)
# f.close()


#
# readline()
#

# f = open('test.txt', 'r')
# cnt = 0
# poem = ''
# while True:
#     cnt += 1
#     line = f.readline()
#     if not line: break
#     print('Line %d: %s' % (cnt, line))
#     poem += line


# Line 1: 窗外的麻雀
# Line 2: 窗外的小麻雀
# Line 3: 窗外的雖小麻雀


#
# readlines()
#

f = open('test.txt', 'r')
lines = f.readlines()
print(lines[0])

# lines
# ['院子落葉\n', '跟我的思念厚厚一疊\n', '\n', '幾句誓言\n', '也無法將我的熱情冷卻\n', '   ']


# Error handler
# https://ithelp.ithome.com.tw/articles/10160048

# Reference : https://ithelp.ithome.com.tw/articles/10245133




