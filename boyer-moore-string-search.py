#/usr/bin/env python
#encoding:utf-8

#Author Mi


pattern = "example"

s = "here is an simple example"

def suffixes(pattern):  #求每一个位置上以该位置为结尾的和后缀相同的字串长度
    m = len(pattern)
    suffixes = [0]*m
    suffixes[-1] = m
    g = m-1
    for i in range(m-2,-1,-1):
        if i > g and suffixes[i+m-1-f] < i-g:  #根据已求出的长度可以快速获得当前位置的长度，
            suffixes[i] = suffixes[i+m-1-f]     #因为i-g和后缀的前部分是完全一致的，
                                                #若相应部分的求出长度就那么长，那么该位置的长度也就那么长
        else:
            if i < g:
                g = i
            f = i
            while (g >= 0 and pattern[g] == pattern[g+m-1-f]):
                g -= 1
            suffixes[i] = f - g
    return suffixes


def badCharacters(pattern):
    m = len(pattern)
    badChars = {}
    for i in range(m-1):
        badChars[pattern[i]] = m-i-1
    return badChars


def goodSuffixes(pattern):
    m = len(pattern)
    suff = suffixes(pattern)
    goodSuffixes = [m]*m
    for i in range(m-1,-1,-1):
        if suff[i] == i + 1:
            for j in range(m-i-1):
                if goodSuffixes[j] == m:
                    goodSuffixes[j] = m-i-1
    for i in range(m-2):
        goodSuffixes[m-1-suff[i]] = m-i-1
    return goodSuffixes

def boyerMoore(pattern, s):
    n = len(s)
    m = len(pattern)

    goodSuff = goodSuffixes(pattern)
    badChars = badCharacters(pattern)

    i = 0
    while i <= n-m:
        j = m-1
        while pattern[j] == s[i+j]:
            j -= 1
        if j < 0:
            print i
            i += goodSuff[0]
        else:
            if s[i+j] not in badChars:
                i += max(goodSuff[j],j+1)
            else:
                i += max(goodSuff[j],badChars[s[i+j]]-m+j+1)

boyerMoore(pattern,s)

    


    
