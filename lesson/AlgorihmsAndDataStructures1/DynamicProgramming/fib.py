

f_i = 1
f_in = 1
for i in xrange(int(raw_input())):
    tmp = f_in
    f_in = f_i + f_in
    f_i  = tmp
print f_i
