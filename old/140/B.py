s=[i for i in list(input())]
t=True
for i in range(len(s)):
    if i %2==0:
        if s[i]=="L":
            t=False
            break
    else:
        if s[i]=="R":
            t=False
            break

if t:
    print("Yes")
else:print("No")