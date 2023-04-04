# -*- coding: utf-8 -*
# Python中在計算加減乘除的時候，只有除法比較特別，
# 當使用單斜線的除法時，計算結果會預設帶有小數點，
# 這種「型態」和原先的整數不同，
# 在Python中整數稱作int，而帶小數點的數字則稱為float。
# 要取得相除的整數，請使用雙斜線：

# 
# float & int
# 
a = (1+100) * 100 / 2
print(a)
print(type(a))

b = (1+100) * 100 // 2
print(b)
print(type(b))

# 留意如果這當中你使用了帶小數點的數字，即便使用雙斜線，仍然會得到float的結果
c = (1+100) * 100 // 2.0
print(c)
print(type(c))


# 
# homework
# 
# 假設圓周率為3.14，一個圓的半徑是7.77
# 請用上面的所學及print()方法，
# 在直譯器中印出該圓的周長和面積。
# (註：print()內可以放計算式子呦！)

# 1
pi = 3.14
radius = 7.77

print((radius * 2) * pi)
print((radius ** 2) * pi)


# 承1，如果有另外兩個圓的半徑分別是5.3和2.5，
# 請計算出這三個圓的周長的和和總面積。

#2
radius2 = 5.3
radius3 = 2.5

print((radius + radius2 + radius3) * 2 * pi)
print((radius ** 2) * pi + (radius2 ** 2) * pi + (radius3 ** 2) * pi)


# refereren: https://ithelp.ithome.com.tw/articles/10237877