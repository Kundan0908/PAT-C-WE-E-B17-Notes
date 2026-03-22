# dic =   {
#     "username_": "standard_user",
#     "password": "secret_sauce",
#     "username": "standard_user1",
#     "password_": "secret_sauce"
#   }

# for each_val in dic:
#     print(each_val) #username,password,username_,password_
#     print(dic[each_val]) # dic_var[key] -> value

# for each_val in dic.values(): # for printing all value of a dictionary using variable_name.value()
#     print(each_val)
#
# for each_val in dic.keys(): # for printing all keys of a dictionary using variable_name.keys()
#     print(each_val)

# for each_key, each_value in dic.items():
#     print(each_key,each_value)

# print(dic.get('usrname'))

# name = ['Kundan','kumar'] # print count of each alphabet of your name in a dictionary format -> {k=1,u=1---}
# name_dic = {}

# get length of the variable
# start a for loop
# get count of each alphabet
# store key and its count as a value in a dictionary

# for each_alphabet in name:
#     name_dic[each_alphabet] = name.count(each_alphabet) # {'k':1,'u':1,'n':2,'a':1,'d':1}
# print(name_dic)

# for each_alpha in name[0]: # Kundan
#     print(each_alpha)

# credentials = [{"username": "standard_user","password": "secret_sauce"},{"username": "standard_user_2","password": "secret_sauce"}]
# for each_credential in credentials:
#     print(each_credential.get('username'))
#     print(each_credential['username'])
