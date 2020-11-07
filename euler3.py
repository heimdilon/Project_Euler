# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:51:19 2020

@author: kor_a
"""
n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
print(n)