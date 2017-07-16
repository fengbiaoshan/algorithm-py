#!/usr/bin/env python
# coding:utf-8

#Author: Mi Zhangpeng

from collections import deque
import math
nums = [6,2,6,2,6,23,5,363,56,2356,23,562,626,4,6,3,62]
stsize = 2*(2**(math.ceil(math.log(len(nums),2))))-1
st = [0]*int(stsize)
def buildst(st,nums,start,end,si):
    if start == end:
        st[si] = nums[start]
        return nums[start]
    mid = (start + end)/2
    st[si] = buildst(st,nums,start,mid,si*2+1) + buildst(st,nums,mid+1,end,si*2+2)
    return st[si]

buildst(st,nums,0,len(nums)-1,0)

def queryst(st,rangel,ranger,start,end,si):
    if rangel <= start and ranger >= end:
        return st[si]
    elif end < rangel or start > ranger:
        return 0
    else:
        mid = (start + end)/2
        return queryst(st,l,r,start,mid,si*2+1)+queryst(st,l,r,mid+1,end,si*2+2)

print queryst(st,7,9,0,len(nums)-1,0)



##queue = deque()
##queue.append(0)
##queue.append(None)
##tmp = ""
##while queue:
##    if len(queue) == 1:
##        break
##    item = queue.popleft()
##    if item == None:
##        print tmp
##        tmp = ""
##        queue.append(None)
##    else:
##        tmp += (str(st[item]) + " ")
##        if 2*item+1 < stsize:
##            queue.append(2*item+1)
##        if 2*item+2 < stsize:
##            queue.append(2*item+2)
    
