# -*- coding: utf-8 -*

# 
# CSV 
# 

# 一般而言，一個CSV檔案中，
# 每一個row(列)的不同單位常以逗號分隔，
# (也有用tab鍵的，相當於'\t')
# 而column(行)的計算則是以換行符號為準。
# (Unix/Mac系統使用'\n'，Windows系統則用'\r\n')
# 註：中國和台灣在指稱列跟行時是剛好相反的，容易搞混。
# 如果沒有特別需求的話，直接使用row/column來對應稱呼橫向/直向就好。

# 
# CSV - write
# 

# import csv
# # with open('student.csv', 'w', newline='') as f:
# with open('student.csv', 'wb') as f:
#     csvw = csv.writer(f, delimiter=' ') # delimiter預設是','，可以自己更改
#     csvw.writerow(['姓名', '數學', '英文', '物理']) # 一次寫一個row
#     students = [
#         ['阿明',   55,  70,   55],
#         ['小美',   90,  88,  100],
#         ['HowHow', 80,  60,   40]
#     ]
#     csvw.writerows(students) # 一次寫多個rows

# 設置 newline='' 是避免行距兩倍的情況 , python 2 不支援
# solution: https://www.codenong.com/51832593/
# https://blog.csdn.net/ppdyhappy/article/details/80431899

# 
# CSV - read
# 

# import csv
# with open('student.csv', 'r') as f:
#     csvr = csv.reader(f, delimiter=' ') #
#     student_from_file = [row for row in csvr]

# print(student_from_file)


# 
# CSV - DictWriter/DictReade
# 

import csv

# with open('student_dic.csv', 'w', newline='') as f:
with open('student_dic.csv', 'wb') as f:
    field = ['姓名', '數學', '英文', '物理'] # 第一個row做為欄位名稱
    csvw = csv.DictWriter(f, delimiter=' ', fieldnames=field)
    csvw.writeheader()
    csvw.writerow({'姓名':'阿明', '數學':55, '英文':70, '物理':55})
    csvw.writerow({'姓名':'小美', '數學':90, '英文':88, '物理':100})
    csvw.writerow({'姓名':'HowHow','數學':80, '英文':60, '物理':40})

with open('student_dic.csv', 'r') as f:
    # DictReader將第一個row當做欄位名稱，所以就省略了
    csvr = csv.DictReader(f, delimiter=' ') 
    student = [row for row in csvr]
    print(student)




# Reference: https://ithelp.ithome.com.tw/articles/10245278
