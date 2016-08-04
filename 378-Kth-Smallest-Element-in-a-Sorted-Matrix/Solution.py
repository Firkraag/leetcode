class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        if k == 1:
            return matrix[0][0]
        elif k == n * n:
            return matrix[n - 1][n - 1]
        else:
            indices = set()
            indices.add((0, 0))
            import heapq
            h = [(matrix[0][0], (0, 0))]
            count = 0
            
            while count < k:
                value, index = heapq.heappop(h)
                count += 1
                x, y = index
                if x + 1 < n and (x + 1, y) not in indices:
                    indices.add((x + 1, y))
                    heapq.heappush(h, (matrix[x + 1][y], (x + 1, y)))
                if y + 1 < n and (x, y + 1) not in indices:
                    indices.add((x, y + 1))
                    heapq.heappush(h, (matrix[x][y + 1], (x, y + 1)))
            return value
                    