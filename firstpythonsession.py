username = 'kundan'
print(type(username))
username = 123
print(type(username))
username = True
print(type(username))
username = 1.0
print(type(username)) #-> type function is used to find the data type
print(f"Hi! {username} welcome to python learning")

# Operators
# arithmatic operators -> +,-,*,/,//
a = 10 # '=' is used to assign right hand value to a declared variable
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b) # division -> result will be in float
print(a//b) # floor division -> result will be in integer

# boolean opeartors -> True, False
c = True
d = False
print(c)
print(d)

# conditonal operators -> <,>,!=,==, if, else, while
e = 30
f = 40
print(a<b)
print(a>b)
print(a!=b) # Not equals to
print(e==f) # == is used for checking left variable value with right variable value
print(id(e)) # id() is used for checking address where value of variable is stored

# logical opeartors -> and,or,not
h = 'boy'
i = 'boy'
# print(h and i)
# print(h or i)
print (h is not i) # boy is not a girl - True, A 'boy' is not a 'boy'



# conditonal statements -> if, else, elif, while
# if-else block
g = 50
if a == e:
    print(True)
else:
    print(False)

# if-elif-else block
if a > b:
    print("a is greater than b")
elif b > g:
    print("b is greater than g")
else:
    print("g is the greatest")

i = 0
while i < 5:
    print('Hello')
    i += 1 # same as writing i = i+1


print("Hello World")


# This isa single line comment
print("This is python learner program!")

"""
Hi
This
is
a
multiline
comments
"""