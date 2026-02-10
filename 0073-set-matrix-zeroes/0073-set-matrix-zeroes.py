class Solution(object):
    def setZeroes(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        m = len(mat[0])
        mr = [0]*n
        mc = [0]*m 
        for i in range (n):
            for j in range (m):
                if mat[i][j] == 0:
                    mr[i] = 1
                    mc[j] = 1
        for i in range (n):
            for j in range (m):
                if mc[j] == 1 or mr[i] == 1:
                    mat[i][j] = 0
        return mat
        