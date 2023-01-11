class Solution:
    def generate(self, numRows):
        outArr = []
        for i in range(numRows):
            row = []
            if i == 0: row.append(1)
            elif i == 1: 
                row.append(1)
                row.append(1)
            else:
                row.append(1)
                for j in range(len(outArr[i-1])-1):
                    row.append(outArr[i-1][j]+outArr[i-1][j+1])
                row.append(1)
            outArr.append(row)
        return outArr


numRows = 5
obj = Solution()
print(obj.generate(numRows))