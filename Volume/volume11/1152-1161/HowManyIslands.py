#!/usr/bin/env python
#coding:utf-8



def movable(w,h,x,y,maps):

  result = []

  rx = x + 1
  lx = x - 1
  uy = y - 1
  dy = y + 1

  if (-1 < uy) and (maps[uy][x] == 1):
    result.append((x,uy))

  if (dy < h) and (maps[dy][x] == 1):
    result.append((x,dy))

  if (rx < w):
    if (maps[y][rx] == 1):
      result.append((rx,y))
    if (-1 < uy) and (maps[uy][rx] == 1):
      result.append((rx,uy))
    if (dy < h) and  (maps[dy][rx] == 1):
      result.append((rx,dy))

  if (-1 < lx):
    if (maps[y][lx] == 1):
      result.append((lx,y))
    if (-1 < uy) and (maps[uy][lx] == 1):
      result.append((lx,uy))
    if (dy < h) and (maps[dy][lx] == 1):
      result.append((lx,dy))

  return result

def walk(w,h,x,y,maps):
  result = set()
  target = set()
  target.add((x,y))
  while (len(target) != 0):
    (px,py) = target.pop()
    result.add((px,py))
    for each in movable(w,h,px,py,maps):
      if (not each in result) and (not each in target):
        target.add(each)
  return result

def solve(w,h,maps):
  visited = []
  cnt = 0
  for y,line in enumerate(maps):
    for x,tile in enumerate(line):
      if (tile == 1) and all([(not ((x,y) in land)) for land in visited]):
        island = walk(w,h,x,y,maps)
        if not (island in visited): 
          cnt += 1
          visited.append(island)
  return cnt

def main():
  while True:
    (w,h) = map(int,raw_input().split(" "))
    if (w,h) == (0,0): break
    maps = []
    for y in xrange(h):
      maps.append(map(int,raw_input().split(" ")))
    print solve(w,h,maps)


if __name__ == "__main__":
  main()




