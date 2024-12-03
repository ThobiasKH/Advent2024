import re

def solveCorruptedMemory(file_path):
    # first time trying to use regex
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    result = 0

    with open(file_path, 'r') as file:
        content = file.read()
        
        matches = re.findall(pattern, content)

        for match in matches:
            num1, num2 = int(match[0]), int(match[1])
            result += num1 * num2

    return result

file_path = "./input.txt"  

total_sum = solveCorruptedMemory(file_path)
print(total_sum)
