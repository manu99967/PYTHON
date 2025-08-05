# Decorators.
## Extend or modify the behavior of 
## functions or without changing their code
## CALLBACKS<-->



def my_deco(fn):
    def wrapper():
        print("Decorator before calling function")
        fn()
        print("Decorator after calling function")
    return wrapper

@my_deco
def hello():
    print("hello world")

@my_deco
def greet():
    print("Greetings from above")



#result the 
# greet()
# hello()
#hello()-> my_deco(hello) -> wrapper -> wrapper()
# my_deco(hello)()