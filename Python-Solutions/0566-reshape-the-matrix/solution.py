class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        new = []
        for row in mat:
            for col in row:
                new.append(col)
        res = []
        for i in range(0, len(new), c):
            res.append(new[i : i + c])
            
        return res
