
ran = xrange(10)

while True:
    try:
        r = 0
        n = int(raw_input())
        for a in ran:
            for b in ran:
                for c in ran:
                    for d in ran:
                        if (a + b + c + d == n): r +=1
        print r
    except (EOFError):break
