#Alternate solution of 3964, with O(n^2) time complexity. Has a similar approach to previous one.

class Solution:
    def minLights(self, lights: list[int]) -> int:
        visibles = [False]*len(lights)
        n = len(lights)
        min_bulb = 0
        for pos, bulb in enumerate(lights):
            if bulb > 0:
                for a in range (max(0, pos-bulb), min(n-1, pos+bulb)+1):
                    visibles[a] = True
        count = 0
        for pos in range(len(visibles)):
            if not visibles[pos]:
                count += 1
            else:
                min_bulb += (count +2) // 3
                count = 0
        min_bulb += (count + 2) // 3
        return min_bulb

#Time Complexity: O(n^2) where n is length of array
#Space complexity: O(n)