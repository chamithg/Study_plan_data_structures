class Solution:
    def matrixReshape(self, mat, r, c) :
        itemArr = []
        outArr = []
        
        # generate an array of all elements
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                itemArr.append(mat[i][j])
                
        # if there is no elements ,return a empty array
        if not itemArr: return []
                
        # check if the given r and c is acceptable to place all the elements
        # if not return the original matrix
        if r*c != len(itemArr):
            return mat

        #  map elememt as per the given matrix
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(itemArr[0])
                del itemArr[0]
            outArr.append(temp)    
        return outArr
        
        




mat = [[1,2],[3,4]] 
r= 1
c = 4

obj = Solution()
print(obj.matrixReshape(mat,r,c))