import pathlib
dir_name=input("コンテストの名称を入力")


if pathlib.Path(dir_name).exists():
    raise FileExistsError

pathlib.Path(dir_name).mkdir()

default="default.py"

with open(default) as f:
    t=f.read()

for char in "A<B<C<D<E<F".split("<"):
    p=pathlib.Path(dir_name)/pathlib.Path(char+".py")
    with open(p,mode="w+") as f:
        f.write(t)
