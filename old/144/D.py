import math
a,b,x=[int(i) for i in input().split(" ")]

V=a*a*b
if x>0.5*V:
    sita=math.atan(2*(V-x)/a/a/a)
else:
    sita=math.atan(a*b*b/2/x)
print(math.degrees(sita))
