class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        left, subStr = 0, 0
        c_set = set()
        for i in range(n):
            while s[i] in c_set:
                c_set.remove(s[left])
                left += 1
            c_set.add(s[i])
            subStr = max(subStr, i - left + 1)
        return subStr