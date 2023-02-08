# * groups all arguments into a tuple


def add(*args):
    sum=0
    for n in args:
        sum+=n
    print(sum)

add(4,6,7,4)

# unlimited keyword arguments 
def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(add=4, plus=8)