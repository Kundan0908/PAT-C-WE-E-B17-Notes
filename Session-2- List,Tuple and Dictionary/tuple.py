# tuple are a data type which is a collection of items of same or another data type.
# tuple are created with () and comma (,) separated.
# tuple are immutable.
# tuple returns items in an ordered sequence.

fruit_items = ('orange','grapes','apple','watermelon','guava','sapota','banana')

# finding length of list
length_of_tuple = len(fruit_items)

# fetching single item of a given tuple
print(fruit_items[0]) # -> use indexing for fetching an item from a particular position
print(fruit_items[1])
print(fruit_items[2])
print(fruit_items[3])

# printing two items in a single print
print(fruit_items[0],fruit_items[1])

# for fetching and printing each item at a time
for i in fruit_items:
    print(i)

# for fetching and printing each item at a time using indexing
for i in range(length_of_tuple): # for i in range(6):
    print(fruit_items[i])       #       print(i)

# count() is used to find the count of a particular item in a tuple
print(fruit_items.count('banana'))

# index() is used to find the index position of a given item from a tuple
print(fruit_items.index('banana'))