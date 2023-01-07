class Solution:
    def twoSum(self, nums,target):
        
        
        #  solution 1-> poor time complexity
        # output = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             output.append(i)
        #             output.append(j)
        #             return output
        
        # solution 2 --> Using hashmaps
        numMap ={}
        
        for i,n in enumerate(nums):
            if target-n in numMap:
                return ([numMap[target-n],i])
            else:
                numMap[n]= i
        
        

nums =[2,7,11,15]
target = 9

obj = Solution()
print(obj.twoSum(nums,target))