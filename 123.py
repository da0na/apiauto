# coding:utf-8


# class Test:
#     def prt(self):
#         # self代表 类的实例
#         print(self)
#         # self.class 指向类
#         print(self.__class__)
#
#
# t = Test()
# t.prt()

# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.score = score
#
#     def print_score(self):
#         print("%s: %s" % (self.__name, self.score))
#
#
# student = Student("Hugh", 99)
# student.print_score()
# print(student.score)
# print(student.__name)

#
# class Parent:
#     def pprt(self):
#         print(self)
#
#
# class Child(Parent):
#     def cprt(self):
#         print(self)
#
#
# c = Child()
# c.cprt() # child
# c.pprt() # child
# p = Parent()
# p.pprt() # parent
#


# class Desc:
#     def __get__(self, ins, cls):
#         print('self in Desc: %s' % self)
#         print(self, ins, cls)
#
#
# class Test:
#     x = Desc()
#
#     def prt(self):
#         print('self in Test: %s ' % self)
#
#
# t = Test()
# t.prt()
# # t.x
#
# a = 1
# def demo():
#     x = 100
#     global b
#     b = 2
#
#     print(globals())
#     print(locals())
#
#     globals()['a'] = 'modified a'
#     globals()['b'] = 'modified b'
#     globals()['c'] = 'new c'
#     locals()['x'] = 'modified x'
#     locals()['y'] = 'new y'
#     globals().pop('c')
#     locals().pop('x')
#
#     print(globals())
#     print(locals())
#
#
# def print_b():
#     try:
#         print(b)
#     except NameError as e:
#         print(e)
#
# def print_x():
#     try:
#         print(x)
#     except NameError as e:
#         print(e)
#
#
# print_b()
# demo()
# print_x()
# print_b()

# import mock
# # print(mock.Mock())
# # print(dir(mock.Mock()))
# a = mock.Mock(name='name_1')
# print(a)
# # return_value指定的是某个值
# b = mock.Mock(name='name_3', return_value=100)
# print(b, "+++>", type(b))
# print(b(), "--->",type(b()))
import unittest

#
# # return_value指定的是类的实例
# class Person(object):
#     arg_0 = 5
#
#     def __init__(self):
#         self.arg_1 = 10
#         pass
#
#     def add(self):
#         return 20
#
#
# p = Person()
# mock_obj = mock.Mock(return_value=p)
# a = mock_obj()
# # mock_obj = mock.Mock()只是返回一个mock实例
# # 要他的返回值时 a = mock_obj() , a就是return_value
# print("a:", a)
# print("a.add", a.add())
# print("a.arg_1:", a.arg_1)
# print("a.arg_0:", a.arg_0)
#
# import mock
# import unittest
# mock_object = mock.Mock(return_value=10, side_effect=StandardError)
# b = mock_object()
#
# # mock一个函数
# import unittest
# import mock
#
#
# # def multiple(a, b):
# #     return a+b
#
#
# class TestProducer(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def test_multiple(self):
#         multiple = mock.Mock(return_value=3)
#         self.assertEqual(multiple(8, 14), 3)
#         # self.assertEqual(multiple(), 3)
#
#
# if __name__ == "__main__":
#     unittest.main()


# 另一种方法是mock.patch
# import unittest
# import mock
#
#
# class Calculator(object):
#     def add(self, a, b):
#         return a+b
#
# def multiple(a, b):
#     return a*b
#
# class TestProducer(unittest.TestCase):
#     def setUp(self):
#         self.calculator = Calculator()
#     # mock.patch('multiple')一定
#     # mock_multiple 是不是可以随时命名？
#     @mock.patch('multiple')
#     def test_multiple(self, mock_multiple):
#         mock_multiple.return_value = 3
#         self.assertEqual(multiple(8, 14), 3)
#
#
# if __name__ == "__main__":
#     unittest.main()
#
#
# import flask, json
#
# # 创建接口后台服务，方便请求接口
# server = flask.Flask(__name__) # 把app.py文件当作一个server
#
# # 装饰器，将get_all_user()函数编程一个接口 127.0.0.1:9000/get_user
# @server.route('/get_user', methods=['get', 'post'])
# def get_all_user():
#     all_user = [
#         {'id': 1, 'sex': 1, 'real_name': '小花'},
#         {'id': 2, 'sex': 0, 'real_name': '小明'},
#         {'id': 3, 'sex': 0, 'real_name': '小黑'}
#     ]
#     res = json.dumps(all_user, ensure_ascii=False) # 将list转换为json串，ensure_ascii为False时，可以包含non-ASCII字符
#     return res
#
# # 启动服务，debug=True表示修改代码后自动重启；
# # 启动服务后接口才能访问，端口号为9000，默认ip为127.0.0.1
# server.run(port=9000, debug=True)
import requests

# 请求地址
url = "http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?char=11"
# 发送get请求
r = requests.get(url).json()
# 获取返回的json数据

print(r)

