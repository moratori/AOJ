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


def solve(n):
  """
    simple way and slow
  """
  cnt = 0
  for t in xrange(n+1,2*n+1):
    if primep(t): cnt += 1
  return cnt


def main():
  while True:
    n = int(raw_input())
    if n == 0 : break
    print solve(n)



if __name__ == "__main__":
  main()
