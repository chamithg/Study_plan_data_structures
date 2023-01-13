class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap ={}
        for index, each in enumerate(s):
            if each not in charMap:
                charMap[each]=index
            else:
                charMap[each]= -1
        
        for key, value in charMap.items():
            if value != -1:
                return value
        
        return -1
        
s ="rrrrleetcode"
obj = Solution()
print(obj.firstUniqChar(s))