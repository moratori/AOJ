
import sys

def pretty_print(l):
    sys.stdout.write(str(l[0]))
    for each in l[1:]:
        sys.stdout.write(" " + str(each))

(rn,cn) = map(int,raw_input().split(" "))
data = [map(int,raw_input().split(" ")) for dummy in xrange(rn)]
res = 0
for row in data:
    pretty_print(row)
    tmp = sum(row)
    sys.stdout.write(" " + str(tmp))
    res += tmp
    print ""
pretty_print(map(sum,zip(*data)))
print " " + str(res)
