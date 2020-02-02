def yes():
    print(1)
def no():
    print(0)


X=int(input())
left,right=divmod(X,100)
left_min=0
r=right
for i in range(0,5):
    i=5-i
    count,r=divmod(r,i)
    left_min=left_min+count
if left>=left_min:
    yes()
else:
    no()