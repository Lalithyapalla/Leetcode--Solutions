class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if (row + col == (len(mat)-1)) or ( row == col):
                    sum += mat[row][col]
        return sum
