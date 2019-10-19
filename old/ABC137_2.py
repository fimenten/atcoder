K,X=[int(a) for a in str(input()).split(" ")]
s=X-(K-1)
print(" ".join([str(s+ a) for a in range(2*K-2)]))