
def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)

def lcm(a,b):
    return a*b/gcd(a,b)

while True:
    try:
        (a,b) = map(int,raw_input().split(" "))
        print "%d %d" %(gcd(a,b),lcm(a,b))
    except (EOFError):
        break

