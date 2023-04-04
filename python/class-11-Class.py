# -*- coding: utf-8 -*

# 
# Class
# 

# 最基礎的類別定義如下
class Student():
    pass # pass表示暫時不做任何事情，但將來必須要將其填補好。

ming = Student() # 阿明是個學生
mei = Student() # 小美是個學生，但和阿明不一樣


class Student():
    def __init__(self, name):
        self.name = name


# 在一個物件被初始化的時候，最先會呼叫其中的__init__()函式。
# 它最前面必須要是self開頭，self的概念是指這個物件本體，
# 我們可以透過self.xxx的方式來取得或修改物件的其他屬性或方法。
# 注意到除了self以外，我們還增加一個name，
# 代表當我們呼叫Student()時，其第一個位置傳入的將會是name。
# 而self.name = name則代表我們要在開始時，
# 將從外面傳入進來的name的值，
# 存放進這個物件本體的name的值。



class Student():
    def __init__(self, name):
        self.name = name
    
    # 可以利用self取得自己這個類別裡面的變數
    def readMyName(self):
        print('聽清楚了，我的名字是' + self.name + '!!!')

ming = Student('阿明')
mei = Student('小美')
print(ming.name)
print(mei.name)
ming.readMyName()
mei.readMyName()


# 
# homework
# 

# 在上述的例子當中，請為類別新增一個字典，名稱為score，
# 將該字典用來儲存{'科目':'分數'}的各科成績，並修改__init__()的函式，
# 在產生阿明及小美時，同時輸入各科成績，
# 如未輸入則預設為0分(也就是缺考)。
# 阿明的成績分別為：數學55/英文70/物理55
# 小美的成績分別為：數學90/英文88/物理100

class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def compare(self, b):
        diff = sum(self.score.values()) - sum(b.score.values())
        # 有冒號的式子如果底下程式碼只有一行，也可以選擇直接和判斷式寫成同一行
        if diff > 0: print(self.name + '贏了！')
        elif diff == 0: print('什麼？竟然平手？！')
        else: print('可...可惡，難道，這就是' + b.name + '真正的實力嗎？')

class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def compare(self, B):
        diff = sum(self.score.values()) - sum(B.score.values())
        if diff > 0: print('{} 贏了！'.format(self.name))
        elif diff == 0: print('什麼？竟然平手？！')
        else: print('可...可惡，難道，這就是{}真正的實力嗎？'.format(B.name))

ming = Student('阿明', { '數學': 55, '英文': 70, '物理': 55 })
mei = Student('小美', { '數學': 90, '英文': 88, '物理': 100 })
# 承上題，請新增一名Student，其name為'HowHow'，
# 數學成績為80，英文成績為60，物理成績為40。
howhow = Student('HowHow', { '數學': 80, '英文': 60, '物理': 40 })


# 請為Student新增一個方法，讓兩個Student可以互相比較，
# 名稱為compare()。
# 例如A.compare(B)，假設：
# A的總分高於B -> A的名字 + '贏了！'
# A的總分等於B -> '什麼？竟然平手？！'
# A的總分小於B -> '可...可惡，難道，這就是' + B的名字 + '真正的實力嗎？'

# 並分別讓阿明和HowHow比較、阿明和小美比較、小美和HowHow比較，輸出結果。
ming.compare(howhow)
ming.compare(mei)
mei.compare(howhow)




#
# 繼承
#

class Car():
    def whoami(self):
        print('I\'m a Car!')

class Tesla(Car):
    pass

car = Car()
tla = Tesla()
car.whoami()
tla.whoami()



#
# override(覆寫/覆載)
#

class Car():
    def whoami(self):
        print('I\'m a Car!')

class Tesla(Car):
    def __init__(self):
        self.pilotmode = 1 # ON: 1, OFF: 0
    def whoami(self):
        print('I\'m a Tesla, not a trash car!')
    def autopilot_switch(self):
        self.pilotmode ^= 1 # ^是取XOR(互斥或)，所以會在0和1之間切換
        if self.pilotmode == 0: print('Auto-pilot mode switch off!')
        else: print('Auto-pilot mode switch on!')

car = Car()
tla = Tesla()
car.whoami()
tla.whoami()
tla.autopilot_switch()
tla.autopilot_switch()



# 
# super().  取得父類別的屬性方法
# 

class Car():
    def __init__(self, name):
        self.name = name
    def whoami(self):
        print('My name is ' + self.name)
        print('I\'m a Car!')

class Tesla(Car):
    def __init__(self, name, mode):
        super().__init__(name) # 使用super來對name初始化，看起來稍微多此一舉，但可以保證對於name處理的一致性，之後如果要額外針對Car這個父類別修改時，就可以一起同時影響到Tesla這邊
        self.pilotmode = mode
    def whoami(self):
        super().whoami() # 先喊名字跟喊自己是輛車
        print('Also, I\'m a Tesla, not a trash car!') # 這兩行再做只有Tesla會做的事情
        print('Auto-pilot mode: ' + str(self.pilotmode))
    def autopilot_switch(self):
        self.pilotmode ^= 1
        if self.pilotmode == 0: print('Auto-pilot mode switch off!\n')
        else: print('Auto-pilot mode switch on!\n')

car = Car('CC')
tla = Tesla('TT', 0)
car.whoami()
print()
tla.whoami()
tla.autopilot_switch()
tla.whoami()
tla.autopilot_switch()

