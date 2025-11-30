 # lists are a data type which is a collection of items of same or another data type.
 # lists are created with [] and comma (,) separated.
 # lists are mutable.
 # lists returns items in an ordered sequence.

fruit_items = ['orange','banana','grapes','apple','watermelon','guava','sapota'] #-> fruit_items[0],[1]

# finding length of list
# length_of_list = len(fruit_items)

# fetching single item of a given list
# print(fruit_items[0]) # -> use indexing for fetching an item from a particular position
# print(fruit_items[1])
# print(fruit_items[2])
# print(fruit_items[3])

# printing two items in a single print
# print(fruit_items[0],fruit_items[1])

# for fetching and printing each item at a time
# for i in fruit_items:
#     print(i)

# for fetching and printing each item at a time using indexing
# for i in range(length_of_list): # for i in range(6):
#     print(fruit_items[i])       #       print(i)


# fetching and printing value until a condition
# for i in range(length_of_list): # for i in range(6):
#     print(fruit_items[i])       #       print(i)


# break is used to finish looping
# for i in range(length_of_list):
#     if i >= 2:
#         break
#     print(fruit_items[i])

# continue is used to skip iteration

# for i in range(length_of_list):
#     if fruit_items[i] == 'banana' or fruit_items[i] == 'guava' :
#         continue
#     print(fruit_items[i])

fruit_items = ['orange','banana','grapes','apple','watermelon','guava','sapota']
# print(fruit_items)

# append () is used for adding item at the end of list
fruit_items.append('papaya')
print(fruit_items)

# extend() is used to combine lists into one
fruit_items.extend(['strawberry','blueberry'])
print(fruit_items)

# insert() is used to insert item at a particular index
fruit_items.insert(3,'litchi')
print(fruit_items)

# pop() is used to remove item from a list
fruit_items.pop()

# pop(6) is used to remove item from a list in sixth index position
fruit_items.pop(6)
print(fruit_items)

# clear() is used for emptying a list
# fruit_items.clear()
# print(fruit_items)

# remove() will remove item from list
fruit_items.remove('sapota')
print(fruit_items)