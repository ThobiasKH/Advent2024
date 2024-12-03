import os

path = "input.txt" 
list1 = []
list2 = []

with open(path, "r") as file:
    lines = file.readlines()
    for line in lines:
        l = line.strip().split()
        list1.append( int( l[0] ))
        list2.append( int( l[1] ))

file.close()

dst = 0
# slight misunderstanding
#for i in range(1000):
 #   l = sorted([int(digit) for digit in str(list1[i])])
  #  r = sorted([int(digit) for digit in str(list2[i])])
   # for j in range(len(l)):
    #    dst += abs(l[j] - r[j])
     
list1.sort()
list2.sort()
for i in range(1000): 
    dst += abs(list1[i] - list2[i])
       
print(dst)