from functools import reduce

add_ = lambda a,b : a+b
lst = [1,2,3,4,5]
# print(list(map(add_,lst)))

print(reduce(add_,lst,10))

