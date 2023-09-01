# ----------------函数
# 函数:给定一个数集A,假设其中的元素为x,对A中的元素x施加对应的法则f,记作f(x).得到的与A相对应的另一数集B.假设B中每一个元素为y,则y与x之间的等量关系可以用y=f(x)表示

# python函数:并不仅限于 计算.可以实现功能复杂的流程

# 函数的基本操作
# 定义函数
#     输入:[2,3,4,5,6,7,8,9]
#     输出:[2,4,6,8,10,12,14]
# 使用函数
# start 且 输入

# python中函数的格式
# def 函数名(输入):
#     流程
#     return 输出

l1 = [2,3,4,5,6,7,8,9]
list(enumerate(l1))
# enumerate() 枚举函数,可以获得列表的 索引 和 值 [(索引,值),(索引,值)]
# 字典.items()   [(关键字,值),(关键字,值)]

# 定义函数
def f(nums):
    y = []
    for i,v in enumerate(nums):
        y.append(i+v)
    return y

# 使用函数
f([2,3,4,5,6,7,8,9])

# 查看函数
f


# 函数的参数
# 1位置参数
def f1(a,b,c):
    y = 3*a + 2*b + c
    return y

f1(10,20,30)
# f1(10,20,30,40)
# f1(10,20)

# 知识: 位置参数 定义了多少个,就必须传递多少个,不能多也不能少.而且是按照位置顺序传递值

# 2默认参数
def f2(a=0,b=0,c=0):
    y = 3*a + 2*b + c
    return y

f2(10)


# 知识:在定义函数时,给予参数一个初始值.保证有值可用

# 关键字传参
f2(b=10,c=20)


# 3关键字参数
def f3(**kwargs):
    print(kwargs)
    print(111)
    return 0

f3(b=10,c=20)

# 知识: 可以接受任意对 以关键字传参形式 传递的值

# 4可变参数
def f4(*args):
    print(args)

    return -1

f4()

# 知识: 可以任意个参数,在内部以元祖的形式存在



# 例1
# 函数名: myFilter
# 输入: int
# 输出: list
# myFilter(6) --> [0,2,4,6]
# 功能说明: 给定任意一个数字,可以获取到0-数字 之间所有的偶数

def myFilter(num:int):
    res = []
    for x in range(num+1):
        if x%2==0:
            res.append(x)
    return res

myFilter(10)

# 练习1:请定义一个函数,获取0-num之间的所有的奇数,默认是获取0-100之间的奇数
# 函数名: Filter2
# 输入: int or None
# 输出: list
# Filter2() --> 0-100之间的奇数
# Filter2(10) --> 0-10之间的奇数
def Filter2(num=100) -> list:
    """
    描述
    :param num:
    :return:
    """
    res=[]
    for x in range(num+1):
        if x%2 == 1:
            res.append(x)
    return res

Filter2()
Filter2(10)
Filter2(9)


def Filter2  (nums = 100):
    odds=[num for num in range(nums+1) if num % 2 != 0]
    return odds


# 匿名函数
Filter2 = lambda nums=100:[num for num in range(nums+1) if num % 2 != 0]
Filter2(10)

# 列表生成式(列表推导式)
# 例1:创建一个1-10的列表
l1 = [x for x in range(1,11)]
# 例2:请对以下列表计算平方
l2 = list('12345678')

l3 = [int(x)**2 for x in l2]

l4 = []
for x in l2:
    l4.append(int(x)**2)


# 三木运算符
a = 1
if a > 0:
    b = 100
else:
    b = 0


b = 100 if a > 0 else 0

# lambda函数
# 注意: 只能是简单函数的简写


# --------------------------------高级特性

# 1.重命名
def a(x):
    return 10

a(1)

a

b = a  # 重命名
b(100)

id(b)
id(a)

c = b
c(1000)


# 2.嵌套
for i in range(5):
    for j in range(10):
        print(i,j)


for i in range(5):
    if i%2==0:
        print(i)


def f1():
    name = '张三'
    def inner():
        print(name)

    inner()
    return 10

f1()



def f1():
    name = '张三'
    def inner():
        print(name)

    return inner # 返回一个函数包

f1()()



# 自身调用:递归

def f(x):
    if x<2:
        return 1
    return f(x-1) + f(x-2)

f(5)

# 斐波那契数列
for i in range(1,10):
    print(f(i))



# 函数:功能 function

# python自带的函数(内建函数
len()
print()
range()
user = input('账号:')
int(user)
str()


# 自定义函数
f()


# 案例1:
students = [{'name':'张三','class':'高一一班','score':629}]
# 把学生信息添加到列表中
def add():
    name = input('请输入姓名:')
    class_ = input('请输入班级:')
    score = input('请输入成绩:')
    s = {'name':name,'class':class_,'score':int(score)}
    students.append(s)

# 修改某位学生信息
def alter():
    n = input('请输入您要修改的学生姓名:')
    for s in students:
        if n==s['name']:
            k = input('请输入您要改变信息的关键字[name,class,score]:')
            v = input('请输入修改后的信息:')
            if k=='score':
                v = int(v)
            s[k] = v
            print('修改成功!')

# 删除某位学生信息
def delete():
    n = input('请输入您要删除的学生姓名:')
    sign = input(f'确实要删除<{n}>吗? [y/n]:')
    for s in students:
        if n==s['name'] and sign=='y':
            students.remove(s)
            print('删除成功')

# 查看全部学生信息
def query():
    for s in students:
        print(s)

# 按成绩输出学生信息
def sort():
    n = len(students)
    for i in range(1, n):
        for j in range(n - i):
            if students[j]['score'] > students[j + 1]['score']:
                students[j], students[j + 1] = students[j + 1], students[j]

sort()

add()

alter()

delete()

query()

# 练习1:
# 改bug: 成绩修改后并不是int  √
# 添功能: \
#     1.删除缺少确认步骤
#     2.按成绩排序输出信息


# 冒泡
score = [99,78,85,93,88]
n = len(score)
# 下标有限
for i in range(1,n):
    for j in range(n-i):
        if score[j] > score[j+1]:
            score[j],score[j + 1] = score[j+1],score[j]

print(score)


# 选择
score = [99,78,85,93,88]
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if score[j] < score[min_index]:
            min_index = j
    score[min_index],score[i] = score[i],score[min_index]





# 插入
score = [5,3,4,7,2]
for i in range(1,len(score)):
    key = score[i]
    j = i-1
    while j>=0 and key < score[j]:
        score[j+1] = score[j]
        j-=1
    score[j+1] = key


# 练习:把 选择 应用到 sort功能



# 交换值
a = 10
b = 20

c = a
a = b
b = c

a,b = b,a

a,b = 10,20




