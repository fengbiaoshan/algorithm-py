class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m>n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax = 0, m
        allhalf = (m+n+1)/2
        while True:
            i = (imin+imax)/2
            j = allhalf - i
            if i<m and nums2[j-1] > nums1[i]:
                imin = i+1
            elif i>0 and nums1[i-1] > nums2[j]:
                imax = i-1
            else:
                break
        if i == 0:
            maxleft = nums2[j-1]
        elif j == 0:
            maxleft = nums1[i-1]
        else:
            maxleft = nums1[i-1] if nums1[i-1] > nums2[j-1] else nums2[j-1]
        if (m+n)%2 == 1:
            return maxleft

        if i == m:
            minright = nums2[j]
        elif j == n:
            minright = nums1[i]
        else:
            minright = nums1[i] if nums1[i] < nums2[j] else nums2[j]
        return (maxleft+minright)/float(2)
sol = Solution()
print sol.findMedianSortedArrays([1,3,5],[2,3,6])
