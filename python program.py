def func(*a):
    print("this is python",a)
func(1,2,3)
def func(**a):
    print(a)
func(a=1,b=2)
def outer():
    print("outer hi")
    def inner():
        print("inner hi")
    inner()
outer()
def add(a,b):
    print(a+b)
add(2,3)
def add(a=7,b=8):
    print(a+b)
add(5,4)







