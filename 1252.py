class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = []
        for i in range(n):
            matrix.append([0] * m)
        for row, col in indices:
            for j in range(m):
                matrix[row][j] += 1
            for i in range(n):
                matrix[i][col] += 1
        odd_count = 0
        for i in range(n):
            for j in range(m):
                odd_count += (matrix[i][j] & 1)
        return odd_count
