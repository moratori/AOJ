

def isgetall(gem_pos,ops):
    assert ((type(gem_pos) == list) and (type(ops) == list))

    result = {(pos[0],pos[1]):False for pos in gem_pos}

    x = y = 10
    for op in ops:
        (direction,movement) = op
        movement = int(movement)
        for step in xrange(1,movement+1):
            if ( direction == "N"):
                y += 1
            elif ( direction == "E" ):
                x += 1
            elif (direction == "S"):
                y -= 1
            elif (direction == "W"):
                x -= 1
            if [x,y] in gem_pos:
                result[(x,y)] = True
    for k in result:
        if not result[k] : return "No"
    return "Yes"





while True:
    n = int(raw_input())
    if (n == 0) : break
    gem_pos = [map(int,raw_input().split()) for d in xrange(n)]
    op_num  = int(raw_input())
    ops     = [raw_input().split() for d in xrange(op_num)]
    print isgetall(gem_pos,ops)
