class Solution:
    def minLights(self, lights) -> int:
        visibles = [False]*len(lights)
        n = len(lights)
        min_bulb = 0
        diff = [0]*(n+1)
        for i, v in enumerate(lights):
            if v > 0:
                L = max(0, i-v)
                R = min(n-1, i+v)
                diff[L] += 1
                if R+1 < n:
                    diff[R+1] -= 1
            print(diff)
        count = 0
        curr = 0
        for i in range(n):
            curr += diff[i]
            visibles[i] = curr > 0
            print(visibles)
        for pos in range(len(visibles)):
            if not visibles[pos]:
                count += 1
            else:
                min_bulb += (count +2) // 3
                count = 0
        min_bulb += (count + 2) // 3
        return min_bulb

sol = Solution()
res = sol.minLights(lights = [0,0,0,0])
print(res)