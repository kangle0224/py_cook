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


# # 4.创建大量对象时节省内存的方法
# # __slots__,适用于简单的数据结构
# class Date:
#     __slots__ = ['year', 'month', 'day']
#
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day

# 5.property
# 用途：
# 1.在对象进行改变值之前进行类型检查
# 2.进行计算
# class Person(object):
#     def __init__(self, first_name):
#         self.first_name = first_name  # 将变量私有化，这样即使是子类也不能访问；这里的变量必须和下面的方法名不一致，否则会出现循环
#
#     @property
#     def name(self):
#         return self.first_name
#
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string.')
#         self.first_name = value
#
#     @name.deleter
#     def name(self):
#         raise AttributeError('Can not delete attribute.')
#
#     @property
#     def get_sum(self):
#         return 1 + 2
#
#
# a = Person('Guido')
# print(a.name)
# print(a.get_sum)
# a.name = 43
# del a.name


# 6. 创建新的类或实例属性
# 类型检查
# 描述器，这个很重要，可以实现@classmethod,@staticmethod,@property,__slots___
# 当程序中有很多重复代码的时候描述器就很有用了
# class Integer:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise TypeError('Expected an int')
#         instance.__dict__[self.name] = value
#
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
#
#
# class Point:
#     x = Integer('x')
#     y = Integer('y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p = Point(2, 3)
# print(p.x)
# print(p.y)
# print(Point.x) #<__main__.Integer object at 0x00000117E5014460>
# p.y = 5
# print(p.y)
# p.x = 2.3  # 报错，会进行类型检查

# 7. 使用延迟计算属性
# 你想将一个只读属性定义成一个 property，并且只在访问的时候才会计算结果。但
# 是一旦被访问后，你希望结果值被缓存起来，不用每次都去计算。
# 7.1这个版本会被更改
# class lazyproperty:
#     def __init__(self, func):
#         self.func = func
#
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             value = self.func(instance)
#             setattr(instance, self.func.__name__, value)  # 将计算结果存储在实例的字典中，以后不需要计算了
#             return value
#
#
# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @lazyproperty
#     def area(self):
#         print('computing area')
#         return math.pi * self.radius ** 2
#
#     @lazyproperty
#     def perimeter(self):
#         print('computing perimeter')
#         return 2 * math.pi * self.radius
#
#
# c = Circle(4)
# print(c.radius)
# print(c.area)
# print(c.area)  # 不打印computing...
# print(c.perimeter)
# print(c.perimeter)  # 不打印computing...
# # 结果被更改
# c.area = 4
# print(c.area)

# 7.2不会被更改，但不高效了
# def lazyproperty(func):
#     name = '_lazy_' + func.__name__
#
#     @property
#     def lazy(self):
#         if hasattr(self, name):
#             return getattr(self, name)
#         else:
#             value = func(self)
#             setattr(self, name, value)
#             return value
#
#     return lazy
#
#
# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @lazyproperty
#     def area(self):
#         print('computing area')
#         return math.pi * self.radius ** 2
#
#     @lazyproperty
#     def perimeter(self):
#         print('computing perimeter')
#         return 2 * math.pi * self.radius
#
#
# c = Circle(4)
# print(c.area)
# print(c.area)
# print(c.perimeter)
# print(c.perimeter)
# c.area = 5  # 报错了，不允许修改，但这种方法也有缺点，具体看书


# 8.简化数据结构的初始化
# 不用写那么多行的初始化定义了
# 先定义基类
import math


# class BaseStruct:
#     _fields = []
#
#     def __init__(self, *args):
#         if len(args) != len(self._fields):
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value)
#
#
# class Stock(BaseStruct):
#     _fields = ['name', 'shares', 'price']
#
#
# class Point(BaseStruct):
#     _fields = ['x', 'y']
#
#
# class Circle(BaseStruct):
#     _fields = ['radius']
#
#
# s = Stock('alex', 50, 91)
# p = Point(2, 3)
# c = Circle(5)
# c = Circle(5, 6) # 报错，参数多了

# 关键字参数
# class BaseStruct:
#     _fields = []
#
#     def __init__(self, *args, **kwargs):
#         if len(args) > len(self._fields):
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#         # 处理所有的位置参数
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value)
#         # 处理关键字参数
#         print(self._fields[len(args):])
#         for name in self._fields[len(args):]:
#             setattr(self, name, kwargs.pop(name))
#
#         # 检查其他参数
#         if kwargs:
#             raise TypeError('Invalid arguments: {}'.format(','.join(kwargs)))
#
#
# class Stock1(BaseStruct):
#     _fields = ['name', 'shares', 'price']
#
#
# s1 = Stock1('alex', 4, 5)
# s2 = Stock1('alex', 4, price=26)
# s3 = Stock1('alex', shares=4, price=26)
# s4 = Stock1('alex', 5, shares=4, price=26)  # 此处会随机报shares或者price，因为字典是乱序的

# 将不再_fields中的名称加入到属性中
# class Structure3:
#     _fields = []
#
#     def __init__(self, *args, **kwargs):
#         if len(args) != len(self._fields):
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value)
#
#         extra_args = kwargs.keys() - self._fields
#         for name in extra_args:
#             setattr(self, name, kwargs.pop(name))
#         if kwargs:
#             raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))
#
#
# class Stock(Structure3):
#     _fields = ['name', 'shares', 'price']
#
#
# s1 = Stock('alex', 4, 5)
# s2 = Stock('alex', 4, 5, date='2020/9/11')
# print(s2.__dict__)
