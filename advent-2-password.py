#!/usr/bin/env python3
import re

def char_count(list):
    count = 0
    for line in list:
        string = re.split('-|:|\s', line)
        if string[4].count(string[2]) in range(int(string[0]), int(string[1]) + 1):
            count += 1
    print("The valid password count is {}".format(count))

def char_location(list):
    count = 0
    for line in list:
        string = re.split('-|:|\s', line)
        # print (i)
        first = string[4][int(string[0])-1]
        second = string[4][int(string[1])-1]
        if (first == string[2]) is not (second == string[2]):
            print (string)
            count += 1
    print(count)



if __name__ == "__main__":
    with open("password-day2.txt", "r") as f:
        lines = [line.rstrip() for line in f]
    char_count(lines)
    char_location(lines)