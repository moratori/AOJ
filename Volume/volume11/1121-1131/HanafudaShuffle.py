
import copy

def read():
    return map(int,raw_input().strip().split())

def operation(deckn,operations):
    deck = range(deckn,0,-1)
    for p,c in operations:
        p -= 1
        top_p = deck[0:p]
        bottom_c = deck[p:p+c]
        rest = deck[p+c:]

        bottom_c.extend(top_p)

        tmp = copy.deepcopy(bottom_c)
        tmp.extend(rest)
        deck = tmp

    return deck[0]

while True:
    (deckn , opn) = read()
    if (deckn == 0) and (opn == 0) : break
    print operation(deckn,[read() for dummy in xrange(opn)])




