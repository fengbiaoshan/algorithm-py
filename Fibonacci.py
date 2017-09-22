#/usr/bin/env python
#encoding:utf-8

#Author Mi


def matrixMul(l, r):
    if not l or not r or (len(l[0]) != len(r)):
        return False
    else:
        midl = len(r)
    ans = [[0]*len(r[0]) for i in range(len(l))]
    for i in range(len(l)):
        for j in range(len(r[0])):

            for k in range(midl):
                ans[i][j] += (l[i][k]*r[k][j])

    return ans


def matrixPower(A, n):
    ans = [[0]*len(A) for i in range(len(A))]
    for i in range(len(A)):
        ans[i][i] = 1
    tmp = A
    while n != 0:
        if ((n & 1) == 1):
            ans = matrixMul(ans, tmp)
        tmp = matrixMul(tmp, tmp)
        n >>= 1

    return ans


def fib(n):
    A = [[1,1],[1,0]]
    ans = matrixPower(A,n-1)
    return ans[0][0]



print fib(7)

