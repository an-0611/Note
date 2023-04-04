# -*- coding: utf-8 -*

# 代表註解

''' 被是視為 函式 打說明文件用的文字 稱之為文件字串(docstring) '''

# \ 用來延續 運算 或函式 告訴直譯器該行還沒結束

# 
# if else 語法
# 

tl = range(7)
if 9 in tl:
	print('9 in tl')
elif 8 in tl:
	print('8 in tl')
else:
	print('no mapping result')


tl = set()
tl.update(range(7))
if 7 not in tl:
	print('7 不在串列中')
else:
	print('7 在串列中')

# 
# 比較運算子有：== (相等), !=(不等於), < (小於), > (大於), <=(小於等於), >=(大於等於), in...(前者在後者的範圍內)
# 布林運算子常用的有：and(且), or(或), not(否定)
# 


# 
# while 語法
# 

# case 1
while True: # 使用while True須謹慎，一定要留下可以離開的方法！
    mode = input('請問你要選擇什麼模式？1. 簡單模式 2. 困難模式 3. 專家模式 [輸入1, 2, 3] ')
    if mode == '3':
        print('\n選擇專家模式的難關 帶著我的夥伴 還有我的不平凡')
        break # 跳出迴圈
    elif mode == '1' or mode == '2': # 簡單來說，其他模式都不給過XD
        print('不選難一點的嗎？再給你選一次！\n')
        continue # 所以在這邊會直接回到迴圈開始處，因而不會印出下一行 (即跳過本輪迴圈)
    print('請輸入正確的選項！\n')

print('恭喜你選擇專家模式，加油！')


# case 2 (while else: 當while正常的結束，沒有被break跳出的話)

mode = ''
while mode != '3': # 使用者選專家模式才能離開！
    mode = input('請問你要選擇什麼模式？1. 簡單模式 2. 困難模式 3. 專家模式 [輸入1, 2, 3] ')
    if mode == '3':
        print('\n選擇專家模式的難關 帶著我的夥伴 還有我的不平凡')
    elif mode == '1' or mode == '2': # 簡單來說，其他模式都不給過XD
        print('不選難一點的嗎？再給你選一次！\n')
    else:
        print('不想玩就算了！\n') # 不想玩的，後續就不繼續給提示
        break
else: # 正常離開，表示mode輸入了'3'
    print('恭喜你選擇專家模式，加油！')


#
# 迭代(iteration)
#

lt = range(5)
for num in lt:
	print(num)


i = 0;
while i < len(lt):
	print(lt[i])
	i += 1


shrimp = {'炸鳳尾蝦':['蝦子','核果','油'],'雲龍炸蝦':['蝦子','核果','油','豆皮','醬汁']}
shrimp = {'a':['1','2','3'],'b':['4','5','6','7', '8']}
for name, ingre in shrimp.items():
	print(name, ingre);

# ('a', ['1', '2', '3'])
# ('b', ['4', '5', '6', '7', '8'])


#
# range(start, stop, step)
#





# Reference: https://ithelp.ithome.com.tw/articles/10240601

