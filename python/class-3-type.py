# -*- coding: utf-8 -*

#
# int() && float()
#
float(1) # 從沒有小數點的int變成帶小數點的float
1.0
int(1.0) # 很直觀XD
1
int(1.6) # 咦? 不是2嗎？
1
int(1.4)
1
int(-1.1)
-1
int(-2.1) # 所以是無條件捨棄
-2
# 1.5+1　# float和int相加
2.5
# 1+3.0  # 順序不影響
4.0

#
# bool()
#
bool(0)
False
bool(1)
True
bool(3)
True
bool(-2)
True
int(True)
1
int(False)
0

# 在Python中如果數字用10以外的基數來表達時，
# 會額外做顯示上的處理：
# 二進位 -> 0b或0B (b代表binary)
# 八進位 -> 0o或0O (o代表octal)
# 十六進位 -> 0x或0X (x代表hexadecimal)

0b10  # 2
2
0b111 # 4+2+1=7
7
0o11  # 8+1=9
9
0x1F  # 16+15=31 (A~F分別代表16進位的10~15)
31

#
# str()
#
str(9)
'9'
str(97.1)
'97.1'
str(True)
'True'
str(0o11) # 以其他基數表達的int，仍會先轉回10進位再處理
'9'



#  \ = 跳脫
print('\"你好\"')

#  \n = 換行
print('我是第一行\n我是第二行')

# 想同時印出多個字串的話，可以用逗號來連接，Python會幫忙在中間加空格。
print('I\n','feel','good') # 即便換行，feel前面還是有一格空格




# 
# python 常見字串操作
# 

'a'+'b'+'c' # 相加就是串在一起就對了！
'abc'

'apple'*2   # 乘上的正整數相當於重複的次數
'appleapple'

a = 'apple'
a[3]        # 取第3位(從0起算)
'l'

a[0:4:1]    # 切片slice: 從0開始，到4結束，每次跳1單位
'appl'

a[0:4:2]    # 切片slice: 從0開始，到4結束，每次跳2單位
'ap'

len(a)      # 取長度
5

len(a[0:4:1]) # 剛剛切出的長度是4
4

b = 'An apple a day, keeps the doctor away.'
b.split() # 用括號內的字串來分割，預設是空白字元(換行/空格/位移tab)
['An', 'apple', 'a', 'day,', 'keeps', 'the', 'doctor', 'away.']

b.split(',') # 用逗號來分割(留意用來分割的東西會不見)
['An apple a day', ' keeps the doctor away.']

b.split('.') # 因為.的右邊沒東西，所以會多一個空字串
['An apple a day, keeps the doctor away', '']

c = b.split()
c
['An', 'apple', 'a', 'day,', 'keeps', 'the', 'doctor', 'away.']

d = '\n'.join(c) # '字串'.join(要被接起來的串列)
d
'An\napple\na\nday,\nkeeps\nthe\ndoctor\naway.'
print(d) # 印出來的時候就知道\n是拿來換行了！
An
apple
a
day,
keeps
the
doctor
away.


# 
# homework
# 

# 給定字串chs = 'abcdefghijklmnopqrstuvwxyz'，請印出：
# 1.1. 從z起算往回頭走，每次step為-2的字串
chs = 'abcdefghijklmnopqrstuvwxyz'
l = len(chs)
print(chs[l::-2])
print(chs[::-2])

# 1.2. 將索引值為16的字元，加上(索引值為14的字元重復2次)，
# 並用一個空格將前者和字串'有種果汁真好喝~'連接起來。
print(chs[16] + (chs[14] * 2) + "\n" + "有種果汁真好喝~")

# 1.3. 已知bin()的方法可以將一個int值用二進位表示並轉為字串，
# 請嘗試給出36的二進位字串，但須去除'0b'的部分。
print(bin(36)[2::])
print(bin(36)[2:])

# 1.4 給定a, b, c = 'pen', 'apple', 'pine'，
# (註：沒錯，你可以在一行同時生成多個變數，使用逗號隔開即可)
# 請用a, b, c組合出'pen pine apple apple pen'。
a, b, c = 'pen', 'apple', 'pine'
print(a + c + b + b + a)
print(a+c+b*2+a)


