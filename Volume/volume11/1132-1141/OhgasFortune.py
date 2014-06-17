


import math


def simulation(left,duration,torf,ratio,fee):
    acc = 0
    fee = int(fee)
    for d in xrange(int(duration)):
        if ( torf == 0 ):
            acc  += int(math.floor(left * ratio))
            left -= fee
        else:
            left = int(math.floor(left * ratio) + left - fee)
    return left + acc


for d1 in xrange(input()):
    init_money = input()
    duration   = input()
    print max([apply((lambda x,y,z: simulation(init_money,duration,x,y,z)),map(float,raw_input().split())) for d2 in xrange(input())])
