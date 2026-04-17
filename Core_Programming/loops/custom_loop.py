num=[1,2,3]
#  fetch the iterator
iter_num= iter(num)

# calling next funuction
# print(next(iter_num))
# print(next(iter_num))
# print(next(iter_num))
# print(next(iter_num))

def custom_forloop(iterable):
    iterator =iter(iterable)
    
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

a=[1,2,3,4]
b=(4,5,6)
c={1,2,3,4,5,6}
d= range(1,10)
e={"name":"karan", "age": 20}

custom_forloop(d)