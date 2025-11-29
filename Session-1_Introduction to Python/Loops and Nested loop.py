# for loop and while loop are two loops which are there in python

for i in range (10): # range works with int data type with start, stop, step
    print(i)


for i in range (1,10): # range works with int data type with start, stop
    print(i)

for i in range (1,10,2): # range works with int data type with start, stop, step
    print(i)

# Reverse Order

for i in range(10,0,-1): #10,10-1,9
    print(i)


str1 = "123"
for i in str1:
    print(i)


list1 = ["hello",'hi',1]
for i in list1:
    print(i)

# while checks for a conditon to be true to execute while blocks

a = 0
while a < 5:
    print(a)
    a +=1

# Nested loop -> Loop inside loop -> More than one looping is called nested loop
# it could be for loop inside for loop
# or while loop inside for loop

for i in range(1,10):
    while i < 5:
        print(i)
        i += 1