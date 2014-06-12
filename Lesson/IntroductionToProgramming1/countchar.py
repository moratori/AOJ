

def gettext():
    res = ""
    while True:
        try:
            res += raw_input()
        except (EOFError):
            return res

d = [0 for d in xrange(26)]
for each in gettext():
    if not each.isalpha():continue
    low = ord(each.lower()) - 97
    d[low] = d[low] + 1
for i,v in enumerate(d):
    print "%s : %s" %(chr(i+97),v)
