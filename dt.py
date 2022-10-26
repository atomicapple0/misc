import functools
def formTeam(d, t, q):
    print(d,t,q)

    @functools.lru_cache(maxsize=None)
    def helperD(l):
        # .... T
        if l <= 0:
            return 0
        if l == 1:
            return 1
        count = 0
        for i in range(1,min(d,l+1)):
            count += helperT(l-i)
        return count
            
    @functools.lru_cache(maxsize=None)
    def helperT(l):
        # .... D
        if l <= 0:
            return 0
        if l == 1:
            return 1
        count = 0
        for i in range(1,min(t,l+1)):
            count += helperD(l-i)
        return count
    
    sol = []
    for qq in q:
        sol.append(helperD(qq+1) + helperT(qq+1))
    print(sol)
    return sol

formTeam(4, 2, [4])