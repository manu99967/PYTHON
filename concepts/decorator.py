# Decorators.
#Extend or modify the behavior of 
## functions or without changing their code
## CALLBACKS<-->

def my_deco(func):
    def wrapper():
        print("Before function run")
        func()
        print("Function completed running")
    return wrapper

@my_deco
def hello():
    print("hello world")

#my_deco(func=hello)()

hello()