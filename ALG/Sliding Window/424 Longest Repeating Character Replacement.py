class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n == 1:
            return 1
        char_count = defaultdict(int)
        left, result = 0, 0
        # i being the right boundary of the substr, aka sliding window
        for i in range(n):
            char_count[s[i]] += 1
            # length of substr - maxfreq char <= k
            if (i - left + 1) - max(char_count.values()) > k:
                char_count[s[left]] -= 1 # substr left boundary shifts to left, decrease its char freq
                left += 1
            result = max(i - left + 1, result)
        
        return result