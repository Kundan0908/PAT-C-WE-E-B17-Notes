# closure functions are called nested functions

def addition(x):
    print(f"This is from addition function where value of x is {x}")
    def wrapper(y):
        return x + y
    total = wrapper(20)
    print(total)
    return total


print(addition(5))