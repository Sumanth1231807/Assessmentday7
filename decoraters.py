def numbers(fun):
    def inner(a,b):
        print(a)
        print(b)
        return fun(a,b)
    return inner
@numbers
def printnumber(a,b):
    print(a*b)
printnumber(6,7)