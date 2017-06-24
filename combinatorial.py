def combinatorial(s,index,tmp,depth,c):
    if depth >= c:
        print tmp
        return
    for i in range(index, len(s)):
        combinatorial(s,i+1,tmp+s[i],depth+1,c)


combinatorial("abcde",0,"",0, 3)
