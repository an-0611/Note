# -*- coding: utf-8 -*

lt = []
# []

llt = list()
# []

lt = ['my', 'dict', 'doesn\'t', 'have', 'the', 'word', 'giving', 'up.', 9527, True]
# 一個串列裡的元素彼此不一定非得要是同樣的資料型態，這點跟C++/Java等不同

' '.join(lt) # 使用join可以將串列連接，但必須要全都是字串


' '.join(lt[:-2]) # 串列同樣可以用slice，用法和字串的邏輯一樣，所以倒數2個被去掉後就能正常join了！
# "my dict doesn't have the word giving up."

(' '.join(lt[:-2])).split()　# 使用split可以將字串拆成串列
# ['my', 'dict', "doesn't", 'have', 'the', 'word', 'giving', 'up.']

list('apple pen') # 直接對字串使用list()方法，會將每個字元拆開來變成一個串列
# ['a', 'p', 'p', 'l', 'e', ' ', 'p', 'e', 'n']

lt[::-1] # 同樣的，利用slice可以輕鬆做到將整個list反轉過來
# [True, 9527, 'up.', 'giving', 'word', 'the', 'have', "doesn't", 'dict', 'my']


#
# built-in function
#

# 
# list()
# 

lt = [1, 2, 3]
lt.append(4)
# [1, 2, 3, 4]

lt.extend([5,6,7,8])
# [1, 2, 3, 4, 5, 6, 7, 8

lt.insert(2, 2.5) # insert(index, value)
# [1, 2, 2,5, 3, 4, 5, 6, 7, 8]

del lt[2] # 可用於刪除整個陣列
# [1, 2, 3, 4, 5, 6, 7, 8]

lt.remove(1)
# [2, 3, 4, 5, 6, 7, 8] # 陣列中需有對應的值 否則報錯

lt.index(5) # 找該值在陣列中第一個索引值 沒有值會報錯

5 in lt
# True

9 in lt
# False

lt.count(5) # 該元素出現次數 找不到則為０
# 1

lt.sort() # 排序

lt2 = sorted(lt) # 不改變原始陣列 (lt) , lt2 為新的排序陣列

len(lt2) # 取陣列長度 


#
# tuple
#
# 1.占用空間較少
# 2.tuple的元素不會不小心被動到
# 3. tuple也可以做為字典的輸入使用

tpl = (1, 2, 3)
v1, v2, v3 = tpl # 可解構取值 像是 js 的解構


