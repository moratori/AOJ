#!/usr/bin/env python
#coding:utf-8




def primep(n):
  if ( n < 2): return False
  if (n == 2): return True
  if (n % 2 == 0) : return False
  acc = 3
  while (n >= acc * acc):
    if (n % acc == 0) : return False
    acc += 2
  return True


def solve(a,d,n):
  """
    simple way and slow
  """
  cnt = 0
  val = a
  while True:
    if (primep(val)) : 
      cnt += 1
      if (cnt == n) : return val
    val += d


def main():
  while True:
    (a,d,n) = map(int,raw_input().split(" "))
    if (a == 0) and (d == 0) and (n == 0) : break
    print solve(a,d,n)

if __name__ == "__main__":
  main()

