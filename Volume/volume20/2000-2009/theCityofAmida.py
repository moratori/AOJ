#!/usr/bin/env python
#coding:utf-8


def main():
    while True:
        (n_tate,n_yoko,start) = map(int,raw_input().split(" "))
        amida = []
        if n_tate == 0 and n_yoko == 0 and start == 0:
            break
        for dummy in range(n_yoko):
            (h,p,q) = map(int,raw_input().split(" "))
            amida.append((h,p,q))
            amida.sort(key=lambda x:-x[0])
        print solve(n_tate,n_yoko,start,amida)


def mymax(*seq):
    if len(seq) == 1:
        return seq[0]
    else:
        return apply(max,seq)

def start_height(amida):
    return apply(mymax,map(lambda x: x[0],amida)) + 0.5


def isfinish(current_tate,current_yoko,amida):
    tmp = filter(lambda x: (x[1] == current_tate) or (x[2] == current_tate),amida)
    for (h,p,q) in tmp:
        if h < current_yoko : 
            return False 
    return True



def getnext(current_tate,current_yoko,amida):
    tmp = filter(lambda x: (x[1] == current_tate) or (x[2] == current_tate),amida)
    index = 0
    minval = float("inf")
    for i,(h,p,q) in enumerate(tmp):
        diff = abs(h-current_yoko)
        if h < current_yoko and  diff < minval:
            minval = diff 
            index = i
    return tmp[index]


def solve(n_tate,n_yoko,start,amida):
    """
       startからamidaを始めた場合にどこに到着するか
       あみだの縦線の番号を返す関数
    """
    current_tate = start
    current_yoko = start_height(amida)

    while not isfinish(current_tate,current_yoko,amida):
        (h,p,q) = getnext(current_tate,current_yoko,amida)
        current_yoko = h - 0.5
        current_tate = p if current_tate == q else q

    return current_tate



if __name__ == "__main__":
    main()
