# Timing Functions with Decorators 
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start= time.time()
        result= func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} Execution time: {end-start} seconds")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

# example_function(2)


#Debugging function calls
def debug(func):
    def wrapper(*args,**kwargs):
        args_value=', '.join(str(arg) for arg in args)
        kwargs_value= ', '.join(f" {k}={v}" for k,v in kwargs.items() )
        print(f"Function {func.__name__} called with arguments: {args_value} and keyword arguments: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("hello")

# @debug
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# hello()
# greet("Karan", "Hii")

# Cache return values
# Memoization 
def cache(func):
    cache_value={}
    print(cache_value)
    def wrapper(*args,**kwargs):
        if args in cache_value:
            return cache_value[args]
        
        result= func(*args,**kwargs)
        cache_value[args]=result
        return result

    return wrapper

# @cache
# def long_running_function(a,b):
#     time.sleep(4)
#     return a+b

# print(long_running_function(2,3))
# print(long_running_function(2,3))
# print(long_running_function(4,3))



# checking datatype

def check_datatype(datatype):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            if type(args[0]) == datatype:
                func(*args,**kwargs)
            else:
                raise TypeError("Wrong data type")
        return inner_wrapper
    return outer_wrapper

@check_datatype(int)
def square(n):
    print(n**2)

@check_datatype(str)
def greet(name,age):
    print("Hello", name, "Your age is ", age)

# greet("karan",20)

# square(2)

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@my_decorator
def square(n):
    print(n**2)
    
# square(10)

def is_admin(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            print("Access denied")
    return wrapper

@is_admin
def role(admin):
    print("Logging as Admin")

# role("admin")

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello")

# greet()


# Multiple decorators
def decor1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decor2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decor1
@decor2
def greet():
    print("Hello")

greet()