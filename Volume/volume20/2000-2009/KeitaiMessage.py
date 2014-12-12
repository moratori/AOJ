#!/usr/bin/env python
#codng:utf-8


TABLE = {
    1: [".",",","!","?"," "] ,
    2: ["a","b","c"] ,
    3: ["d","e","f"] ,
    4: ["g","h","i"] ,
    5: ["j","k","l"],
    6: ["m","n","o"],
    7: ["p","q","r","s"],
    8: ["t","u","v"],
    9: ["w","x","y","z"]}


def getchar(series):
  kind = int(series[0])
  data = TABLE[kind]
  return data[(len(series) % len(data))-1]

def solve(series):
  result = ""
  tmp = ""
  for c in series:
    if (c != '0') : 
      tmp += c
    else:
      if (tmp != "") : 
        result += getchar(tmp)
        tmp = ""
  return result


def main():
  for d in xrange(int(raw_input())):
    print solve(raw_input())

if __name__ == "__main__" : main()
