

import sys

def pretty_print(seq):
    sys.stdout.write(str(seq[0]))
    for each in seq[1:]:
        sys.stdout.write(" " + str(each))
    print ""

length = int(raw_input().strip())
A = map(int,raw_input().strip().split())
for i in xrange(1,length):
    pretty_print(A)
    key = A[i]
    j = i -1
    while (j >= 0) and (A[j] > key):
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key
pretty_print(A)
