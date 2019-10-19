string="""
A	4
E	3
G	6
I	1
O	0
S	5
Z	2"""

enc_dict={}
for thing in string.split("\n"):
    if len(thing)!=0:
        char,num=thing.split("\t")
        print(char)
        enc_dict[char]=num

raw_string="TEST"
enc_string="".join([enc_dict[thing] if thing in enc_dict else thing for thing in list(raw_string)])
print(enc_string)