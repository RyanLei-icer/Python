# def mul(a, *numbers):
#     s = a
#     if len(numbers) == 0:
#         s = a
#         return s
#     for n in numbers:
#         s = s * n
#     return s

# def mul(x, *args):
#     for i in args:
#         x = x * i
#     return x
#
# # 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#     print('测试失败!')
# elif mul(5, 6) != 30:
#     print('测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         mul()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')
#
#
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#         return
#     move(n - 1, a, c, b)
#     print(a, '-->', c)
#     move(n - 1, b, a, c)
#
#
# move(10, 'A', 'B', 'C')

# def findMinAndMax(L):
#     x = None
#     y = None
#     for i in L:
#         if i == min(L):
#             x = i
#         if i == max(L):
#             y = i
#
#     return x, y
#
#
# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

# import os  # 导入os模块，模块的概念后面讲到
#
# L = []
# L = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
# print(L)

# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# for k, v in d.items():
#     print(k, '=', v)

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [L2.lower() for L2 in L1 if isinstance(L2, str)]
#
# # 测试:
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')

# def fib(max_number):
#     n, a, b = 0, 0, 1
#     while n < max_number:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# fib(10)

# def fib(max_number):
#     n, a, b = 0, 0, 1
#     while n < max_number:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# for n in fib(10):
#     print(n)


# def triangles():
#     for i in range(10):
#         yield (x for x in range(i))

# def triangles():
#     L = [1]
#     yield L
#     while True:
#         L = [1 if i == 0 else L[i - 1] + L[i] for i in range(len(L))]
#         L.append(1)
#         yield L
#
#
# # 期待输出:
# # [1]
# # [1, 1]
# # [1, 2, 1]
# # [1, 3, 3, 1]
# # [1, 4, 6, 4, 1]
# # [1, 5, 10, 10, 5, 1]
# # [1, 6, 15, 20, 15, 6, 1]
# # [1, 7, 21, 35, 35, 21, 7, 1]
# # [1, 8, 28, 56, 70, 56, 28, 8, 1]
# # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# n = 0
# results = []
# for t in triangles():  # 迭代对象可以为集合数据类型，如list、tuple、dict、set、str;
#     results.append(t)  # 还可以是generator，包括生成器和带yield的generator function
#     n = n + 1
#     if n == 10:
#         break
#
# for t in results:
#     print(t)
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# from functools import reduce
#
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#
#     def char2num(s):
#         return DIGITS[s]
#
#     return reduce(fn, map(char2num, s))
#
#
# print("1556")
# print(str2int("1556"))


# def normalize(name):
#     t1 = name[0:1].upper()
#     t2 = name[1:].lower()
#     t = t1 + t2
#     return t
#
#
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# from functools import reduce
#
#
# def prod(L):
#     def multi(x, y):
#         return x * y
#     return reduce(multi, L)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# from functools import reduce
#
#
# def str2float(s):
#     index = s.find('.')
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#     def char2num(s):
#         t0 = digits[s]
#         return t0
#
#     t1 = reduce(lambda x, y: x * 10 + y, map(char2num, s[0:index]))
#     t2 = reduce(lambda x, y: x * 10 + y, map(char2num, s[index + 1:]))
#     return t1 + t2 * 0.1 ** (len(s)-index-1)
#
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
# def is_palindrome(n):
#     t1 = str(n)
#     t2 = str(n)[::-1]
#     return t1 == t2
#
#
# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77,
#                                                   88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 假设我们用一组tuple表示学生名字和成绩：
# 请用sorted()对上述列表分别按名字和成绩排序：


# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
#
# def by_name(t):
#     return t[0].lower()
#
#
# def by_score(t):
#     return -t[1]
#
#
# L2 = sorted(L, key=by_name)
# print(L2)
# L2 = sorted(L, key=by_score)
# print(L2)

# def inc():
#     x = 0
#     def fn():
#         # 仅读取x的值:
#         return x + 1
#     return fn
#
# f = inc()
# print(f()) # 1
# print(f()) # 1

# def inc():
#     x = 0
#     def fn():
#         nonlocal x #不加此行则会认为x为fn的局部变量，未赋初值报错
#         x = x + 1
#         return x
#     return fn
#
# f = inc()
# print(f()) # 1
# print(f()) # 2

# # 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# def createCounter():
#     x = 0
#
#     def counter():
#         nonlocal x
#         x = x + 1
#         return x
#
#     return counter
#
#
# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# # 请用匿名函数改造下面的代码：
# # def is_odd(n):
# #     return n % 2 == 1
# is_odd = lambda x: x % 2 == 1
#
# L = list(filter(is_odd, range(1, 20)))
#
# print(L)

# # 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
# import time, functools
#
#
# def metric(fn):
#     def wrapper(*args, **kw):
#         t1 = time.time()
#         fn(*args, **kw)
#         t2 = time.time()
#         print('%s execute in %s ms' % (fn.__name__, t2 - t1))
#         return fn(*args, **kw)
#
#     return wrapper
#
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
#
# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())

# # 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self._gender = gender
#
#     def get_gender(self):
#         return self._gender
#
#     def set_gender(self, gender):
#         self._gender = gender
#
#
# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


# # 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count = Student.count + 1  # 需要绑定Student类
#
#
# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')


# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2015 - self._birth

# # 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# class Screen:
#     # def __init__(self):
#     #     self._resolution = None
#     #     self._height = None
#     #     self._width = None
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         self._height = value
#
#     @property
#     def resolution(self):
#         return self._width * self._height
#
#
# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')


# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1  # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self  # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b  # 计算下一个值
#         if self.a > 100000:  # 退出循环的条件
#             raise StopIteration()
#         return self.a  # 返回下一个值
#
#
# for n in Fib():
#     print(n)


# # 把Student的gender属性改造为枚举类型，可以避免使用字符串：
# from enum import Enum, unique
#
#
# class Gender(Enum):
#     Male = 0
#     Female = 1
#
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#
# # 测试:
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')


# from functools import reduce
#
#
# def str2num(s):
#     return float(s)
#
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
# main()


# # 对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：
# import unittest
#
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score < 0 or self.score > 100:
#             raise ValueError
#         if self.score >= 80:
#             return 'A'
#         if self.score >= 60:
#             return 'B'
#         return 'C'
#
#
# class TestStudent(unittest.TestCase):
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
#
# if __name__ == '__main__':
#     unittest.main()


# # 对函数fact(n)编写doctest并执行：
# def fact(n):
#     """
#     Calculate 1*2*...*n
#
#     >>> fact(1)
#     1
#     >>> fact(10)
#     3628800
#     >>> fact(-1)
#     Traceback (most recent call last):
#     ValueError
#     """
#     if n < 1:
#         raise ValueError()
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()


# # 请将本地一个文本文件读为一个str并打印出来：
# fpath = 'E:\\其他文件\\名词解释.txt'  # 'D:\\info\\testRead.txt'

# with open(fpath, 'r', encoding='utf-8') as f:  # 注意编码utf-8
#     s = f.read()
#     print(s)

# # 运行代码观察结果







'''
# MOOC 课程Python编程
'''
# # TempConvert.py 温度转换
# TempStr = input("请输入带有符号的温度值: ")
# if TempStr[-1] in ['F', 'f']:
#     C = (eval(TempStr[0:-1]) - 32)/1.8
#     print("转换后的温度是{:.2f}C".format(C))
# elif TempStr[-1] in ['C', 'c']:
#     F = 1.8*eval(TempStr[0:-1]) + 32
#     print("转换后的温度是{:.2f}F".format(F))
# else:
#     print("输入格式错误")

# print(eval("1+2+3")) #去掉参数最外侧引号并执行余下语句的函数






