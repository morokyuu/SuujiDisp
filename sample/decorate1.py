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
a = 5 

def refine(func):
    def wrapper(value):
        func(value)
        print(a)

        global d1,d10
        d1 = a % 10
        d10 = a // 10
        print(f'{d10},{d1}')
    return wrapper ## this is essential

@refine
def setv(value):
    global a
    a += value

setv(23)
