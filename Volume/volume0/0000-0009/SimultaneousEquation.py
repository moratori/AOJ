

def convert(n):
    if n == 0: return 0
    return n


while True:
    try:
        (a,b,c,d,e,f) = map(float,raw_input().split(" "))
        print "%.3f %.3f" %(convert(round((c*e-b*f)/(a*e-b*d),3)),convert(round((a*f-d*c)/(a*e-b*d),3)))
    except (EOFError):
        break
