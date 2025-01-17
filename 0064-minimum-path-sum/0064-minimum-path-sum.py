class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memorize = [[-1] * n for _ in range(m)]
        return self.minPathSumAux(grid, 0, 0, memorize)
    
    def minPathSumAux(self, grid, row, col, memorize):
        m = len(grid)
        n = len(grid[0])
        if memorize[row][col] != -1:
            return memorize[row][col]
        if row >= m - 1 and col >= n - 1:
            return grid[row][col]
        elif row < m - 1 and col < n - 1:
            memorize[row][col] = min(self.minPathSumAux(grid, row + 1, col, memorize), self.minPathSumAux(grid, row, col + 1, memorize)) + grid[row][col]
        elif row < m - 1 and col == n - 1:
            memorize[row][col] = self.minPathSumAux(grid, row + 1, col, memorize) + grid[row][col]
        elif row == m - 1 and col < n - 1:
            memorize[row][col] = self.minPathSumAux(grid, row, col + 1, memorize) + grid[row][col]
        return memorize[row][col]