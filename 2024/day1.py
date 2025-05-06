left_list = []
right_list = []
with open("src/day1.txt") as src:
    for line in src:
        a, b = [int(x) for x in line.split()]
        left_list.append(a)
        right_list.append(b)
left_list.sort()
right_list.sort()
result = 0
for i in range(len(left_list)):
    result += abs(left_list[i] - right_list[i])
print("the answer for part 1: ", result)
result = 0
for i in left_list:
    result += i * right_list.count(i)
print("the answer for part 2: ", result)
