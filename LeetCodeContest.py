class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        n = len(nums)
        a = [0] * (n - 1)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                a[i - 1] = 1
            elif nums[i] == nums[i - 1]:
                a[i - 1] = 0
            else:
                a[i - 1] = -1
        
        n -= 1
        m = len(pattern)
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j and pattern[j] != pattern[i]:
                j = lps[j - 1]
            if pattern[j] == pattern[i]:
                j += 1
            lps[i] = j
        
        j = 0
        ans = 0
        for i in range(n):
            while j and pattern[j] != a[i]:
                j = lps[j - 1]
            if pattern[j] == a[i]:
                j += 1
            if j == m:
                ans += 1
                j = lps[j - 1]
        
        return ans
