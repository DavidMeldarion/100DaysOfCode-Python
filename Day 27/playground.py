from re import X


def add(*args):
    x=0
    for n in args:
        x+=n
    return x
print(add(1,5,3))
