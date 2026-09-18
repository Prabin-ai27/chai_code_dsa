from functools import wraps
def my_decorator(func):
    @wraps(func)
    def warpper():
        print('Before function')
        func()
        print('After function')
    return warpper
@my_decorator
def hello():
    print('Hello !')
    pass
hello()
print(hello.__name__)