# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/1912:21
software: PyCharm

Description:
"""

print('\n'.join([''.join([__import__('random').choice('\u2571\u2572') for i in range(80)]) for j in range(24)]))
"""
\u2571:代表符号/
\u2572:代表符号\
‘’.join()去掉了列表的括号
"""
