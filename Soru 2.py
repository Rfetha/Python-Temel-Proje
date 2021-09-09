# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:01:11 2021

@author: ERSOY
"""

'''
    Soru 2    
'''


lst = [[1, 2], [3, 4], [5, 6,7],9]
lst.reverse()
for i in lst:
    if isinstance(i,list) == True:
        i.reverse()
print(lst)
