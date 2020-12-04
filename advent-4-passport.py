#!/usr/bin/env python3
import re
import json

def validate_passports(passports):
    required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl','pid')
    count = 0
    for line in passports:
        passport= {field.split(":")[0]: field.split(':')[1] for field in line.split()}
        if all(item in passport for item in required):
            count += 1
    print(count)

def validate_values(passports):
    valid = 0
    for passport in passports:
        counter = 0
        # Validate the given requierenments
        if re.search(r"byr:(19[2-9][0-9]|200[0-2])\b",
                     passport):  # Requirenment: byr (Birth Year) - four digits; at least 1920 and at most 2002.
            counter += 1
        if re.search(r"iyr:(201[0-9]|20[0-2]0)\b",
                     passport):  # Requirenment: iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            counter += 1
        if re.search(r"eyr:(202[0-9]|2030)\b",
                     passport):  # Requirenment: eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            counter += 1
        if re.search(r"(hgt:59in|hgt:6[0-9]in|hgt:7[0-6]in|hgt:1[5-8][0-9]cm|hgt:19[0-3]cm)\b",
                     passport):  # Requirenment: hgt (Height) - a number followed by either cm or in: If cm, the number must be at least 150 and at most 193. If in, the number must be at least 59 and at most 76.
            counter += 1
        if re.search(r"hcl:#([0-9]|[a-f]){6}\b",
                     passport):  # Requirenment: hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            counter += 1
        if re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b",
                     passport):  # Requirenment: ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            counter += 1
        if re.search(r"pid:([0-9]){9}\b",
                     passport):  # Requirenment: pid (Passport ID) - a nine-digit number, including leading zeroes.
            counter += 1

        if counter == 7:
            valid += 1  # increment the valid counter if all seven requirenments are satisfied

    print(valid)

if __name__ == "__main__":
    with open("day-4-passport.txt") as f:
        passports = f.read().replace('\n\n', '|').replace('\n', ' ').split('|')
    validate_passports(passports)
    validate_values(passports)



