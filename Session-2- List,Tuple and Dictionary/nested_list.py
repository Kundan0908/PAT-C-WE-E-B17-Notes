sorted_lst = [-3,1,2,4,6]
for i in range(len(sorted_lst)):
    print(f"I am from first for loop with value {sorted_lst[i]}") # -3
    for j in range(i+1,len(sorted_lst)): #1,2,4,6
        print(f"I am from second for loop with value {sorted_lst[j]}")