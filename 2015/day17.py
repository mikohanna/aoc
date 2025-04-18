import itertools

liters = 150

#prepare the numbers:
nums = []
with open("src/day17.txt") as f:
    for line in f:
        nums.append(int(line))
nums.sort(reverse=True)


#find the min number of combinations:
min_comb = 0
for i in range(len(nums)):
    if sum(nums[:i]) <= liters:
        min_comb += 1
    else:
        break

#find the max number of combinations:
max_comb = 0
for i in range(len(nums)):
    if sum(nums[len(nums)- 1 - i :]) <= liters:
        max_comb += 1
    else:
        break
    
#answer for part 1:
liter_fit = 0
for i in range(min_comb, max_comb + 1):
    variations = tuple(itertools.combinations(nums, i))
    liter_fit += sum([1 for x in variations if sum(x) == liters])
print("the answer for part 1: ", liter_fit)

#answer for part 2:
variations = tuple(itertools.combinations(nums, min_comb))
part2_ans = sum([1 for x in variations if sum(x) == liters])
print("the answer for part 2: ", part2_ans)