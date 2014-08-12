

(x,y) = map(int,raw_input().split(" "))
while (not (x == 0 and y == 0)):
    print "%s %s" %(min(x,y) , max(x,y))
    (x,y) = map(int,raw_input().split(" "))

