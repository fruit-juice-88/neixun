import part6  # 导入part6这个文件,自动执行part6全部代码

S = part6.StuInfo()  # 只能通过创建对象,才能调用方法
S.run()

'C:/Users/admin/Desktop/学生信息.txt'

# 知识点1:文件属性
# print(__name__) # 当前文件的名字
# print(__doc__)
# print(__file__)
#
#
# print(part6.__name__) # 输出part6的文件名字
# print(part6.__doc__)
# print(part6.__file__)


# 知识点2: 类方法和装饰器


class A:
    # 对象方法
    def a(self):
        print('1111')

    # 类方法
    @classmethod
    def b(cls):
        print(2222)

    # 静态方法
    @staticmethod
    def c():
        print(3333)

# 通过对象调用
aa = A()
aa.a()
aa.b()
aa.c()

# 通过类名调用
# A.a()
A.b()
A.c()

