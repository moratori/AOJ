
taro = 0
hanako = 0
for dummy in xrange(int(raw_input())):
    (tcard , hcard) = raw_input().split(" ")
    if tcard > hcard:
        taro += 3
    elif hcard > tcard:
        hanako += 3
    else:
        taro += 1
        hanako += 1
print taro,hanako
