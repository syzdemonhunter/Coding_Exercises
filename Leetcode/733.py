# https://leetcode.com/problems/flood-fill/
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
            return image
        m, n = len(image), len(image[0])
        self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image
    
    def dfs(self, image, i, j, color, newColor):
        if i < 0 or i >= len(image) or \
           j < 0 or j >= len(image[i]) or \
           image[i][j] != color:
            return
        
        image[i][j] = newColor
        self.dfs(image, i + 1, j, color, newColor)
        self.dfs(image, i - 1, j, color, newColor)
        self.dfs(image, i, j + 1, color, newColor)
        self.dfs(image, i, j - 1, color, newColor)