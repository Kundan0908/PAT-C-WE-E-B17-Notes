# string manipulation is changing/modifying string output.
# string slicing and string manipulation are same

str_var = 'hello,hi!how are you doing?' #-> Every new variable gets a memory allocation along with address
print(len(str_var)) # len() is used to find the length of the variable

# when assigning positions this start from 0,1,2,--- til the pos of last item is allocated
print(str_var[0])
print(str_var[len(str_var)-1]) # str_var[25]

# string slicing is declared using [start:stop:step]

print(str_var[9:])
print(str_var[9:19]) # starting position gets printed but stopping position is not
print(str_var[9:20])
print(str_var[0::2]) # -> 0 gets printd all the time, next printing would be 0+2 = 2, 2+2=4