#!/usr/bin/env python
# encoding:utf-8
# Mi

def divgcd(a, b):
    x = 0 #被除数
    y = 0 #除数
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a
    while y != 0:
        (x, y) = (y, x%y)
    return x
    

if __name__ == "__main__":
    
    print divgcd(15, 20)
