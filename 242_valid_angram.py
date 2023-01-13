class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t): return False
        # create counter hashmap s
        charMap = {}
        for i in s:
            if i in charMap:
                charMap[i] += 1
            else:
                charMap[i] =1
        for index,j in enumerate(t):
            if j not in charMap:
                return False
            charMap[j] -=1
            if charMap[j] == 0:
                charMap.pop(j)
            if not charMap and index == len(t)-1:
                return True
        
        return False
s = "anagrat"
t = "nagaram"       
obj =Solution()
print(obj.isAnagram(s,t))