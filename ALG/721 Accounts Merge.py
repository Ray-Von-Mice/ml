class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        '''
        mapping between each email and its account index in accounts
        for example, jhs@e.com mapps john at index 0 (accounts[0])
        '''
        emIndx = dict()
        for i in enumerate(accounts):
            tmp = i[1][1:]
            j = 0
            for email in tmp:
                try:
                    emIndx[email]
                except KeyError:
                    emIndx[email] = []
                emIndx[email].append(i[0])
        # To find neighbors, use usr_email_index -> to find usr_email_index -> use the mapping we created, with each email -> to find email, use input accounts with enumerate n
        result = []
        visited =[False] * n
        for m in range(n):
            if visited[m]:
                continue
            travel = deque()
            travel.append(m)
            ems = set()
            while travel:
                cur = travel.popleft()
                emails = accounts[cur][1:]
                for em in emails:
                    ems.add(em)
                    for usr_em_index in emIndx[em]:
                        if visited[usr_em_index]:
                            continue
                        travel.append(usr_em_index)
                        visited[usr_em_index] = True
            emList = list(ems)
            emList.sort()
            templ = [accounts[m][0]] + emList
            result.append(templ)
        return result         