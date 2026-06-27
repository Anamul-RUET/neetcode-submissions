class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    for val in range(n):
                        if(matrix[val][j]): matrix[val][j]=10000000000

                    for val in range(m):
                        if matrix[i][val]:
                            matrix[i][val]=10000000000
                    matrix[i][j]=10000000000
        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==10000000000): matrix[i][j]=0
        