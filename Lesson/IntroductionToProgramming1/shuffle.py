
def shuffle(target,h):
    return target[h:] + target[0:h] 


while True:
    target = raw_input()
    if target == "-": break
    num = int(raw_input())
    for dummy in xrange(num):
        h = int(raw_input())
        target = shuffle(target,h)
    print target
