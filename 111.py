# for i in 'hello world':
#     if i == 'o':
#         break
#     print(i * 2, end='')

#
# def gs(a=2, b=3):
#     print(a + b)
#
# gs(4)
# print('str'[0:3])
#
# try:
#     a = 2 + '1'
#     print(a)
# except TypeError:
#     print('Error')
#
# s = map(lambda x: x * x, [0,1,2,3,4])
# print(list(s))
#
# c = [1,2] + []
# print(c)
#
# d = {{{'socrat': 'empty'}: {'plato': 'mineral'}}: 'again'}
# key = {'socrat': 'empty'}
# print(dict[key]['plato'])
# for i in "str":
#     print(i.upper(), end='.')
# import random
# print(random.random())
# x = 23
# num = 0 if x>10 else 11
# print(num)
# o_d = {'a': 10, "b": 10}
# n_d = {}
#
# for i, j in o_d.items():
#     n_d[j] = i
#
# print(n_d)

# d = {1, 2} == set([1, 2])
# print(d)

# a ={'a': 10, "c":30}
# b = {'c': 20, 'e':5}
# for i in a.keys():
#     if i not in b:
#         b[i] = a[i]
# print(b)

#
# try:
#     b = 1/ 0
# except ZeroDivisionError:
#     b = 0
# print(b)
#
# pg = True
#
# def fun1():
#     pg = None
#     def fun2():
#         nonlocal pg
#         pg = 'py'
#
#     fun2()
#
# fun1()
#
# print(pg)
a = {'a': {'a': ["a"]}}
print(a.pop('a') == a.clear())