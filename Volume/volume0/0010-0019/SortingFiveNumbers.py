
import sys

nums = map(int,raw_input().split(" "))
nums.sort(cmp = lambda x,y: y-x)
for i,v in enumerate(nums):
    if i != 0:
        sys.stdout.write(" ")
    sys.stdout.write(str(v))
print ""
