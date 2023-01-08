class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer = 0
        
        while pointer < m and nums2:
            if nums1[pointer] >= nums2[0]:
                nums1.insert(pointer,nums2[0])
                del nums1[-1]
                del nums2[0]
                m+=1
            pointer +=1
        if nums2:
            for i in range(m,len(nums1)):
                if nums1[i] == 0:
                    nums1[i]= nums2[0]
                    del nums2[0]
                
        print(nums1)
        

# passed
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# passed
nums1 = [-1,0,1,1,0,0,0,0,0]
m = 4
nums2 = [-1,0,2,2,3]
n = 5

obj = Solution()
print(obj.merge(nums1,m,nums2,n))