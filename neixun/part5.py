# 面向对象编程

# 对象.方法: 针对不同的对象定义的方法
# 字符串.方法
s1 = str()
s1 = 'abcdef'
s1.center(20)

# 列表.方法
l1 = list()
l1 = [1,2,3,4]
l1.remove(2)
l1.count(3)

# 可以在列表上使用字符串的方法?
# l1.center(20)


# 自定义类的格式
# class 类名(object):
#     a = 10
#     b = 20
#     def 方法名(self):
#         代码


# 例1: 定义一个用户类
class Users(object):
    name = ''
    password = ''
    address = ''

    def login(self):
        pass

    def out(self):
        pass

    def run(self):
        pass

    def buy(self):
        pass

# 例2:使用一个类,创建对象
u1 = Users()

# 例3:使用对象 调用方法
u1.buy()

# 例4:如何给方法定义参数
class Users2(object):
    name = ''
    password = ''
    address = ''

    def login(self,username,password):
        pass

    def out(self,sign=True):
        pass

    def run(self,*args):
        pass

    def buy(self,**pay):
        pass

# 例5:如何调用有参数的方法
u2 = Users2()

u2.login('abc','123456')


# 1.创建类
# 2.通过类创建对象
# 3.通过对象调用方法
# 4.给方法写参数


# 例6: 类的属性
print(u2.name)  # 使用
u2.name = '张三' # 修改属性值
u2.age = 20  # 添加
# u2.password  # 删除

# 例7: 私有属性,对象属性
# 私有属性 : 只有在类中能够调用
class Users3:
    __name = '张三'
    __age = 30
    address = '北京'

    print(__name)

u3 = Users3()
# u3.__name


# 例8:魔术方法
class Users4:
    # 初始化方法:在创建对象时,自动执行
    def __init__(self):
        print('自动执行')

    # 描述方法:描述类的基本情况
    def __str__(self):
        return '这是users4 类'

    # 描述方法:描述对象的长度
    def __len__(self):
        return 10


u4 = Users4()

print(u4)


# 例9:对象属性
class Car:
    pass



bmw = Car()
bmw.brand = '宝马'
bmw.power = 600
bmw.price = 1000000

benz = Car()
benz.brand = '奔驰'
benz.power = 800
benz.price = 2000000

# 你需要创建n个对象的时候,那么你需要写多少行代码? 4n

class Car:
    def __init__(self, a, b, c):
        self.brand = a
        self.power = b
        self.price = c


bmw = Car('宝马',600,100000)
bmw.km = 100
benz = Car('奔驰',800,2000000)



# 面向对象的特点
# 封装
# 继承 ***  继承是指一个对象直接使用另一对象的属性和方法
# 多态

# object:所有类的父类
# 父子
class A(object): #继承
    pass

class B: # 没有继承
    pass

# 继承的关系
class A:
    name = 'A'

    def a(self):
        print('这是A的a')

class B(A):
    pass

class C(A):
    pass

b1 = B()
b1.a()
b1.name
c1 = C()
c1.a()
c1.name


# -----------------------------
class A:
    name = 'A'

    def a(self):
        print('这是A的a')

class B(A):
    name = 'B'

    def b(self):
        print('这是B的b')

class C(B):
    pass

b1 = B()
b1.a()
b1.name  # 当自身拥有属性时,优先使用自己的
c1 = C()
c1.a()
c1.b()
c1.name

# ---------------------------
class A:
    name = 'A'

    def a(self):
        print('这是A的a')

class B:
    name = 'B'

    def b(self):
        print('这是B的b')

class C(A,B):
    pass


c1 = C()
c1.a()
c1.b()
c1.name

# ----------------------------------

class A:
    name = 'A'
    age = 10
    def a(self):
        print('这是A的a')

class B(A):
    name = 'B'
    age = 20
    def a(self):
        print('这是B的a')
        super().a() # super()代表父类

    def get_name(self):
        return self.name,super().name  # 类中使用属性 self.属性名 # 父类的属性 super().属性名

b1 = B()
b1.get_name()

