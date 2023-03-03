#!/usr/bin/python3

arr = [10, -200, -50, -30, 200, 1000]

max = arr[0]

for x in arr:
    if x > max:
       max = x

print("Maximum of arr is ", max)
