def input_int_list():
    return [int(thing) for thing in input().split(" ")]
N,M=input_int_list()
ken_toshi=[input_int_list() for _ in range(M)]
ken_shinotoshi={i+1:sorted([thing[1] for thing in ken_toshi if thing[0]==i+1]) for i in range(N)}
ken_toshinum={i+1:0 for i in range(N)}
def normalize(num:int):
    return str(num).zfill(6)

for ken,toshi in ken_toshi:
    ans_left=normalize(ken)
    the_index=ken_shinotoshi[ken].index(toshi)
    ken_shinotoshi[ken].pop(the_index)
    ans_right=normalize(the_index+1+ken_toshinum[ken])
    print(ans_left+ans_right)