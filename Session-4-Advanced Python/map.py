# Write a program using map() to square a list of numbers
# Write a program using map() function convert all strings into upper case """

# map() is used for generating values of an iterable using a function

# def square_num(a):
#     return a**2

list_1 = [1,2,3,4,5,6,7,9]

num_sqr = lambda y : y**2
# print(num_sqr(4))

sqr_num = list(map(num_sqr,list_1))
print(sqr_num)

