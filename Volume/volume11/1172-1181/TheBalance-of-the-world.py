#!/usr/bin/env python
#coding:utf-8



OPEN = ["(","["]
CLOSE = [")","]"]
MAPPING = {")":"(" , "]":"["}

def solve(line):
  stack = []
  for char in line:
    if char in OPEN:
      stack.append(char)
    elif char in CLOSE:
      if not stack : 
        print "no"
        return
      expected = MAPPING[char]
      act = stack.pop()
      if expected != act : 
        print "no"
        return
  if not stack :
    print "yes"
  else:
    print "no"

def main():
  while True:
    line = raw_input()
    if line == "." : break
    solve(line)

if __name__ == "__main__":
  main()
