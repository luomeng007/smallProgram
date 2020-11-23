# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/1912:21
software: PyCharm

Description:
"""

print('\n'.join([''.join(['*' if abs((lambda a: lambda z, c, n: a(a, z, c, n))(lambda s, z, c, n: z if n == 0 else
s(s, z * z + c, c, n - 1))(0, 0.02 * x + 0.05j * y, 40)) < 2 else ' ' for x in range(-80, 20)]) for y in
                 range(-20, 20)]))
