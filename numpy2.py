# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:42:12 2018

@author: Administrator
"""
import numpy as np

a=np.arange(2,14).reshape(3,4)

print(a)
print(np.argmax(a))
print(np.mean(a))
print(np.cumsum(a))
print(np.diff(a))
print(np.nonzero(a))
print(a.T)
print(np.clip(a,5,9))