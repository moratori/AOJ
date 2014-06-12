


ai = 100000
debt = 5/100.0
for i in xrange(1,int(raw_input())+1):
    ai = ai + ai * (debt)
    hasu = ai % 1000
    if hasu != 0 : ai += 1000 - hasu
print int(ai)

