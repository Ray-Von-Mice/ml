class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns, nt = len(s), len(t)
        if ns < nt:
            return ""
        needs, matches = defaultdict(int), defaultdict(int)
        subStrL = float("inf")
        for i in range(nt):
            needs[t[i]] += 1
        
        cnt_need, cnt_match = len(needs), 0
        '''
            match and need are overall char counter respectively for string s and string t, 
            len(needs) represent how many characters are there in T, and needs[char] represent char frequency
            len(matches) represent how many chas in S, and matches[char] must match or greater than needs[char]
        '''
        left = 0
        boundaries = [0, 0]
        for i in range(ns):
            curChar = s[i]
            matches[curChar] += 1

            if curChar in needs and matches[curChar] == needs[curChar]:
                cnt_match += 1
            
            while cnt_match == cnt_need:
                if (i - left + 1) < subStrL:
                    subStrL = i - left + 1
                    boundaries = [left, i]
                '''
                    shifting left boundary to left by 1 regardlessly, decrease its frequency regardlessly, 
                    check if s[left] char is in needs, if yes and its frequency smaller than its needs, decrease the overall count of matches
                '''
                matches[s[left]] -= 1
                if s[left] in needs and matches[s[left]] < needs[s[left]]:
                    cnt_match -=1
                    print(cnt_match == cnt_need)
                left += 1

        return s[boundaries[0]: boundaries[1] + 1] if subStrL != float("inf") else ""