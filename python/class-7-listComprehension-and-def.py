# -*- coding: utf-8 -*

# 
# list comprehension [算式 for 單項 in 迭代項目] (串列生成式/串列表達式/串列解析式) 
# dict 也有類似觀念 {key:value for 單項 in 迭代項} (dict 的生成式 key & value 必須都給)

[2 * i for i in range(9) if i % 2 == 0] # 取0~8當中能整除2的數，每個都先乘以2再加到list
# [0, 4, 8, 12, 16]


[[0 for i in range(3)] for j in range(4)] # 一層一層看就會理解等於[0, 0, 0]重複4次
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


combo = [(row, col) for row in range(4) for col in range(3)] # 留意4跟3的順序
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]



#
# def
#

# 由於Python是腳本式語言，
# 一個函式必需要先被定義或引入後，
# 才能夠被使用，所以我們必須在使用(或稱呼叫)函式前，
# 先將它定義完，在下一行開始才能夠使用它。


def area(r):
    pi = 3.14
    return pi * r ** 2

print(area(10))



def printAll(r, pi=3.14):
	def area():
		return pi * r ** 2
	def perimeter():
		return 2 * pi * r
	# 下面{}的用法是所謂的format，可以將多個變數按照順序放置到{}中
	print('半徑 = {}的圓，其周長 = {}，面積 = {}'.format(r, area(), perimeter()))
	
printAll(3, 3.14159)


# 
# homework
# 

#  請使用兩個迴圏，將1~10之間的偶數兩兩相乘並放到一個空的list中。
# (所以這個list應該會有2 * 2, 2 * 4, 2 * 6, 2 * 8, 2 * 10, 4 * 2, 4 * 4, ..., 10 * 10)
arr = range(1, 11)[1::2]
list = list()
for i in arr:
	for j in arr:
		list.append(i * j);

print(list)

# 請改用列表生成式來完成1的問題。
# [2 * i for i in range(9) if i % 2 == 0]
# [[0 for i in range(3)] for j in range(4)]
# combo = [(row, col) for row in range(4) for col in range(3)]

arr = [(num * num1) for num in range(1, 11)[1::2] for num1 in range(1, 11)[1::2]]
print(arr)



# 請用while, if else等，寫出一個猜數字的遊戲，遊戲的答案為37，
# 請在開始時提示使用者猜1~100範圍中的數字，
# 並依據使用者的答案，逐步將範圍縮小，直到猜中答案，則印出恭喜訊息並離開迴圏。
# (先不考慮使用者會亂輸入的問題，並且要告訴使用者這次猜的比答案大還是小)

from random import randrange
randrange(1, 101)

min = 1
max = 100
answer = randrange(1, 101)
mode = 0

while mode != answer:
	mode = input('請輸入終極密碼: ' + str(min) + ' 到 ' + str(max) + ' [請輸入數字]: ')
	if (type(mode) != int):
		print('請輸入數字')
		continue
	if mode > max or mode < min:
		print('超過範圍，請重新選擇')
		continue
	if mode > answer:
		max = mode - 1
	else:
		min = mode + 1
else:
	print('恭喜，密碼是: ' + str(answer))

# 終極密碼 二分最快? 最多六次


# Reference: https://ithelp.ithome.com.tw/articles/10241349






# fetch("https://ddragon.leagueoflegends.com/cdn/11.6.1/data/zh_TW/champion.json", {
#   method: "GET",
#   headers: [
#     ["Content-Type", "application/json"],
#     ["Content-Type", "text/plain"]
#   ]
# });



# var script = document.createElement('script');
# script.onload = function () {
    
# };
# script.src = 'https://unpkg.com/axios/dist/axios.min.js';

# document.head.appendChild(script);

# axios.get('https://ddragon.leagueoflegends.com/cdn/11.6.1/data/zh_TW/champion.json')

# # window.$nuxt.$axios.get('https://ddragon.leagueoflegends.com/cdn/11.6.1/data/zh_TW/champion.json').then(res => console.log(res))



