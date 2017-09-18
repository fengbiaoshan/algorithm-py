#/usr/bin/env python
#encoding:utf-8

#Author Mi


#longest palindrome substr


#manacher's algorithm


a = "ababababsdadadbababadawddafzhgffghadwdlkjhgfghjklfse"



def lps(a):
    a = "#"+"#".join(list(a))+"#"
    maxr = 0
    pos = 0
    LR = [0]*len(a)   #插入特殊字符后的字符串每一点的回文半径数组
    i = 0
    while i < len(a):
        if i > maxr:
            j = 0
            while i+j < len(a) and a[i+j] == a[i-j]:
                if i+j > maxr:
                    maxr = i+j
                    pos = i
                j+=1
            LR[i] = j
            
        else:
            j = min(LR[2*pos-i], maxr-i)
            while i+j < len(a) and a[i+j] == a[i-j]:
                if i+j > maxr:
                    maxr = i+j
                    pos = i
                j+=1
            LR[i] = j
        i += 1

    maxl = 0
    maxp = 0
    for k in range(len(LR)):
        if maxl < LR[k]-1: #LR[k]-1正好是原字符串以k为中心的回文长度
            maxl = LR[k]-1
            maxp = k
    return maxl


print lps(a)
