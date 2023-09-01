from flask import Flask

app = Flask(__name__)

home_page = """
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

@app.route('/<name>')
def index(name:str):
    return f'hello,{name}!'


@app.route('/stu')
def stu():
    return home_page


if __name__ == '__main__':
    app.run()

