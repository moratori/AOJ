

def readata():
    return map(int,raw_input().split(" "))

def grade(mid,fin,re):
    if (mid == -1) or (fin == -1):return "F"
    total = mid + fin
    if total >= 80: return "A"
    if 80 > total >= 65: return "B"
    if 65 > total >= 50: return "C"
    if 50 > total >= 30: 
        if re >= 50: return "C"
        return "D"
    if 30 > total : return "F"

(mid,fin,re) = readata()
while True:
    if (mid == -1) and (fin == -1) and (re == -1):break
    print grade(mid,fin,re)
    (mid,fin,re) = readata()

