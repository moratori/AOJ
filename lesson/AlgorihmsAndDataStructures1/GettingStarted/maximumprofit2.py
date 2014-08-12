

length = int(raw_input())
data = [int(raw_input()) for d in xrange(length)]
nextr = True
maximum = float("-inf")
t = 0
for i in xrange(length):
    #if (i + 1 == t) : nextr = True
    if not nextr:
        diff = data[i] - data[t]
        lm = maximum - diff
        if lm > maximum:
            maximum = lm
            t = i
    for j in xrange(i+1,length):
        tmp = data[j] - data[i]
        if tmp > maximum : 
            maximum = tmp
            t = i
            nextr = True if (j == i + 1) else False

print maximum

