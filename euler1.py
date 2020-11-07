# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:12:50 2020

@author: kor_a
"""
print(sum([x for x in range(1000) if ((x % 5 == 0) or (x % 3 == 0))]))