#!/usr/bin/env python
#coding:utf-8



import sys



def movable(w,h,pos,room):
  result = []
  (x,y) = pos
  rx = x + 1
  lx = x - 1
  dy = y + 1
  uy = y - 1

  if (rx < w) and (room[y][rx]  != "#"):
    result.append((rx,y))

  if (-1 < lx) and (room[y][lx] != "#"):
    result.append((lx,y))

  if (dy < h) and (room[dy][x]  != "#"):
    result.append((x,dy))

  if (-1 < uy) and (room[uy][x] != "#"):
    result.append((x,uy))

  return result


def solve(w,h,pos,room):
  visited = set()
  target  = set()
  counter = 0
  target.add(pos)
  while (len(target) != 0):
    now = target.pop()
    visited.add(now)
    counter += 1
    for each in movable(w,h,now,room):
      if (not each in visited) and (not each in target):
        target.add(each)

  return counter


def main():
  while True:
    (w,h) = map(int,raw_input().split(" "))
    if ((w == 0) and (h == 0)) : break
    room = []
    for y in xrange(h):
      width = []
      for x in xrange(w):
        tile = sys.stdin.read(1)
        if ( tile == "@") : 
          pos = (x,y)
        width.append(tile)
      room.append(width)
      sys.stdin.read(1)
    print solve(w,h,pos,room)


if __name__ == "__main__": main()
