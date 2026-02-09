class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        s1cnt, s2cnt = [0] * 26, [0] * 26
        for i in range(n1):
            s1cnt[ord(s1[i]) - ord('a')] += 1
            s2cnt[ord(s2[i]) - ord('a')] += 1

        if s1cnt == s2cnt:
            return True

        for i in range(n1, n2):
            # fixed substring size, upgrading both right and left by 1
            s2cnt[ord(s2[i]) - ord('a')] += 1
            s2cnt[ord(s2[i - n1]) - ord('a')] -= 1
            if s1cnt == s2cnt:
                return True

        return False