

LENGTH = int(raw_input())
DATA = []
right = int(raw_input())
left = int(raw_input())

DATA.append(right)
DATA.append(left)
maximum = left - right

for i in xrange(LENGTH-2):
    read = int(raw_input())
    if read > left:
        maximum += read - left
        left = read
    else:
        for already in (DATA):
            tmp = read - already
            if tmp > maximum:
                maximum = tmp
                left = read
                right = already
    DATA.append(read)
print maximum
