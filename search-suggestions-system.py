import bisect
class Solution:
    def suggestedProducts(self, products, searchWord):
        deq = products
        deq.sort()

        sol = []
        idx = 0
        for i in range(len(searchWord)):

            soll = []
            while idx < len(deq):
                try:
                    if deq[idx][:i + 1] == searchWord[:i + 1]:
                        break
                except:
                    pass
                idx += 1

            for j in range(idx, min(len(deq), idx + 3)):
                try:
                    if j < len(deq) and deq[j][:i + 1] == searchWord[:i + 1]:
                        soll.append(deq[j])
                    else:
                        break
                except:
                    pass

            sol.append(soll)
        return sol

    def optimal(self, A, word):
        A.sort()
        res = []
        prefix = ''
        i = 0
        for c in word:
            prefix += c
            i = bisect.bisect_left(A, prefix, lo=i)
            res.append([w for w in A[i:i+3] if w.startswith(prefix)])
        return res