

def read():
    return raw_input().strip()


def ismake(num,series):
    if (num == 0):return True
    if series == [] : return False
    if (1 > num): return False
    if (num > sum(series)) : return False
    if (num in series) :return True

    for each in series:
        cand = series[:]
        cand.remove(each)
        if ismake(num-each,cand):return True
    return False

ser_len = int(read())
series  = map(int,read().split(" "))
query_len = int(read())
for query in map(int,read().split(" ")):
    print "yes" if ismake(query,series) else "no"
