
data = []
while True:
    try:
        data.append(int(raw_input()))
    except (EOFError):
        break
dic = {each:data.count(each) for each in data}
k = max(dic,key=lambda k:dic[k])
length = dic[k]
for each in sorted([key for key in dic if length == dic[key]]):print each
