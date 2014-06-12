#!/usr/bin/env python2.7
#coding:utf-8

(a,b) = map(int,raw_input().split(" "))
if a < b:
    print "a < b"
elif a > b:
    print "a > b"
else:
    print "a == b"
