# lambda is an anonymous function which are created using lambda keyword.
# lambda functions are created on a fly.
# syntax for lambda
# _my_lambda_fun = lambda argument:expression


# Write program to square two numbers
# def square_num(a):
#     return a**2
#
# print(square_num(5))

# num_sqr = lambda y : y**2
# print(num_sqr(4))

# Write program to add two numbers
# def addition_of_two_numbers(a,b):
#     return a+b
#
# print(addition_of_two_numbers(10,20))
#
# num_addition = lambda a,b : a+b
# print(num_addition(11,12))


# Write a program to count number of digits in a number.. len()

# def count_num(_value):
#     return len(_value)

# _value = str(input("Enter the letter which need will be counted using len(): "))
# print(count_num(_value))

len_of_str = lambda x : len(x)
print(len_of_str(input("Enter the letter which need will be counted using len(): ")))

# Write a program to find the maximum of three numbers (max() function )

# max_num =  lambda y : max(y)
# print(max_num('193766'))

max_num = lambda x,y,z : max(x,y,z)
print(max_num(10,20,30))

# Write a program to check a given number is odd or even



