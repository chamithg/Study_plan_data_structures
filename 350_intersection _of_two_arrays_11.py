class Solution:
    def intersect(self, nums1, nums2):
        
        #  this solution works , but failed to find intersection with shuffled values
        # output = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             t = 0
        #             while i+t < len(nums1) and j+t < len(nums2) and (nums1[i+t] == nums2[j+t] or nums1[i+t] == nums2[j-t]):
        #                 output.append(nums1[i+t])
        #                 t+=1
        #             return output    
        
        #  solution2 = hashmap
        
        numMap = {}
        output =[]
        # this will create a counter object of the array.
        for i in nums1:
            if i not in numMap:
                numMap[i]= 1
            else:
                numMap[i]+=1
                
        for j in nums2:
            
            if j in numMap and numMap[j]>0:
                numMap[j]-=1
                output.append(j)
        return output
    
    
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj = Solution()
print(obj.intersect(nums1,nums2))

