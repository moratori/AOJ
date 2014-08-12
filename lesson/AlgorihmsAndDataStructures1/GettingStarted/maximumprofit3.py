

length = int(raw_input())
data = [int(raw_input()) for d in xrange(length)]
maximum = float("-inf")
then_i = 0

for i in xrange(length):
    diff = data[i] - data[then_i]
    lm = maximum - diff
    if lm > maximum : 
        maximum = lm
        then_i = i
    for j in xrange(i+1,length):
        tmp = data[j] - data[i]
        if tmp > maximum : 
            maximum = tmp
            then_i = i

print maximum

