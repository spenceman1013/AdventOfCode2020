#!/usr/bin/env python3

def count_trees(*slopes):
    with open("day-3-map.txt") as f:
        map = f.read().splitlines()
    total = 1
    for slope in slopes:
        count = 0
        xcord, ycord = 0, 0
        while ycord < (len(map) - 1):
            xcord += slope[0]
            ycord += slope[1]
            if xcord > (len(map[ycord])-1):
                xcord -= len(map[ycord])
            if map[ycord][xcord] == "#":
                count +=1
        total *= count
    print (total)



if __name__ == "__main__":
    count_trees((3,1))
    count_trees((1,1), (3,1), (5,1), (7,1),(1,2))
