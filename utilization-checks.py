import math
def solution(averageUtil, instances):
    i = 0
    while (i < len(averageUtil)):
        util = averageUtil[i]
        if util < 25:
            if instances != 1:
                instances = math.ceil(instances / 2)
            i += 10
        elif util > 60 and 2*instances <= 2*108:
            instances = 2*instances
            i += 10
        else:
            i += 1
        print(instances, i)
    return instances


instances=1
averageUtil=[30, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89,]
print(solution(averageUtil,instances))

