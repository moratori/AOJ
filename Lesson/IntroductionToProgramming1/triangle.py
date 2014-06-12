
import math

(a,b,C) = map(int,raw_input().split(" "))
rad = math.radians(C)
h = b * math.sin(rad)
c = math.sqrt((a ** 2 + b ** 2) - 2 * a * b * math.cos(rad))
print "%f\n%f\n%f" %(a * h * (1/2.0) , a+b+c,h)
