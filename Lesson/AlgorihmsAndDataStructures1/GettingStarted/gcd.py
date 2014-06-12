
def gcd(x,y):
    # 1 < y < x
    # 1 < y AND y < x
    # 1 >= y or y >= x
    if y == 0: return x
    return gcd(y,x%y)

(a,b) = map(int,raw_input().split(" "))
print gcd(a,b)

