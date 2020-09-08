#!/usr/bin/env python
# coding: utf-8

# # 1.改变对象的字符串显示
# class Pair:
#     """
#     __repre__是实例化类的，给程序员排错用的，
#     __str__是给用户看的
#     """
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return "pair{0.x!r}, {0.y!r}".format(self)
#
#     def __str__(self):
#         return "pair{0.x!s}, {0.y!s}".format(self)
#
#
# # 2.自定义字符串的格式化
# _formats = {
#     'ymd': '{d.year}-{d.month}-{d.day}',
#     'mdy': '{d.month}/{d.day}/{d.year}',
#     'dmy': '{d.day}/{d.month}/{d.year}'
# }
#
#
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def __format__(self, code):
#         if code == '':
#             code = 'ymd'
#         fmt = _formats[code]
#         return fmt.format(d=self)
#
#
# d = Date(2020, 01, 12)
# print format(d)
# print format(d, 'mdy')
# print format(d, 'dmy')
# print "the date is {:ymd}".format(d)
# print "the date is {:mdy}".format(d)


# 3.让对象支持上下文管理协议
# 类需要支持__enter__(),__exit__()方法，这时__init__()方法只是进行初始化


# 4.创建大量对象时节省内存的方法
# __slots__,适用于简单的数据结构
class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
