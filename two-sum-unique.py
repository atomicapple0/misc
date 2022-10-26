def solution(nums, target):
    dict = {}
    count = 0
    for num in nums:
        if target - num in dict:
            if dict[target - num]:
                dict[target - num] = False
                count += 1
        elif num not in dict:
            dict[num] = True
    return count

print(solution([1,1,2,45,46,46],47))
print(solution([1,1],2))
print(solution([1,5,1,5],6))
