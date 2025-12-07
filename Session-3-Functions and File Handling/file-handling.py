# file handling is a way to handle text files in python.
# Operation supported
    # 1. read
    # 2. write
    # 3. append
    # 4. read and write


# Write into an empty file
# path = 'test.txt' # provide path of the file
# f = open(file=path, mode='w') # open a file using open(file= file path,mode = mode for file to open)
# f.write("This line is written using python") # write something in a file
# f.close() # close file

# Reading content from file
# path = 'C:/Users/Kundan_Kumar/PycharmProjects/PAT-B17/Session-3-Functions and File Handling/test.txt'
# f = open(file=path, mode='r')
# file_content = f.read()
# print(file_content)

# Append newlines in a file
path = 'test.txt' # provide path of the file
f = open(file=path, mode='a') # open a file using open(file= file path,mode = mode for file to open)
f.write("\nThis line is written using python") # append content in a new line. \n is used for moving cursor to new line.
f.close() # close file