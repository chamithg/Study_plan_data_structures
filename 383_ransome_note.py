class Solution:
    def canConstruct(self, ransomNote,magazine):
        #  create ransomeNode hashmap:
        wordMap={}
        for i in ransomNote:
            if i in wordMap:
                wordMap[i]+=1
            else:
                wordMap[i] =1
        
        # iteraet over the magazine
        runner = 0
        while runner < len(magazine):
            if magazine[runner] in wordMap:
                wordMap[magazine[runner]] -=1
                if wordMap[magazine[runner]] ==0:
                    wordMap.pop(magazine[runner])
            if not wordMap: return True
            else:
                runner +=1
        return False

ransomNote = "bbbbb"
magazine = "bbabb"
obj = Solution()
print(obj.canConstruct(ransomNote,magazine))