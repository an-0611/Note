# -*- coding: utf-8 -*

# e.g.
# import module # 直接將整個檔案納入(不用加.py)
# from module import function # 只匯入function的部分
# import module as xx # xx是自己選的名字，用來在這個程式中全程替代原先的module名
# from module import function as oo # 這時候用oo就相當於跟function一樣

# import whileTest

# from random import randrange
# randrange(1, 101)

# import random
# random.random()

# from random import random as rd
# rd()

# 如果是Python內建的模組，那麼不論你的主要的程式.py檔放在哪都沒問題；
# 但如果你想要匯入的是別的檔案，那麼要將這些檔案放在同一個目錄下，
# 才能夠正常匯入。
# 如果我們要更嚴謹一點的話，就要使用套件的形式。
# 假設我們有一批寫好的檔案，他們都是這個主程式可能會用到的工具，
# 我們可能會開一個名為utils(工具箱)的資料夾，
# 裝入所有的檔案，比方說假設有check.py, schedule.py這兩個檔案。
# 除此以外，還要裝入一個至少是空白的檔案，必須取名為__init__.py。
# (前後都有兩個底線)

# 所以我們的資料夾結構會變成這樣：
# |--class-9-import.py
# |--utils
# 　　|--__init__.py # 將文件夾變成一個 python 模塊
# 　　|--math.py
# 　　|--string.py

from utils import math, string
print(math.rd())
print(string.abc())


# 上次我們的猜數字遊戲本來是固定的數字，
# 已知現在可以使用從random模組中的函式取得亂數法，
# (詳見Python Document https://docs.python.org/3/library/random.html)
# 請利用random.randint(a,b)或random.random()，
# 將前面的題目中要猜的數字改成隨機的1~100(含)之間的整數。

# 承上題，1~100當中有一些數假設有我們想避開，不想被成為要猜的數字的話，
# 若給定該串列avoid_lt = [4, 14, 44, 94]，
# 請參照上面的說明，使用random.choice(seq)來處理。
# (random.choice()方法可以從一個序列型態的東西seq中隨機取出一個值)
# (序列是有順序的元素的集合統稱，比如list, tuple, range)
# 提示：可以先新增一個數列並去處掉不要的元素再做random.choice()


import random
min = 1
max = 100
banAnswers = [1,2,3,4,5]
answerSet = set(range(1, 101)) - set(banAnswers)
answer = random.choice(list(answerSet)) # set 沒有 seq , 要先轉 list, tuple, range
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



