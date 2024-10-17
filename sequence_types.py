my_list = [200, 15, "Programming", 1+2, "Lab 3"]
print(len(my_list))
my_list.append(7)
my_list.insert(0,"computing")
my_list.remove(7)
len(my_list)
print(my_list[0])
my_list[1] = 100
print(type(my_list))
my_tuple = tuple(my_list)
print(type(my_tuple))
print(my_tuple[0]) 
print(len(my_tuple))
another_tuple = (5,13,24)
joined_tuple = my_tuple + another_tuple
print(joined_tuple)