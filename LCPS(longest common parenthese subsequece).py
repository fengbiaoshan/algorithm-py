#!/usr/bin/env python
# coding:utf-8

#Author: Mi Zhangpeng


##最长公共子括号序列
##Description
##
##一个合法的括号匹配序列被定义为:
##
##空串""是合法的括号序列
##如果"X"和"Y"是合法的序列,那么"XY"也是一个合法的括号序列
##如果"X"是一个合法的序列,那么"(X)"也是一个合法的括号序列
##每个合法的括号序列都可以由上面的规则生成
##例如"", "()", "()()()", "(()())", "(((()))"都是合法的。
##从一个字符串S中移除零个或者多个字符得到的序列称为S的子序列。
##例如"abcde"的子序列有"abe","","abcde"等。
##定义LCS(S,T)为字符串S和字符串T最长公共子序列的长度,即一个最长的序列W既是S的子序列也是T的子序列的长度。
##小易给出一个合法的括号匹配序列s,小易希望你能找出具有以下特征的括号序列t:
##1、t跟s不同,但是长度相同
##2、t也是一个合法的括号匹配序列
##3、LCS(s, t)是满足上述两个条件的t中最大的
##因为这样的t可能存在多个,小易需要你计算出满足条件的t有多少个。
##如样例所示: s = "(())()",跟字符串s长度相同的合法括号匹配序列有:
##"()(())", "((()))", "()()()", "(()())",其中LCS( "(())()", "()(())" )为4,其他三个都为5,所以输出3.
##
##Input
##
##输入包括字符串s(4 ≤ |s| ≤ 50,|s|表示字符串长度),保证s是一个合法的括号匹配序列。
##
##Output
##
##输出一个正整数,满足条件的t的个数。
##
##Sample Input
##
##(())()
##
##Sample Output
##
##3



##根据题意，当且仅当修改距离为 1 时 LCS 最大。很容易证明对于两种基本序列 (()) 和 ()() 都有距离为 1 的合法修改。
##把每个符号插入到任意位置，判合法，去重，累计

def validPa(plist):
    lf = 0
    for i in range(len(plist)):
        if plist[i] == "(":
            lf += 1
        else:
            lf -= 1
            if lf < 0:
                return False
    if lf == 0:
        return True
    else:
        return False

pare = raw_input()
plist = list(pare)
pset = set()

for i in range(len(plist)):
    tmp = plist[:i] + plist[i+1:]
    for j in range(len(plist)):
        if plist[i] == plist[j]:
            continue
        tmp.insert(j,plist[i])
        if "".join(tmp) in pset:
            tmp.pop(j)
            continue
        if validPa(tmp):
            pset.add("".join(tmp))
        tmp.pop(j)

print len(pset)-1


