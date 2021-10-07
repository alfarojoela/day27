def add(*args):  #the *args as a tuple
    total = 0
    for number in args:
        total += number
    print(total)

    #**kwargs is key word arguments  creates dictionary
def calculate(n, **kwargs):
    print(type(kwargs))

    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]  #adds (2+3) * 5
    n *= kwargs["multiply"]
    print(n)

    #alternative to above loop:
   # print(kwargs["add"])

class Car:
    def __init__(self, **kw):
        #if value absent when object initialized error will occur.
        # self.make = kw["make"]
        # self.model = kw["model"]

        #below helps with avoiding above error if value is missing
        self.make= kw.get("make")
        self.model=kw.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)


