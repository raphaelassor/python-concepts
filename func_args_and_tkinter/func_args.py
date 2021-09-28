# Default Values
def my_func(a=1, b='A'):
    print(a, b)


my_func()


# unlimited arguments
def add(*args):
    print('IT IS A TUPLE!', args)
    sum = 0
    for n in args:
        sum += n
    return sum


sum = add(1, 4, 56, 7, 8, 5, 3)
print(sum)


# unlimited keyword argument
def calculate(num, **kwargs):
    print('A DICTIONARY MAPPING THE ARGUMENTS BY KW AND VALUE', kwargs)
    if kwargs.get("add"):
        print(num + kwargs["add"])
    if (kwargs.get("multiply")):
        print(num * kwargs["multiply"])
    if (kwargs.get("divide")):
        print(num / kwargs["divide"])


calculate(5, add=4, multiply=5,nonsense="hello")
