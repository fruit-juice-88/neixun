1+1

# 张三
# 注释:解释说明,不是python代码,也不参与运行

# --------------变量的基本操作--------------
# 创建变量
# 格式: 变量名 = 值
x = 10
y = 5.4
z = 4/5
q = 'qwe'
name = '张三'

# 变量的类型
# 小数
# 整数
# 文本
# 布尔值(True  False)

1>10
False


# 目的:
# 如何把生活的数据传递给python(或者传递给电脑)
# 只有把数据传递给电脑-->计算,存储


# 使用变量
# 数字(小数,整数)
# 文本(string 字符串

# ------------字符串------------
# 注意: 文本可以包含一切
name + q  # 拼接
name * 10 # 重复
name.replace('三','3') # 替换

# ------------数字------------
# +  -  *  /  **  %   //
100 + 10
100 - 10
100 * 10
100 / 10
2 ** 3
123 % 100  # 取余
123 // 100  # 取整

# ------------浮点数------------
# 精度非常高的数据类型
9.8 + 0.3  # 溢出
10.1 - 0.8
9.2 ** 2

# 更多符号,同上

# ------------布尔值------------
# 乔治-布尔
True # 真
False # 假
# 目的: 帮助电脑做逻辑运算(and  or  not) 与或非
# 逻辑运算的目的: 让电脑拥有判断的能力

# 比较运算符 > < >= <= == != (针对数
# 判断运算符 in  ; not in  (针对文本
asdkjash = 9 > 8

10>6
'张三' != '李四'
'a' not in 'abcd'


True and True
True or False
not True


# 删除变量
del q


# ---------------变量的高级操作-----------------
"""
str : 字符串
int : 整数
float: 浮点数
bool : 布尔值
"""

# 类型转换
int() # 转换为整数
str() # 转换为文本
float() # 转换为小数
bool() # 转换为布尔值

asdkjash = 10
asdkjash = str(asdkjash)
asdkjash = int(asdkjash)
asdkjash = float(asdkjash)
asdkjash = bool(asdkjash)

b = '张三'
b = bool(b)

c = '101'
c = int(c)
c = float(c)

d = '9.8'
d = float(d)
d = int(d)

d = int(float(d)) # 简写

# 创建简写
asdkjash = 1
b = 2
c = 3

asdkjash, b, c = 1, 2, 3

asdkjash = 10
b = 10
c = 10

asdkjash = b = c = 10


# 快捷键
# ctrl + /  快速注释
# ctrl + D  向下复制粘贴
# shift + alt + e  选择执行

# 概念
# 运行顺序: 由上到下,由左到右

# --------------------------------------------------------

# 如何把数据存储到python中?
# 变量

# int 数字 直接写
# float
# str 文本加 ''
# bool 不自己创建,是比较的结果

# 基本操作
# 创建

asdkjash = 10
b = '注释'

# 使用
# 算术运算符 + - * / % //
# 比较运算符 > < >= <= == !=
# 逻辑运算符 not or and
# 成员运算符 in ; not in
# 赋值运算符 =

text = '工具:Excel (简单数据库 (取数,计算python (编程语言,R业务知识:业务统计学行业业务(电商,互联网,游戏,保险,金融,财会)'
# 如何存储多行文本信息?

# 输出 变量值
print(text)

# 字符串的所有的操作

# 1.字符串的种类
# 单行字符串 ' '  or   " "
# 多行字符串 ''' '''  or """ """
text = "工具:Excel (简单数据库 (取数,计算python (编程语言,R业务知识:业务统计学行业业务(电商,互联网,游戏,保险,金融,财会)"

text1 = '''
工具:
Excel (简单
数据库 (取数,计算
python (编程语言,R

业务知识:
业务统计学
行业业务(电商,互联网,游戏,保险,金融,财会)
'''
print(text)
print(text1)

# 2.字符串中 转义符
# \n  换行
# \t  制表符
# \r  回退
text2 = '张\三\r李四n'
print(text2)


# 3.字符串的 格式化
# 格式化字符
# %d  digit  数字
# %f  float  浮点数 默认保留小数点后6位  %.1f 保留1位小数
# %s  string 文本
name = '张三'
age = 20
score = 98.5

mode = "你好,我叫%s,我今年%d岁,我考试成绩%.2f分"  # 模板

mode%(30,3.1415,score)


# 4.字符串的索引和切片
text = "工具:Excel (简单数据库 (取数,计算python (编程语言,R业务知识:业务统计学行业业务(电商,互联网,游戏,保险,金融,财会)"
print(text)
text1 = '奥斯卡还记得光华科技'
print(text1)
# 索引:下标,字符的标号.从0开始
# 格式: 变量名[下标]
# 正向索引:从0开始
# 反向索引:从-1开始
text[3] # 'E'
text[10]
text1[6]
text1[-4]

# 切片:截取子串substring [左闭右开)
# 格式: 变量名[起始位置:结束位置:步长]
text[3:8]
text[10:15]
text[10:15:2]
# 简写
text[:8]
text[8:]
text[3:8]
# 其他
text[:]
text[::2]
text[::-1]


# -----------------简写
# 格式化简写
name = '张三'
age = 20
score = 98.5

mode = f"你好,我叫{name},\n我今年{age}岁,\n我考试成绩{score}分"
print(mode)

# 取消转义
text2 = r'张\三\n李四n' # 原始字符串
print(text2)

# 叠加
mode = rf"你好,我叫{name},\n我今年{age}岁,\n我考试成绩{score}分"
print(mode)

# ---------------------------------------------------
# 字符串的方法
# 操作
# 判断
text = '张三,李四,王五,赵六'
text.replace(',','--')
text.center(30,'-')
text.split(',')
'wer'.join(['张三', '李四', '王五', '赵六'])
text.index('李四')
text.find('王六')

asdkjash = 'hello lilei'
asdkjash.title()
asdkjash.lower()
asdkjash.upper()
asdkjash.zfill(20)
asdkjash = '000010'
asdkjash.count('l')


# -------------------
'abc'.isalpha() # 是否全为字母
'10.0'.isdigit() # 是否全为数字
'abcD'.islower() # 是否全为小写
'abcD'.isupper() # 是否全为大写
'Ab'.istitle() # 是否首字母大学
'2.0'.isdecimal() # 是否是十进制的数
'张三'.startswith('张') # 是否以..开头
'张三李'.endswith('李') # 是否以..结尾


# -------------------
# 编码格式
# ASCII 美国
# utf-8 通用
# gbk   中国

'张三'.encode('utf-8')
b'\xe5\xbc\xa0\xe4\xb8\x89'.decode('utf-8')
'寮犱笁'


# 变量命名
# 在练习阶段,当然越简单越好
# 脚本编写阶段,见名知意,标准化
age = 90
年龄 = 90
# utf-8 支持中文

# 变量名 是对 保存值的 一个描述
# 颜值为8
Face_value = 8  # 下划线命名法
FaceValue = 8  # 驼峰命名法
facevalue = 8
