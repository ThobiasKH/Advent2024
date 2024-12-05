def createArrays(filename):
    rules = []
    updates = []
    isReadingRules = True
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line == '\n':
                isReadingRules = False
            
            if isReadingRules:
                data = line.strip().split('|')
                rules.append( (int(data[0]), int(data[1])) )
            
            else:
                data = line.strip().split(',')
                updates.append( [int(i) for i in data if i != ''] )
                
    return rules, updates

rules, updates = createArrays("input.txt")

def findPairs(tuples, pair):
    pairSet = set(pair)
    for tup in tuples:
        if set(tup) == pairSet:
            return tup
    return None

def determineValidUpdate(rules, update):
    isValid = True
    for i in range(len(update) - 1):
        num1 = update[i]
        num2 = update[i + 1]
        rule = findPairs(rules, (num1, num2))
            
        if rule == None:
            continue
            
        elif rule[0] != num1 or rule[1] != num2:
            isValid = False
            break
        
    if isValid and update != []:
        center = update[len(update) // 2]
        return center
        
    return False
            
print(len([]))

total = 0
for u in updates:
    center = determineValidUpdate(rules, u)
    print(center)
    total += center if center != False else 0
    
print(total)

# part 2
print("PART 2")
incorectOrderedUpdates = [u for u in updates if determineValidUpdate(rules, u) == False]

# cool algorithm
def sortUpdate(rules, update):
    graph = {num: [] for num in update}
    in_degree = {num: 0 for num in update}

    for x, y in rules:
        if x in graph and y in graph:  
            graph[x].append(y)
            in_degree[y] += 1

    queue = [node for node in update if in_degree[node] == 0]
    sorted_list = []

    while queue:
        current = queue.pop(0)  
        sorted_list.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_list) == len(update):
        return sorted_list
    else:
        return []  

for i in range(len(incorectOrderedUpdates)):
    incorectOrderedUpdates[i] = sortUpdate(rules, incorectOrderedUpdates[i])

total2 = 0
for i in incorectOrderedUpdates:
    center = determineValidUpdate(rules, i)
    total2 += center if center != False else 0
    
print(total2)
# under 100 lines