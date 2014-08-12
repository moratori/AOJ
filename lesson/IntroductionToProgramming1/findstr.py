
def convert(w1):
    return map((lambda x: ord(x) if not (x.isalpha()) else ord(x.lower())),w1)

def string_eq(w1,w2):
    return convert(w1) == convert(w2)

def count(target,line):
    linesp = line.split()
    r = 0
    for each in linesp:
        if string_eq(each,target): r += 1
    return r

target = raw_input()
res = 0
while True:
    line = raw_input()
    if line == "END_OF_TEXT":break
    res += count(target,line)
print res
