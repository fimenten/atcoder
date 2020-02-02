N=int(input())
S=list(input())
alphabets=list(str("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"))
a=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
narabikae=alphabets[N:N+26]
print("".join([narabikae[a.index(thing)] for thing in S]))