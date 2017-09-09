#!/usr/bin/env python
# coding:utf-8

#Author: Mi Zhangpeng


##有一个合法的字符串，合法是指左括号与右括号全部能配对，现在每次将这个序列第一个左括号删去，在将任意一个右括号删去，每次删去后的序列必须合法，最后消去所有括号，求有多少种消去方法。
##
##输入：
##
##一个合法括号序列。
##
##输出：
##
##方案数。
##
##样例1：
##
##Input:
##
##()()()()
##
##Output：
##
##1
##
##样例2：
##
##Input
##
##(((())))()()
##
##Output:
##
##24


pare = raw_input()
plist = list(pare)
lf = 0
ans = 1

for i in range(len(plist)):
    if plist[i] == "(":
        lf += 1
    else:
        ans *= lf
        lf -= 1

print ans
