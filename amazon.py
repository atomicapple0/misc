from collections import defaultdict

def slowestKey(num, keyTimes):
    # WRITE YOUR CODE HERE
    best = defaultdict(int)
    prevTime = 0

    for c,t in keyTimes:
        time = t - prevTime
        best[c] = max(best[c],time)
        prevTime = t
    alp = "abcdefghijklmnopqrstuvwxyz"
    
    bc = None
    bt = -1
    for c,t in best.items():
        if t > bt:
            bt = t
            bc = c
    return alp[bc]


def stockPairs(num, stocksProfit, target):
    # WRITE YOUR CODE HERE
    print(stocksProfit, target)
    
    hashset = set()
    dict = {}
    acc = 0
    for stock in stocksProfit:
        wtf = target - stock
        
        if wtf == stock:
            if 2 * wtf == target and wtf not in hashset and wtf in dict:
                acc += 1
                hashset.add(wtf)
            dict[wtf] = True
        elif wtf in dict and dict[wtf]:
            acc += 1
            dict[wtf] = False
            dict[stock] = False
        else:
            if stock not in dict:
                dict[stock] = True
        
        
            
    return acc