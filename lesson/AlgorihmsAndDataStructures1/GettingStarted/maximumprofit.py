
cache = {}


def profit(sindex,seq):
    global cache
    diff = float("-inf")
    val = seq[sindex]
    if val in cache:
        return cache[val]
    else:
        for each in seq[sindex+1:]:
            tmp = each - val
            if tmp > diff : diff = tmp
        cache[val] = diff
        return diff

data = [int(raw_input()) for d in xrange(int(raw_input()))]
maximum = float("-inf")
for i in xrange(len(data)):
    val = profit(i,data)
    if val > maximum: maximum = val
print maximum

