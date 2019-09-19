#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not type(str):
        return 0
    a = 0
    su = 0
    if roman_string.count('I') > 3 or roman_string.count('V') > 3 \
       or roman_string.count('X') > 3 or roman_string.count('L') > 3 \
       or roman_string.count('C') > 3 or roman_string.count('D') > 3:
        return 0
    for i in range(len(roman_string) - 1, -1, -1):
        if roman_string[i] == 'D':
            a = 500
            su += 500
        elif roman_string[i] == 'C' and a <= 100:
            a = 100
            su += 100
        elif roman_string[i] == 'C' and a > 100:
            su -= 100
        elif roman_string[i] == 'L' and a <= 50:
            a = 50
            su += 50
        elif roman_string[i] == 'L' and a > 50:
            su -= 50
        elif roman_string[i] == 'X' and a <= 10:
            a = 10
            su += 10
        elif roman_string[i] == 'X' and a > 10:
            su -= 10
        elif roman_string[i] == 'V' and a <= 5:
            a = 5
            su += 5
        elif roman_string[i] == 'V' and a > 5:
            su -= 5
        elif roman_string[i] == 'I' and a <= 1:
            a = 1
            su += 1
        elif roman_string[i] == 'I' and a > 1:
            su -= 1
    return su
