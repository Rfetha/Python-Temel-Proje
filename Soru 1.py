# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:02:46 2021

@author:FERHAT ERSOY
"""

'''
Soru 1
    Bir listeyi düzleştiren (flatten) fonksiyon yazın.
'''



def flatten_list(x):
  return _flatten_list([], x)

def _flatten_list(arr, x):
  for e in x:
    if isinstance(e, list):
      _flatten_list(arr, e)
    else:
      arr.append(e)
  return arr

print( flatten_list([[1,'a',['cat'],2],[[[3]],'dog'],4,5]) ) 