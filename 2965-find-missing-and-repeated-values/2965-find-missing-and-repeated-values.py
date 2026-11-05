class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid) ** 2
        freq = {}

        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        repeated = missing = 0

        for i in range(1, n + 1):
            if freq.get(i, 0) == 2:
                repeated = i
            elif freq.get(i, 0) == 0:
                missing = i

        return [repeated, missing]