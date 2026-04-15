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

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

hello()
greet("Karan", "Hii")

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

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(4,3))

