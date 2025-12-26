# Exception Handling
# Exceptions are something whose occurance are rare but can lead to code failure when encountered
# to handle these kind og exceptions we use exception handling concept in programming.

# Jouney is to go from A-B-C
# Divide a given number and multiply reminder by 2
# try:
#     numerator = int(input("Enter a number for divison"))
#     denominator = int(input("Enter a number to divide"))
#     result = numerator/denominator
#
# except ZeroDivisionError:
#     print("division by zero is not possible, Please divide by num greater than 0")
#
# except Exception as e:
#     print(e)
#
# else:
#     print(f'the result of division is {result}')
#
# finally:
#     # Reaching C
#     print(f"Executing finally block")


# try: if error comes in the try statement then except block gets executed and then finally block will be executed
# try : if no error comes in the try statement then else block gets executed and then finally block gets executed
# try -> except -> finally

# Raise Exception

num = int(input("Enter value to divide number 10"))
if num>0:
    result = 10/num
    print(f'{result}')
else:
    raise Exception ("The number should be greater than 0")

