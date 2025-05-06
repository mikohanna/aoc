def is_safe(nums):
    is_incr = nums[0] < nums[1]
    for i, n in enumerate(nums[:-1]):
        diff = abs(nums[i+1] - n)
        if diff > 3 or diff < 1 or is_incr and n > nums[i+1] or not is_incr and n < nums[i+1]:
            return False
    return True
        
def is_safe_with_dampener(nums):
    if is_safe(nums):
        return True
    for i in range(len(nums)):
        if is_safe(nums[:i]+nums[i+1:]):
            return True
    return False
            
result_part1 = 0
result_part2 = 0
with open("src/day2.txt") as src:
    for line in src:
        result_part1 += 1 if is_safe([int(x) for x in line.split()]) else 0
        result_part2 += 1 if is_safe_with_dampener([int(x) for x in line.split()]) else 0
        
print("the result for part 1:", result_part1)
print("the result for part 2:", result_part2)