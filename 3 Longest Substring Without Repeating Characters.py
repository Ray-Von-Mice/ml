class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        chIndex = defaultdict(int)
        result, left = 0, -1
        for indx, char in enumerate(s):
            # charactor appeared before, if recorded index greater than slide window left bound (charactor is within current substr), upgrade left (move window left bound)
            if (char in chIndex) and chIndex.get(char) > left:
                left = chIndex.get(char)
            chIndex[char] = indx
            result = max(result, indx - left)
        
        return result