# -*- coding: utf-8 -*-

from flask import Flask, escape, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello,world!'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)

@app.route('/test')
def test_url_for():
    #下面是调用一些示例（请在命令行窗口查看输出的URL）
    print(url_for('hello')) #输出：/
    #注意下面两个调用是如何生成包含URL变量的URL的
    print(url_for('user_page', name = 'greyli'))
    print(url_for('user_page', name = 'Peter'))
    print(url_for('test_url_for'))
    #下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到URL后面
    print(url_for('test_url_for', num = 2))
    return 'Test page'


if __name__ == '__main__':
     app.run()
