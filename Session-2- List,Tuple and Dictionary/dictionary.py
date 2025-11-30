# dictionary are a data type which is defined using key:value pair
# dictionary are created with {} and comma (,) separated.
# dictionary are mutable.

dict_item = {'Name':'Kundan','Batch':'PAT-B17'}
print(dict_item)

# pop() is used to remove item based on key provided
# dict_item.pop('Batch')
# print(dict_item)

# get() is used to fetch value of a particular key
dict_item.get('Name')
print(dict_item)

# clear() is used to clear/emptying a dictionary
# dict_item.clear()
# print(dict_item)

# for adding / updating new key:value in a dictionary
dict_item['Role'] = 'Mentor'
print(dict_item)

dict_item['Batch'] = 'PAT-B11'
print(dict_item)