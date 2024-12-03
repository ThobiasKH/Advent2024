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

# part 2
def solveCorruptedMemoryPart2(file_path):
    do = True
    
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    patternDo = r"do\(\)"
    patternDont = r"don\'t\(\)"
    
    result = 0
    
    with open(file_path, 'r') as file:
        content = file.read()
        
        matches = re.finditer(f"{pattern}|{patternDo}|{patternDont}", content)

        for match in matches:
            if match.group(0) == "do()":
                do = True  
            elif match.group(0) == "don't()":
                do = False  
            elif match.group(0).startswith("mul"):
                num1 = int(match.group(1))
                num2 = int(match.group(2))
                
                if do:
                    result += num1 * num2
    
    return result   

totalP2 = solveCorruptedMemoryPart2(file_path)
print(totalP2)