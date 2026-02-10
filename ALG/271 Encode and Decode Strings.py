class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # Hello -> 5#Hello
        i, n = 0, len(s)
        result = []
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            substr_l = int(s[i:j])
            start = j + 1
            j = start + substr_l
            substr = s[start:j]
            result.append(substr)
            i = j
        return result