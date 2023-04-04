# -*- coding: utf-8 -*

#
# classmethod
#

class Student():
    cnt = 0 # 這個變數是屬於整個Student類別的
    def __init__(self, name, score):
        print(self)
        Student.cnt += 1 # 每次新開一個Student的物件，計數器就會+1
        self.name = name
        self.score = score
    
    def readMyName(self):
        print('聽清楚了，我的名字是' + self.name + '!!!')
        
    def compare(self, b):
        diff = sum(self.score.values()) - sum(b.score.values())
        # 有冒號的式子如果底下程式碼只有一行，也可以選擇直接和判斷式寫成同一行
        if diff > 0: print(self.name + '贏了！')
        elif diff == 0: print('什麼？竟然平手？！')
        else: print('可...可惡，難道，這就是' + b.name + '真正的實力嗎？')
    
    @classmethod
    def getCount(cls):
        print('目前的學生總數：%d' % cls.cnt) # 別忘了print也可以用format類型的形式
        print('目前的學生總數：%d' % Student.cnt) # 同上
        

print('開始之前')
Student.getCount() 

ming = Student('阿明', {'數學':55, '英文':70, '物理':55})
ming.readMyName()
Student.getCount()

mei = Student('小美', {'數學':90, '英文':88, '物理':100})
mei.readMyName()
Student.getCount()

howhow = Student('HowHow', {'數學':80, '英文':60, '物理':40})
howhow.readMyName()
Student.getCount()


# 對於類別方法，我們會在前面加上"@classmethod"，
# 同時由於"class"已經是Python的保留字(用來定義類別)，
# 所以在使用時Python是給定"cls"，用來指稱這個類別。
# 不過直接使用Student.cnt也可以，意思是一樣的。
# 所以請留意類別方法/屬性和物件方法/屬性的差異，
# 前者是屬於整個類別，後者是會依照產生的物件來操作。
# 可以看到即便在開始之前，
# 我們還沒加入任何Student，類別屬性就已經存在了。

# 還有一種比較特別的方法叫靜態方法。
# 使用"@staticmethod"來開頭，不需要self或cls參數，
# 通常用以處理可以固定不變，不受其他屬性影響的東西。


#
# staticmethod
#

class Desolve():
    @staticmethod
    def ads():
        print('無情工商時間!')
        print('從LeetCode學演算法是一系列非常好的課程!')
        print('https://bit.ly/leetcodeall')

Desolve.ads()



# 
# 繼承用法
# 

# 一個類別也可以繼承不只一個類別
# 簡單來說，當A跟B有相同的方法時，
# 呼叫方法會呼叫哪一個，端看你把誰寫前面，寫越前面的優先程度越大。


class A():
    def __init__(self):
        self.name = 'A'
        print('A')
        print('Name = ' + self.name)

class B():
    def __init__(self):
        self.name = 'B'
        print('B')
        print('Name = ' + self.name)

class C(A, B):
    pass
    
test = C()

# Name = 'A'



#
# 特殊的方法：
#

# 最後，我們來談談特殊的方法：
# 當我們在Python內使用那些 ==, !=, >=, <=, >, <......等比較運算子時，
# 其實是依靠Python有對這些東西做定義，才知道如何去做比較；
# 但是對於我們自己生成的類別來說，想要比較兩個相同類別的物件，
# 可能就需要我們自己定義了。
# 例如說假設有一個類別叫nmod3()，會紀錄數字並判斷餘數是否相等：

# !!!!!! 用於物件的比較 取代原本的運算子功能 !!!!!!
# !!!!!! 用於物件的比較 取代原本的運算子功能 !!!!!!
# !!!!!! 用於物件的比較 取代原本的運算子功能 !!!!!!


class nmod3():
    def __init__(self, num):
        self.num = num
        
    def __eq__(self, n2): # 定義 "==" 這個運算子為是否除以3的餘數相同
        return self.num % 3 == n2.num % 3
        
a = nmod3(11) # 除以3餘2
b = nmod3(18) # 除以3餘0
c = nmod3(17) # 除以3餘2

print(a == b)
print(a == c)
print(b == c)


# 這些都是兩個物件相比，我們假定後面的物件叫b。
# __eq__ => self == b
# __ne__ => self != b
# __lt__ => self < b
# __gt__ => self > b
# __add__ => self + b
# __mul__ => self * b # 原來字串的乘法是這麼弄出來的XD
# __len__ => len(self) # 可以定義什麼是你的物件的"長度"


# 
# homework
# 

# 請參照之前的Student類別，
# 假設今天有一個科系要求是(數學 * 2 + 英文 * 5)的加權分數採計，
# 定義__gt__(也就是>), __eq__(也就是==)，
# 用上面的採計方式及重新定義的比較運算子來寫成新的A.compareE(B)函式，
# 假設：
# A的加權分高於B -> A的名字 + ' > ' + B的名字
# A的加權分等於B -> A的名字 + ' == ' + B的名字
# A的加權分小於B -> A的名字 + ' < ' + B的名字
# 並分別讓阿明和HowHow比較、阿明和小美比較、小美和HowHow比較，輸出結果。
# (請保留之前compare的函式及呼叫的比較，我們兩種都要比呦!)

# 承上，請使用類別方法和屬性，在每次進行比較時就將總比較次數+1，
# 並print出來，這邊的「比較」是指compare()及compareE()都算。

class Student():
    cp_cnt = 0 # 這個變數是屬於整個Student類別的
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __eq__(self, b):
        # print('self = %d, b = %d' % (self.score['數學'] * 2 + self.score['英文'] * 5, b.score['數學'] * 2 + b.score['英文'] * 5))
        return self.score['數學'] * 2 + self.score['英文'] * 5 == b.score['數學'] * 2 + b.score['英文'] * 5
    
    def __gt__(self, b):
        return self.score['數學'] * 2 + self.score['英文'] * 5 > b.score['數學'] * 2 + b.score['英文'] * 5
    
    def readMyName(self):
        print('聽清楚了，我的名字是' + self.name + '!!!')
        
    def compare(self, b):
        Student.cp_cnt += 1
        # 同樣，印出diff方便檢查正確性，讀者可自行註解掉。
        diff = sum(self.score.values()) - sum(b.score.values())
        print('diff = %d' % diff)
        # 有冒號的式子如果底下程式碼只有一行，也可以選擇直接和判斷式寫成同一行
        if diff > 0: print(self.name + '贏了！')
        elif diff == 0: print('什麼？竟然平手？！')
        else: print('可...可惡，難道，這就是' + b.name + '真正的實力嗎？')
        print('已比較 %d 次!\n' % Student.cp_cnt)
    
    def compareE(self, b):
        Student.cp_cnt += 1
        if self > b: print(self.name + ' >  ' + b.name)
        elif self == b: print(self.name + ' == ' + b.name)
        else: print(self.name + ' <  ' + b.name)
        print('已比較 %d 次!\n' % Student.cp_cnt)
    
    @classmethod
    def getCpCount(cls):
        print('目前的比較次數：%d' % cls.cp_cnt) # 別忘了print也可以用format類型的形式

print('開始之前')
Student.getCpCount() # 開始前先看看是不是0

ming = Student('阿明', {'數學':55, '英文':70, '物理':55})
ming.readMyName()
mei = Student('小美', {'數學':90, '英文':88, '物理':100})
mei.readMyName()
howhow = Student('HowHow', {'數學':80, '英文':60, '物理':40})
howhow.readMyName()

ming.compare(howhow)
ming.compareE(howhow)
ming.compare(mei)
ming.compareE(mei)
mei.compare(howhow)
mei.compareE(howhow)



# Refereren: https://ithelp.ithome.com.tw/articles/10244886