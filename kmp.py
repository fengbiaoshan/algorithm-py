#!/usr/bin/env python

# Mi

def get_next(pattern):
    nex = [0] * len(pattern)
    j = 0
    nex[0] = 0
    for i in range(1,len(pattern)):
        while j > 0 and  pattern[i] != pattern[j]:
            j = nex[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        nex[i] = j
    return nex

def kmp(pattern, text):
    pos = -1
    nex = get_next(pattern)
    i = 0
    j = 0
    for i in range(len(text)):
        while j>0 and pattern[j] != text[i]:
            j = nex[j-1]
        if pattern[j] == text[i]:
            j += 1
            if j == len(pattern):
                pos = i-j+1
                break

    return pos
        

if __name__ == "__main__":
    
    print kmp("abcab","dghabcabbgcabchab")
