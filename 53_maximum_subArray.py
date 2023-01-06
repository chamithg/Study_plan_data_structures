class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]
        tempSum = 0

        for each in nums:
            if tempSum <0:
                tempSum = 0
            tempSum += each

            maxSum = max(maxSum, tempSum)

        return maxSum 

nums = [-2,1,-3,4,-1,2,1,-5,4]
obj = Solution()
print(obj.maxSubArray(nums))