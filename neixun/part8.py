# 知识点1---
# 模块,包,库
# 模块是python团队创建的插件.可以使你在程序中快速拥有某个扩展功能
# 不重复造轮子.

# 需求:把多维列表的字符串 变为 列表
# a = "[['张三',30,20],['张三',30,20]]"
# # 自己写
# a.replace('[','').replace(']','').replace('\'','').split(',')
#
# import ast
# # 调包
# list_a = ast.literal_eval(a)


# 知识点2---
# 关于包常用指令
# pip list
# pip show 包
# pip install 包
# pip install 包==版本号
# pip uninstall 包
# pip install 包 -i 数据源url
# pip install 包 -i 数据源url --user


import faker  # 导入整个文件
fake = faker.Faker()
fake.name()


from faker import Faker # 导入文件中的某个类
fake = Faker()
fake.name()


import faker as f # 设置别名
fake = f.Faker(locale='zh_CN')
for _ in range(10):
    print(fake.text())





