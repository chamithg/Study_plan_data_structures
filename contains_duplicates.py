class Solution:
    def containsDuplicate(self, nums):
        numMap ={}
        
        for i in nums:
            if i not in numMap:
                numMap[i]=1
            else:
                return True
        return False
        
        
        
        
        
nums = [1,2,3,5]

obj = Solution()
print(obj.containsDuplicate(nums))