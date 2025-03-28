# parametr *args
# example
def add(*args):
    sum = 0
    for n in args:
        sum += args
    print(sum)

# użycie **kwargs  - dictionary

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)