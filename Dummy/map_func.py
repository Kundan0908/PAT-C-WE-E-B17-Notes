# Write a program to check a given number is odd or even
result = lambda x: x%2 == 0
lst = [1,2,3,4,5,6]
num_even = map(result,lst)
for i in num_even:
    print(i)