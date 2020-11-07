# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:43:04 2020

@author: kor_a
"""
fib = 1
fib2 = 2
temp = 0
total = 0
while temp <= 4000000:
    temp = fib2
    if temp % 2 == 0:
        total += temp
    temp = fib + fib2
    fib = fib2
    fib2 = temp
print(total)
def even_fib(limit):
    a,b = 0,1
    while a < limit:
        if not a % 2:
            yield a
        a, b = b, a + b
print(sum(even_fib(4000000)))