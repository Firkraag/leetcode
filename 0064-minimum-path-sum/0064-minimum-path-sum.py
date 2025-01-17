class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memorize = [[-1] * n for _ in range(m)]
        memorize[m - 1][n - 1] = grid[m - 1][n - 1]
        for col in range(n - 2, -1, -1):
            memorize[m - 1][col] = grid[m - 1][col] + memorize[m - 1][col + 1]
        for row in range(m - 2, -1, -1):
            memorize[row][n - 1] = grid[row][n - 1] + memorize[row + 1][n - 1]

        return self.minPathSumAux(grid, 0, 0, memorize)
    
    def minPathSumAux(self, grid, row, col, memorize):
        if memorize[row][col] != -1:
            return memorize[row][col]
        memorize[row][col] = min(self.minPathSumAux(grid, row + 1, col, memorize), self.minPathSumAux(grid, row, col + 1, memorize)) + grid[row][col]
        return memorize[row][col]