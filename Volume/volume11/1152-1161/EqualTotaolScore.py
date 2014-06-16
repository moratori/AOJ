


def read_point(n):
    return [int(raw_input()) for d in xrange(n)]


def sum_other(array,index):
    r = 0
    for i,v in enumerate(array):
        if i != index : r += v
    return r


def proc(taro_point,hana_point):
    cand = []
    for ti,tp in enumerate(taro_point):
        for hi,hp in enumerate(hana_point):
            if (sum_other(taro_point,ti) + hp == sum_other(hana_point,hi) + tp):
                cand.append((tp,hp))
    if ( cand == []):
        return "-1"
    else:
        tmp = min(cand,key=(lambda x: x[0] + x[1]))
        return "%s %s" %(tmp[0],tmp[1])

def main():
    while True:
        (n,m) = map(int,raw_input().strip().split())
        if (n == 0) and (m == 0) : break 
        taro_point = read_point(n)
        hana_point = read_point(m)
        print proc(taro_point,hana_point)


main()


