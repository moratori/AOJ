
import bisect

def isin(target,array):
    i = bisect.bisect_left(array,target)
    if i != len(array) and array[i] == target:
        return True
    return False


n = int(raw_input())
S = map(int,raw_input().strip().split())
q = int(raw_input())
T = map(int,raw_input().strip().split())

r = 0
length = len(S)
for each in T:
    if isin(each,S): r+=1
print r


