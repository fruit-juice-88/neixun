# 练习题:
# 1.请把你手机的相关信息(型号,品牌,价格,内存,芯片)存储到python中
model = 'RedmiK40S'
brand = 'Redmi'
price = 4000
memory = 128
chip = 'gaotongxiaolong870'

# ------------------------------------------------------
# 数据容器(数据结构)
# 数据容器: 一组数据的集合,为了更高效的存取数据
# []  list  列表
# ()  tuple 元组
# {}  set  集合
# {k:v} dict 字典

# ----------------------创建
# 创建列表
a = 1
l1 = []
l2 = [1,2,3,4,5]
l3 = ['zs','ls','ww','zl']
l4 = [3.4,3.5,23.6]
l5 = [True,False,True]
l6 = ['张三',20,180,130.5,'北京市海淀区',True]

# 创建元祖
t1 = ()
t2 = (1,2,3,4,5)
t3 = ('zs','ls','ww','zl')
t4 = (3.4,3.5,23.6)
t5 = (True,False,True)
t6 = ('张三',20,180,130.5,'北京市海淀区',True)

# 创建集合
s1 = {} # 字典
s2 = {1,2,3,4,5}
s3 = {'zs','ls','ww','zl'}
s4 = {3.4,3.5,23.6}
s5 = {True,False,True}
s6 = {'张三',20,180,130.5,'北京市海淀区',True}

# 创建字典
d1 = {}
d2 = {1:'a',2:'b',3:'c'}
d3 = {'a':100,'b':200,'c':300}
d4 = {'model': 'RedmiK40S',
      'brand': 'Redmi',
      'price': 4000,
      'memory': 128,
      'chip': 'gaotongxiaolong870'}
# 自定义下标: 自己定义关键字与值
# 创建较复杂,使用很简单



# ----------------------使用
# 索引,切片
# 增删改查

# ***列表
# 查
l6[1]
l6[-2]
l6[1:4]
l6.index(120)
l6[2]
# 增
l6.insert(0,'张无忌')
l6.append('河北省雄安新区')
# 删
l6.remove('张三')
a = l6.pop(1)
# 改
l6[2] = 120

# ***字典
# 索引,没有切片
d4['price']
# d4['price':'memory']
# 添加
d4['used_time'] = 365
# 修改
d4['memory'] = 256
# 删除
d4.pop('chip')
# 查询
d4.keys()
d4.values()
d4.items()

# ***元祖
# 特点: 不可改变
l1 = [1,2,3,4,5]
t1 = (1,2,3,4,5)

l1.append(20)  # 自身可变

t1 = t1 + (10,)  # 对t1的重新赋值;
# 一个元素的元祖, (值,)
a = (10)
b = (10,)

# 索引,切片
t1[2:4]
t1[1]
t1[-1]


# 1.知识点:可变与不可变,内存地址id()
# 不可变: 数字,字符串,元祖
# 可变: 列表,集合,字典
a = 10
id(a) # 140715392763840
a = a + 1
id(a) # 140715392763872

a = 1
a = 2

l1 = [1,2,3]
id(l1)  # 1651359621824
l1.append(40)
id(l1) # 1651359621824


# ***集合
# 特点: 唯一性,没有索引和切片,无序
s1 = {1,2,3,4,5,6,7,2,3,5}

# 添加
s1.add(100)
# 删除
s1.remove(5)
s1.pop()
# 修改
s1.update({1,20,300})
# 运算
s1 = {1,2,3,4}
s2 = {3,4,5,6,7}
s1 & s2
s1 | s2
s1 - s2


# 数据类型
# int()      9
# float()    9.0
# bool()     True
# str()      ' '
# list()     []      可变
# tuple()    ()
# set()      {}      可变
# dict()     {k:v}   可变

# 基本操作
s1 = 'abcdefg'
list(s1)
tuple(s1)
str(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
''.join(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
''.join(('a', 'b', 'c', 'd', 'e', 'f', 'g'))


# 练习题:
# 创建一个列表,包含中国五岳山峰
#       添加一个 自己家乡的山
#       删除第一个山峰
#       查询出第2个到第4个
#       查询出最后一个
#       修改第一个为 泰山
# 创建一个元祖,包含中国的三大河流
#       查询出第一个元素
#       查询出最后一个元素
# 创建一个字典,包含你朋友的相关信息(姓名,性别,身高,体重,爱好)
#       添加一组信息 成绩=90
#       删除 体重
#       修改 身高 = 当前值 + 10

mount = ['泰山','华山','衡山','嵩山','恒山']
mount.append('寿山')
mount.insert(1,'香山')
mount.pop(0)
mount.remove('泰山')
print(mount[1:3])
print(mount[-1])
mount[0] = '泰山'

river = ('长江','黄河','珠江')
print(river[0])
print(river[-1])

friend = {'name': '张三',
          'sex': '男',
          'height': 180,
          'weight': 130,
          'hobby': '轮滑'}
friend.pop('weight')
friend['height'] += 10
friend['height'] = friend['height'] + 10
friend['score'] = 90

a = 10
a = a + 1
a += 1


# 字符串
text = '据塔斯社8月22日报道，莫斯科所有机场关闭，禁止进出航班。据中新网报道，当地时间21日，美国驻白俄罗斯大使馆在一份声明中表示，美国方面在警告中提醒本国公民不要前往白俄罗斯，敦促仍在白俄罗斯的美国人立即离开该国。目前，美国务院对赴白俄罗斯的旅行建议为最高级别4级，即 “请勿前往”。声明称，立陶宛政府于18日关闭了两个与白俄罗斯间的边境口岸。波兰、立陶宛和拉脱维亚政府表示，有可能进一步关闭与白俄罗斯的边境口岸'

# 把 莫斯科 替换为 俄罗斯
text.replace('莫斯科','俄罗斯')
# 请按照 , 分割这段文本
text.split('，')
# 提取出 8月22日
text[4:9]
# 提取出 边境口岸
text[-4:]
# 反转字符串
text[::-1]
# 隔一个取一个
text[::2]
# 请让每一句话独占一行
print(text.replace('。','\n'))
print(text.replace('。','\n').replace('，','\n')) # 链式操作


# ------------------多维数据结构-----------------
# list 列表
# dict 字典
# tuple 元祖

l1 = [1,2,3]
l2 = [[1,2,3],
      [4,5,6]]

l2[1][1]

l3 = [(1,2,3),
      (4,5,6)]

l3[1][0]

l4 = [{'name': '张三',
       'sex': '男',
       'height': 180,
       'weight': 130,
       'hobby': '轮滑'},
      {'name': '李四',
       'sex': '男',
       'height': 181,
       'weight': 131,
       'hobby': '篮球'}
      ]

l4[0]['hobby']


l5 = [{'name': '张三',
       'sex': '男',
       'height': 180,
       'weight': 130,
       'hobby': '轮滑'},
      {'name': '李四',
       'sex': '男',
       'height': 181,
       'weight': 131,
       'hobby': ['篮球','唱','跳','rap']}
      ]

# 查询
l5[1]['hobby'][1]
# 修改
l5[1]['height'] += 3

# 注意: 一定要确定好,你取出的数据是什么数据类型
# 因为不同的类型有不同的操作

l5[1]['weight'][1]

l5[1]['name'][0]

# '李四'[0]


# 练习1
# 1.读取本地文件
f = open(r'C:\Users\admin\Desktop\today_news.txt','r',encoding='utf-8')
content = f.read()

# 2.把字符串转为多维数据结构
import json
new_content = json.loads(content)

# 3.检索
new_content['data'][1]['Title']

# 4.关闭文件
f.close()