#!/usr/bin/env python3

def is_triangle(sides):
    return max(sides) < sum(sides) - max(sides)
# other solution:
    # return sides[0] < sides[1] + sides[2] and sides[1] < sides[0] + sides[2] and sides[2] < sides[0] + sides[1]

def main():
    possibles_p1 = 0
    possibles_p2 = 0
    triangles = [[], [], []]
    counter = 0
    with open("src/day3.txt") as f:
        for line in f:
            nums = [int(n) for n in line.split()]
            possibles_p1 += 1 if is_triangle(nums) else 0

            triangles[0].append(nums[0])
            triangles[1].append(nums[1])
            triangles[2].append(nums[2])
            counter += 1
            if counter == 3:
                possibles_p2 += 1 if is_triangle(triangles[0]) else 0
                possibles_p2 += 1 if is_triangle(triangles[1]) else 0
                possibles_p2 += 1 if is_triangle(triangles[2]) else 0
                triangles = [[], [], []]
                counter = 0
            
    print("The answer for part 1: ", possibles_p1)
    print("The answer for part 2: ", possibles_p2)
            


if __name__ == "__main__":
    main()