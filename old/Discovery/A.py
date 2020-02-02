juni=[int(thing) for thing in input().split(" ")]
shokin=0
for x in juni:
    if x==1:
        shokin=shokin+300000
    elif x==2:
        shokin=shokin+200000
    elif x==3:
        shokin=shokin+100000
if juni[0]==juni[1] and juni[0]==1:
    shokin=shokin+400000
print(shokin)