# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:11:37 2020

@author: 15025
"""

import itertools as its


words = "abcdefghigklmnopqrstuvwxyz1234567890"
r = its.product(words, repeat=8)
dic = open("C:/Users/15025/Desktop/password.txt", "a")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
    # print(i)

dic.close()
print("密码本已生成")