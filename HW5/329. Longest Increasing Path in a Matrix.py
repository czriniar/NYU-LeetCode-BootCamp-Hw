from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        memo = [[0] * n for _ in range(m)]
        
        def dfs(x, y):
            if memo[x][y] != 0:
                return memo[x][y]
            
            max_length = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    max_length = max(max_length, 1 + dfs(nx, ny))
            
            memo[x][y] = max_length
            return max_length
        
        max_path_length = 0
        for i in range(m):
            for j in range(n):
                max_path_length = max(max_path_length, dfs(i, j))
        
        return max_path_length
