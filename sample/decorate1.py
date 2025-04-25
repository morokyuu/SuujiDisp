def log(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} run')
        return func(*args, **kwargs)
    return wrapper

class MyClass:
    @staticmethod  # outer one
    @log
    def static_hello():
        print('static hello')

    @classmethod # inner one
    @log
    def class_hello(cls):
        print('class hello')

MyClass.static_hello()
MyClass.class_hello()


## basic
d1 = 0
d10 = 0

def refine(func):
    def wrapper(value):
        print(value)
        a = func(value)
        print(a)
    return wrapper ## this is essential

@refine
def setv(value):
    global d1,d10
    d1 = value % 10
    d10 = value // 10
    return d10,d1

setv(23)
