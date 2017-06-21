#!/usr/bin/env python
# coding:utf-8

#Author: Mi Zhangpeng


def mul(a, b):
    result = [0]*(len(a)+len(b))
    for i in range(len(a)-1, -1, -1):
        carry = 0
        for j in range(len(b), 0, -1):
            result[i+j] = result[i+j] + carry + int(a[i])*int(b[j-1])
            carry = result[i+j] // 10
            result[i+j] = result[i+j] % 10
        result[i] = carry
    result_str = ""
    for d in result:
        result_str += str(d)
    return result_str

if __name__ == "__main__":
    a = "2142413249832789573275891723453418294"
    b = "4875438952638564375724609857043897589237"
    print mul(a, b)
    print 2142413249832789573275891723453418294*4875438952638564375724609857043897589237
