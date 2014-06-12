
n = int(raw_input())
S = map(int,raw_input().strip().split())
q = int(raw_input())
T = map(int,raw_input().strip().split())

r = 0
for each in T:
    if each in S: r+=1
print r
