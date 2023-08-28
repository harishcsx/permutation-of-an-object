import math
import random

combinations = []
string = list(input("enter the value of string : "))
permutation = math.factorial(len(string))
print(permutation)

i = 0
while (i<=permutation) :
    random.shuffle(string)
    print("suffel item is :",string)
    print(i)
    if string not in combinations:
        combinations.append(string)
        i += 1
        continue
        
print("the following list values are : ",combinations)
for ans in range(len(combinations)):
    print(f"the number of combination: {ans} :- {combinations[ans]}")

print("done")