class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return[strs]
        answer = defaultdict(list)
        for word in strs:
            tmp = "".join(sorted(word))
            answer[tmp].append(word)
        result = []
        for i in enumerate(answer):
            result.append(answer[i[1]])
        return result