# Generators are functions which return an iterator (sequence of items).
# These functions use yield instead of return.
# They help save memory space.

# normal function contains 'return' statement -> which returns the value and
# finishes the function execution and skips if anything is written after return statement

# generator function contains 'yield statement -> which pauses execution to return iterator value and
# then resumes the next step defined inside that generator function.
# It requires for loop to return object one by one

def addition(num):
    start = 0
    while start < num:
        yield start #0,2,4,6,8
        break

# print(addition(10))
for i in addition(10):
    print(i)

# Tc1 - login
# TC2 - add item to cart
# TC3 - checkout
# TC4 - log out