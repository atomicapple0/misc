'''
geo node has many buildings
numOfBuilding: trivial
buildingOpenTime: list of offload time of each intake delivery
offloadTime: list of offload time of each intake delivery
output: earliest time at which intake deliveries can be offloaded
'''

'''b, n'''
'''O(nlgn)'''


def deliveries(numOfBuilding, buildingOpenTime, offloadTimes):
    '''
    number of offloads == 4 * buildings
    [10000000, 1]
    [1,2,3,4,5,6,7,8]
    => 
    '''
    buildingOpenTime.sort()
    # offloadTimes.sort()
    # offloadTimes.reverse()
    offloadTimes.sort(key=lambda x: -1 * x)

    sol = 0
    for buildingTime, offloadTime in zip(buildingOpenTime,offloadTimes[:3:4]):
        sol = max(sol, buildingTime + offloadTime)
    return sol


print(deliveries(2, [8,10], [2,2,3,1,8,7,4,5]))