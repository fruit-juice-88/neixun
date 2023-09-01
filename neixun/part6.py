"""
学生信息管理系统
1.添加学生信息
    添加1条
    批量添加
2.查询学生信息
    查询全部
    条件查询
    排序输出
3.修改
4.删除
    删除全部
    删除指定
    条件删除
0.启动,退出
"""
import pandas as pd
import numpy as np


class Stu:
    def __init__(self, name, class_, score):
        self.name = name
        self.class_ = class_
        self.score = score


class StuInfo:
    students = list()

    def add(self):
        print('-*--*--*--*--*--*--*--*--*--*--*-')
        print('            <添加页面>')
        print('-*--*--*--*--*--*--*--*--*--*--*-')

        name = input('请输入姓名:')
        class_ = input('请输入班级:')
        score = int(input('请输入成绩:'))
        self.students.append(Stu(name, class_, score))
        print('添加成功')

    def batch_add(self):
        path = input('请输入本地文件的路径:')
        content = pd.read_csv(path, sep=' ', names=['姓名', '班级', '成绩'])
        content = np.array(content).tolist()
        for s in content:
            self.students.append(Stu(s[0],
                                     s[1],
                                     s[2]))
        print('添加成功')

    def query(self):
        for s in self.students:
            print(s.name, s.class_, s.score)

    def condition_query(self):
        condition = input('请输入查询条件(score > 500):').split(' ')

        if condition[0] == 'score':
            for s in self.students:
                if condition[1] == '>' and s.score > int(condition[-1]):
                    print(s.name, s.class_, s.score)
                elif condition[1] == '<' and s.score < int(condition[-1]):
                    print(s.name, s.class_, s.score)
                elif condition[1] == '=' and s.score == int(condition[-1]):
                    print(s.name, s.class_, s.score)
        elif condition[0] == 'class_':
            for s in self.students:
                if condition[1] == '=' and s.class_ == condition[-1]:
                    print(s.name, s.class_, s.score)
        elif condition[0] == 'name':
            for s in self.students:
                if condition[1] == '=' and s.name == condition[-1]:
                    print(s.name, s.class_, s.score)
        else:
            print('输入有误!')

    def sort_data(self):
        for i in range(1, len(self.students)):
            key = self.students[i]
            j = i - 1
            while j >= 0 and key.score < self.students[j].score:
                self.students[j + 1] = self.students[j]
                j -= 1
            self.students[j + 1] = key
        print('排名完成!')
        self.query()

    def update(self):
        n = input('请输入您要修改的学生姓名:')
        for s in self.students:
            if n == s.name:
                k = input('请输入您要改变信息的关键字[name,class,score]:')
                v = input('请输入修改后的信息:')
                if k == 'name':
                    s.name = v
                elif k == 'class':
                    s.class_ = v
                elif k == 'score':
                    s.score = int(v)
                else:
                    print('输入有误!')
                print('修改成功!')

    def del_all(self):
        status = input('您确实要删除全部信息吗? [y/n] : ').lower()
        if status == 'y':
            self.students.clear()

    def del_one(self):
        n = input('请输入您要删除的学生姓名:')
        status = input(f'您确实要删除<{n}>的信息吗? [y/n] : ').lower()
        if status == 'y':
            for s in self.students:
                if s.name == n:
                    self.students.remove(s)
                    print('删除成功')
                    break

    def del_if(self):
        condition = input('请输入删除条件(score > 500):').split(' ')

        if condition[0] == 'score':
            for s in self.students:
                if condition[1] == '>' and s.score > int(condition[-1]):
                    self.students.remove(s)
                elif condition[1] == '<' and s.score < int(condition[-1]):
                    self.students.remove(s)
                elif condition[1] == '=' and s.score == int(condition[-1]):
                    self.students.remove(s)
        elif condition[0] == 'class_':
            for s in self.students:
                if condition[1] == '=' and s.class_ == condition[-1]:
                    self.students.remove(s)
        elif condition[0] == 'name':
            for s in self.students:
                if condition[1] == '=' and s.name == condition[-1]:
                    self.students.remove(s)
        else:
            print('输入有误!')

    def run(self):
        home_page = """
        ===============================================
                          学生信息管理系统
        ===============================================
                         1. 添加信息
                         2. 批量添加
                         3. 查询信息
                         4. 条件查询
                         5. 排名信息
                         6. 修改信息
                         7. 清空信息
                         8. 删除单条
                         9. 条件删除
                         0. 退出
        ================================================
        """
        print(home_page)
        while True:
            select = input('请输入您的选择: ')
            while select not in '0123456789':
                select = input('输入有误. 请重新输入您的选择: ')
            if select == '0':
                break
            d = {
                '1': self.add,
                '2': self.batch_add,
                '3': self.query,
                '4': self.condition_query,
                '5': self.sort_data,
                '6': self.update,
                '7': self.del_all,
                '8': self.del_one,
                '9': self.del_if
            }
            d[select]()


if __name__ == '__main__':
    print('----end ! part6')



# 有一段代码,想要在part6执行时执行
# 但是如果是其他文件引入part6时,不让这段代码