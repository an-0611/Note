# -*- coding: utf-8 -*

# 
# dict
# 

# define dict
dic = dict()
dic = {}

dic = {'xd': 1, '放棄': False, [1,5,9]: 3}  # list是unhashable，不能作為key

dic = {'xd': 1, '放棄': False, 3.33: 3} # 這樣就沒問題啦！

dic['xd']
# 1

arr = [('a', 1),('b',2),('c',3)]

dicArr = dict(arr); # 串列 tuple 兩個字字串都可以拆成 dic, e.g. tuple 內保持兩個元素 及Key & value 的關係 則可以轉換成 dict, 若一個 tuple 超過兩個元素 就無法形成Key value 關係 會報錯
# { 'a': 1, 'b': 2, 'c': 3 }

tul = (['a','b'],['c','d'],['e','f'],['g','h']) # 裡外兩層不管是tuple或list都沒有問題！
dictul = dict(tul)
# {'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h'}

chs = ['ab','cd','13']
dicchs = dict(chs)
{'a': 'b', 'c': 'd', '1': '3'}


# 
# dict built in function
# 

dict1 = { 'id': 1, 'name': 'an' }
dict2 = { 'name': 'anan', 'age': 30 }
dict1.update(dict2) # 將dict2的內容複製後放到dict1(key重覆時，dict2的value優先)
# {'id': 1, 'name': 'anan', 'age': 30 }

del dict1['age']
# {'id': 1, 'name': 'anan' }

dict1.clear() # equal dict1 = dict()
# {}

dict1 = { 'id': 1, 'name': 'an' }
'name' in dict1
# True

dict1.keys()
# ['id', 'name']

dict1.values()
# [1, 'an']

dict1.items() # 會將原本 Key value 改成 tuple 呈現， 可以將 dict 轉成 tuple
# [('id', 1), ('name', 'an')]

dict2 = dict1.copy() # 相當於 js Object assign, 獨立兩個記憶體位置


# 
# set()
# 

set1 = set() # 也可以用大括號 {} 建立 set， 但不能用來建立空 set , 直接用大括號會變成 dict 
# set([])

set1.add(5)
# set([5])

set1.add(5) # 重複 KEY 無效
# set([5])

set1.add('aaa') # add 只能一次加一個 key
# set(['aaa', 5])

set1.update([1,2,3,4,5,6,7,8,9,10])
# set(['aaa', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

set('XDDDD') # 可用來判斷串列中有幾個元素
# set(['X', 'D'])

len(set([1,2,3,1,2,3,1,2,3]))
# 3

st1 = {'A', 'C', 'E'}
'A' in st1
# True

st1 = {'A', 'C', 'E'}
st2 = {'B', 'C', 'A', 'D'}

st1 & st2 # 取交集
# set(['A', 'C'])

st1.intersection(st2) # 取交集 同上
# set(['A', 'C'])

st1 | st2 # 取聯集
# set(['A', 'C', 'B', 'E', 'D'])

st1.union(st2) # 取聯集 同上
# set(['A', 'C', 'B', 'E', 'D'])

st1 - st2 # '-'和difference都是取差集，也就是取前者有，後者沒有
# set(['E'])

st1.difference(st2) # 取差集 同上
# set(['E'])

st1 ^ st2 # 取互斥
# set(['B', 'E', 'D'])

st1.symmetric_difference(st2) # 取互斥 同上
# set(['B', 'E', 'D'])

st1 <= st2 # '<='和issubset代表檢查前者是否是後者的子集
# False

st2 <= st1
# False

st1.issubset(st2)
# False


#
# homework
#

# 1.
shrimp = dict()
shrimp['炸鳳尾蝦'] = ['蝦子', '核果', '油']
shrimp['雲龍炸蝦'] = ['蝦子', '核果', '醬汁', '豆皮']

# 2.
lee = set(shrimp['炸鳳尾蝦'])
liu = set(shrimp['雲龍炸蝦'])

# 劉昴星的作品中比李嚴的作品多用了什麼材料？
liu - lee 
# ['醬汁', '豆皮'] 

# 李嚴的作品中比劉昴星的作品多用了什麼材料？
lee - liu
# ['油']

# 兩人的作品都有用到什麼材料？
lee & liu
# ['蝦子', '核果']

# 假定今天李嚴能做完醬汁的話，請將新增的材料(蘋果、洋蔥)以及內容(醬汁)，加到lee這個set中，
lee.add('蘋果')
lee.add('洋蔥')
lee.add('醬汁')

# 接著請指出現在李嚴的作品中比劉昴星的作品多用了什麼材料？
lee - liu

# 並請將材料和內容更新回shrimp這個字典中的對應作品。
shrimp['炸鳳尾蝦'].extend(['蘋果', '洋蔥', '醬汁'])


# 3.
# 已知有一個列表lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，
lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 請利用slice及其他方法來達成以下要求：
# a. 請生成一個lt1，其內容為lt的所有奇數
lt1 = set(lt[::2])
lt = set(lt)
# b. 請生成一個lt2，其內容為lt的所有偶數
lt2 = lt - lt1

# c. 請將lt2的所有元素依序附加到lt1上
a = list(lt1)
b = list(lt2)
a.extend(b)
lt1 = set(a)

# d. 請刪除lt1當中index 7和index 1的數
lt1 = list(lt1)
del lt1[7]
del lt1[1]
# [1, 3, 4, 5, 6, 7, 9, 10]

# e. 請將lt1進行排序
lt1.sort()







# reference: https://ithelp.ithome.com.tw/articles/10240088



lt = set()
if lt:
	print('lt is not empty')
else:
	print('lt is empty')
# lt is empty


shrimp = {'a':['1','2','3'],'b':['4','5','6','7','8']}
for name, ingre in shrimp.items():
	print(name, ingre)



	
