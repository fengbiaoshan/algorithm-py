from collections import deque
import time



def swap(array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

def allpermu(array, n, index):
    if index >= n:
        temp = ""
##        for it in array:
##            temp += it

        return
    for i in xrange(index,n):
        swap(array, i, index)
        allpermu(array, n, index+1)
        swap(array, i, index)



def allpermutwo(array):
    leng = len(array)
    queue = deque()
    queue.append("")
    for i in xrange(leng):
        while len(queue[0]) == i:
            temp = queue.popleft()
            for c in array:
                if c not in temp:
                    queue.append(temp+c)

start1 = time.clock()
allpermu(["a","c","d","b","e","f","g","h"], 8, 0)
end1 = time.clock()

start2 = time.clock()
allpermutwo(["a","c","d","b","e","f","g","h"])
end2 = time.clock()



print end1 - start1
print end2 - start2

