#!/usr/bin/python3
for i in range(1, 80):
    for j in range(1, i + 1):
        if str(format(j, '02'))[::-1] == str(format(i, '02')):
            break
        elif j == i:
            print(format(i, '02'), end=", ")
print("89")
