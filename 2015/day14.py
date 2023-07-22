#!/usr/bin/env python3

REINDEERS = []

def get_data(filename):
    f = open(filename)
    for line in f:
        line = line.split()
        REINDEERS.append({
            "name": line[0],
            "speed": int(line[3]),
            "length": int(line[6]),
            "rest": int(line[-2])
        })


def get_distance(time_limit):
    max_distance = 0
    winner = ""
    for reindeer in REINDEERS:
        one_dist = reindeer['length'] * reindeer['speed']
        one_time = reindeer['length'] + reindeer['rest']
        distance = time_limit // one_time * one_dist
        remain = time_limit % one_time
        if remain >= reindeer['length']:
            distance += one_dist
        else:
            distance += reindeer['speed'] * remain
        if(distance > max_distance):
            max_distance = distance
            winner = reindeer['name']
        print(reindeer['name'], distance)
    return (winner, max_distance)


#for part 2:
def get_points(time_limit):
    for reindeer in REINDEERS:
        reindeer['points'] = 0
        reindeer['distance'] = 0
        reindeer['time_count'] = 0
        reindeer['is_rest'] = False
    for sec in range(time_limit):
        for reindeer in REINDEERS:
            reindeer['time_count'] += 1
            if reindeer['is_rest']:
                if reindeer['time_count'] == reindeer['rest']:
                    reindeer['is_rest'] = False
                    reindeer['time_count'] = 0
            else:
                reindeer['distance'] += reindeer['speed']
                if reindeer['time_count'] == reindeer['length']:
                    reindeer['is_rest'] = True
                    reindeer['time_count'] = 0
        incr_point()


def incr_point():
    max_distance = 0
    for reindeer in REINDEERS:
        if reindeer['distance'] > max_distance:
            max_distance = reindeer['distance']
    for reindeer in REINDEERS:
        if reindeer['distance'] == max_distance:
            reindeer['points'] += 1
        
        
def find_winner_points(time_limit):
    get_points(time_limit)
    win_points = 0
    winner = ""
    for reindeer in REINDEERS:
        if reindeer['points'] > win_points:
            winner = reindeer['name']
            win_points = reindeer['points']
    return (winner, win_points)


def print_reindeer():
    for reindeer in REINDEERS:
        print(f"name: {reindeer['name']}\npoints: {reindeer['points']}\ndistance: {reindeer['distance']}\n")


def main():
    get_data("src/day14.txt")
    winner_reindeer = get_distance(2503)
    print("PART 1:")
    print(f"The winner reindeer is {winner_reindeer[0]}, who flew {winner_reindeer[1]} kilometers away.") #2660
    winner_reindeer = find_winner_points(2503)
    print("PART 2:")
    print(f"The winner reindeer is {winner_reindeer[0]}, who collected {winner_reindeer[1]} points.") #1256


if __name__ == "__main__":
    main()