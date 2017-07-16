#求出数组中与当前元素左相邻的不小于当前元素的数的个数
nums =  [2,2,6,5,2,3]
n = len(nums)
leftad = [0]*n
stack = []
i = 0
while i < n:
    if not stack or nums[i] > nums[stack[-1]]:
        if not stack:
            leftad[i] = i+1
        else:
            leftad[i] = i - stack[-1]
        stack.append(i)
        i += 1
    else:
        stack.pop()

print leftad


