import operator
defop = {"+": operator.__add__ ,
         "-": operator.__sub__,
         "*": operator.__mul__,
         "/": operator.__div__}

(left,op,right) = raw_input().split(" ")
while (op != "?"):
    print defop[op](int(left),int(right))
    (left,op,right) = raw_input().split(" ")

