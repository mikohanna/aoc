#!/usr/bin/env python3
from asyncio.windows_events import NULL
import get_data as gd


class Bingo:
    def __init__(self, file_name, last_win=False) -> None:
        f = open(file_name)
        self.my_nums = [int(n) for n in f.readline().split(',')]
        self.grids = []
        grid_index = -1
        for line in f:
            if len(line) < 2:
                self.grids.append([])
                grid_index += 1
                continue
            self.grids[grid_index].append([int(n) for n in line.split()])
        self.is_part_2 = False
        if last_win:
            self.is_part_2 = True

    def change_num(self, num):
        for i, grid in enumerate(self.grids):
            for j, line in enumerate(grid):
                self.grids[i][j] = [n if n != num else -1 for n in line]

    def check_win(self):
        for grid in self.grids:
            column_count = 0
            for line in grid:
                if line == [-1] * 5:
                    return grid
            for i in range(5):
                for j in range(5):
                    if grid[j][i] == -1:
                        column_count += 1
                    else:
                        column_count = 0
                if column_count == 5:
                    return grid
        return None

    def check_win2(self):
        last_win_grid = []
        for grid in self.grids:
            column_count = 0
            is_win = False
            for line in grid:
                if line == [-1] * 5:
                    is_win = True
                    break
            if not is_win:
                for i in range(5):
                    column_count = 0
                    for j in range(5):
                        if grid[j][i] == (-1):
                            column_count += 1
                        else:
                            column_count = 0
                    if column_count == 5:
                        is_win = True
                        break
            if is_win:
                if len(self.grids) == 1:
                    last_win_grid = grid
                self.grids.remove(grid)
        return last_win_grid

    def count_result(self, grid, num):
        result = 0
        for line in grid:
            result += sum([n for n in line if n != -1])
        return result * num

    def play_part1(self):
        for n in self.my_nums:
            self.change_num(n)
            win_grid = self.check_win()
            if win_grid:
                res = self.count_result(win_grid, n)
                print(win_grid)
                print(f"You win with the {n} number\nThe result is: {res}")
                break

    def play_part2(self):
        for n in self.my_nums:
            self.change_num(n)
            last_win = self.check_win2()
            if not self.grids:
                print("-" * 50)
                res = self.count_result(last_win, n)
                print(last_win)
                print(f"You win with the {n} number\nThe result is: {res}")
                break

    def play(self):
        if self.is_part_2:
            self.play_part2()
        else:
            self.play_part1()

def main():
    print("Part 1------")
    bingo = Bingo("src/day4.txt")
    bingo.play()
    print("Part 2------")
    bingo2 = Bingo("src/day4.txt", True)
    bingo2.play()


if __name__ == "__main__":
    main()
