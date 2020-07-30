def decorate_func(func):  #Decorator function
    def inner():
        print("I am decorated")
        func()
    return inner

@decorate_func
def ordinary():
    print('I am ordinary')


def smart_divide(func):
    def inner(a,b):
        print("{} is dividing by {}".format(a,b))
        if b == 0:
            print("Whoops! cannot divide")
            return
        func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b
