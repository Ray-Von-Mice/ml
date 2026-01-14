class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        visit = set(deadends)
        if target in visit or "0000" in visit:
            return -1
        
        level = 0
        travel = deque()
        travel.append("0000")

        while travel:
            n = len(travel)
            level += 1
            for _ in range(n):
                cur = travel.popleft()
                for i in range(4):
                    for j in [-1, 1]:
                        digit = (int(cur[i]) + j + 10) % 10
                        neb = cur[:i] + str(digit) + cur[i+1:]

                        if neb in visit:
                            continue
                        if neb == target:
                            return level
                        if neb not in visit:
                            visit.add(neb)
                            travel.append(neb)
                        
        return -1