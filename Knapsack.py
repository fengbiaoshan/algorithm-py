#!/usr/bin/env python
# coding:utf-8

#Author: Mi Zhangpeng


def knapsack(sizes, values,capacity):
    dp = [[0]*(capacity+1) for i in range(len(sizes))]
    backpointer = {}

    for k in range(1,capacity+1):
        if k >= sizes[0]:
            dp[0][k] = values[0]

    for i in range(1,len(sizes)):
        for j in range(1,capacity+1):
            if j >= sizes[i] and dp[i-1][j-sizes[i]] + values[i] > dp[i-1][j]:
                dp[i][j] = dp[i-1][j-sizes[i]] + values[i]
                backpointer[(i,j)] = (i-1,j-sizes[i])
            else:
                dp[i][j] = dp[i-1][j]
                backpointer[(i,j)] = (i-1,j)
    i, j = len(sizes)-1, capacity
    resultindex = []
    while (i,j) in backpointer:
        if j != backpointer[(i,j)][1]:
            resultindex.append(i)
        i, j = backpointer[(i,j)]
    resultindex.reverse()
    return (resultindex, dp[len(sizes)-1][capacity])
    

    
if __name__ == "__main__":
    a = [4,3,2,5]
    b = [5,2,2,6]
    print knapsack(a,b,7)

