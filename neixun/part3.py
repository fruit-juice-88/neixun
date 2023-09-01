"""控制语句"""
# 目的: 控制程序的执行顺序

"""循环"""
# 目的:反复执行一段程序. 次数?(由可迭代对象的长度) 5 死循环
# 确定两个必要问题
# 1.次数
# 2.程序
# 格式:
# for 临时变量 in 可迭代对象(字符串,列表,元祖,字典):
#     程序
for _ in '1abcdf1':
    print(1)

for x in [1, 2, 3]:
    print(x)

for x in (1, 2, 3):
    print(x)

d1 = {'a': 100, 'b': 200}
for x in d1:
    print(x, d1[x])

d1.items()
for x in [('a', 100), ('b', 200)]:
    print(x)

for x in d1.items():
    print(x)

# for循环的双层解析
for k, v in [('a', 100), ('b', 200)]:
    print(f'k={k}   v={v}')

a, b = (10, 20)

# 问题1: 假如我要循环1000次?
# 使用range()函数,快速生成一组数
# range(起始,结束,步长)
count = 0
for x in '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111':
    print(x)
    count += 1
print(count)

list(range(100))
list(range(50, 100))
list(range(50, 100, 20))

for x in range(10000):
    print(1)

# 格式:
# while 条件:
#   代码
a = 10
while a > 0:
    print(a)
    a -= 1

"""判断"""
# 目的: 根据环境感知,执行不同的程序
# 两个必要问题
# 1.条件?
# 2.程序?

# 例1:请创建一个程序,用来判断成绩是否及格?
score = 99
if score >= 60:
    print('恭喜你,及格')
    money = 1000
    print('出国游')
else:
    print('很遗憾,没及格')
    print('下次继续努力!')

# 例2:请创建一个程序,用来判断成绩能上什么学校?
score = 643
if score > 620:
    print('恭喜你,可以上985')
    money = 50000
elif score > 590:
    print('恭喜你,可以上211')
    money = 30000
elif score > 550:
    print('恭喜你,可以上本一')
    money = 10000
elif score > 500:
    print('恭喜你,可以上本二')
    money = 5000
else:
    print('很遗憾')
    money = 0

# 综合案例1:
# 1.请循环打印1-100.
for i in range(1, 101):
    print(i)

# 2.请循环打印1-100.(while实现)
i = 1
while i <= 100:
    print(i)
    i += 1

# 3.请循环打印1-100中3的倍数
for i in range(1, 101):
    if i % 3 == 0:
        print(i)

# 4.请读取出所有的新闻标题
# 1.读取本地文件
f = open(r'C:\Users\admin\Desktop\today_news.txt', 'r', encoding='utf-8')
content = f.read()

# 2.把字符串转为多维数据结构
import json

new_content = json.loads(content)

# 3.检索
for news in new_content['data']:
    if news['Label'] == 'new':
        print(news['Title'], news['LabelDesc'])

# 4.关闭文件
f.close()

# 练习1: 请把下面字典中的成绩,修改为A,B,C (使用循环,判断实现
# 大于90: A
# 大于75: B
# 大于60: C
grade = {'小张': 99, '小李': 88, '小明': 66, '小赵': 55}
for k in grade:
    if grade[k] > 90:
        grade[k] = 'A'
    elif grade[k] > 75:
        grade[k] = 'B'
    elif grade[k] > 60:
        grade[k] = 'C'
    else:
        grade[k] = 'D'


# 练习2: 现在老师只想统计及格分数的平均分，把<60的分数剔除掉
L = [75, 98, 59, 81, 66, 43, 69, 86]
for score in L:
    if score < 60:
        L.remove(score)
print(L)

L = [75, 98, 59, 81, 66, 43, 69, 86]
right = []
for score in L:
    if score >= 60:
        right.append(score)
print(right)


# 练习3:
names = ['Thomas Williams',
         'susan osborn',
         'megan Scott',
         'Lisa harris',
         'Roger Soto',
         'elizabeth becker',
         'Dale Foley',
         'Jack Brown',
         'James Erickson',
         'Ashley Zimmerman']

# 请把列表中的每个名字,标准化(首字母大写)
# names[1].title()
for name in names:
    print(name.title())
print(names)

# 找出上述 名(first name) 中长度大于4的名字,打印出来.
for name in names:
    first_name = name.split(' ')[0]
    count = 0
    for s in first_name:
        count += 1
    if count > 4:
        print(name)

# 知识点: len() 返回对象的长度, 内建函数
len('asdjkh')
len([1,2,3])

for name in names:
    first_name = name.split(' ')[0]
    if len(first_name) > 4:
        print(name)

# 知识点: 自定义函数
# 格式:
# def 名称(自变量):
#     return 因变量

def myLen(obj):
    count = 0
    for _ in obj:
        count += 1
    return count

myLen('asdb')


def f(x):
    return x+1
y = f(10)

f = lambda x:x+1
y = f(1)

# 编程语言:语法,规则.创始人指定

for name in names:
    first_name = name.split(' ')[0]
    if myLen(first_name) > 4:
        print(name)


# 请循环把名字 姓氏 改为 字典  'Thomas Williams' --> {'first_name':'Thomas','last_name':'Williams'}
for name in names:
    # name:'Roger Soto' 使用split分割 结果['Roger','Soto'] 最终 使用索引 取出第0个元素'Roger'
    first_name = name.split(' ')[0]
    # 使用索引 取出第1个元素'Soto'
    last_name = name.split(' ')[1]
    d = {'first_name': first_name, 'last_name': last_name}
    print(d)

# 掌握语法后的第一件事
# 实现想法
# 熟能生巧
