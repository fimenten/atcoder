A,B=[int(thing) for thing in input().split(" ")]
for i in range(B):
    if 1+(A-1)*i>=B:
        break
print(i)