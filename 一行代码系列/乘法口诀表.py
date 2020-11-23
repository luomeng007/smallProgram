# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/1912:21
software: PyCharm

Description:
"""

print('\n'.join([' '.join(["%2s x%2s = %2s" % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))
