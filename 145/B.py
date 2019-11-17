N=int(input())
S=input()
if N%2==1:
    print("No")
elif N==2:
    if S[0]==S[1]:
        print("Yes")
    else:
        print("No")
else:
    if S[0:int(N//2)-1]==S[N//2:N-1]:
        print("Yes")
    else:
        print("No")
