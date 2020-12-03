#!/usr/bin/env python3


if __name__ == "__main__":
    with open('numbers-day1.txt', "r") as f:
        lines = [line.rstrip() for line in f]
    for i in lines:
        for j in lines:
            for k in lines:
                if int(i) + int(j) + int(k) == 2020:
                    print ("numbers are {} and {} and {}".format(i,j, k))
                    print ("product is {}".format(int(i)*int(j)*int(k)))
                    break