def countfunc(authornames):
    count = 0
    for i in authornames:
        if i == "Akash":
            count += 1
    return count

s = countfunc(['Akash','Shinde','Akash'])
# print(s)

# create decorator
def test_decorator(func):
    def wrapper(*args,**kwargs):
        abc = func(*args,**kwargs)
        print(abc,"   ",func.__name__,"This is decorator function")
        return abc
    return wrapper



@test_decorator
def test_func(a,b):
    return a+b
st = test_func('akash','s')
