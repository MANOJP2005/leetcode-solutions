class Solution:
    def setZeroes(self, matrix):

        m = len(matrix)
        n = len(matrix[0])

        rows = set()
        cols = set()

      
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        for j in cols:
            for i in range(m):
                matrix[i][j] = 0