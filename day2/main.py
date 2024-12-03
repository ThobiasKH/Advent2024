import os

path = "day2\\input.txt" if os.name == "nt" else "./input.txt" 
data = []
with open(path, "r") as file:
    lines = file.readlines()
    for line in lines:
        x = line.strip().split()
        print(x)
        data.append([int(n) for n in x])

file.close()

def isSafe(report):
    isIncreasing = report[0] <= report[1]
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if abs(diff) > 3 or abs(diff) < 1:
            return False
        if isIncreasing and diff < 0 or not isIncreasing and diff > 0:
            return False
    return True

numSafe = 0
for i in range(len(data)):
    numSafe += 1 if isSafe(data[i]) else 0

print(numSafe)