#week 2 solution
def final(a,rem):
    prod = 1
    for each in a:
        prod *= each
    if prod in rem: #if product is found in given array
        return True
    else:
        return False
    
l = int(input())
a = [int(x) for x in input().split()]

from itertools import permutations
ans = permutations(a,l) #generating possible combination
done = True
for each in ans:
    rem = a.copy()
    for item in each:
        rem.remove(item)
    if final(each, rem):
        done = False
        print(*each)
        break
if done:
    print("Requirement not met")