# filter() is used to keep only the element that satisfy a condition. It returns an iterator.
# filter (function, iterator)
# create a function to print age greater than 15 and less than 30.

"""
Below function is a age filter which will filter out age greater than 15 and less than 30
"""
def age_filter(a):
    if a > 15 and a <30:
        return True

def check_for_odd_and_even(a):
    if a % 2 == 0:
        return True

# list_of_ages = [5,10,15]
# age = list(filter(age_filter,list_of_ages))
# print(age)

num = [1,2,3,4,5,6,7]
even_num = tuple(filter(check_for_odd_and_even,num))
print(even_num)