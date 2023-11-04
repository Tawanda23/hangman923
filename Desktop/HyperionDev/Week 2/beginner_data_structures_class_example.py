

my_list = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

#my_list.append([13, 14, 15])
#my_list.append([20, 23, 25])
#my_list.append([10, 11, 12])

#print(my_list[-3][-2]) # this prints out items in list 1 and item 3 (number 6)

#print(len(my_list)) #this counts the number of lists inside the list which is 3 for this example
#to print backwards, use the print(my_list[-3][-2])


#to add a row into a specific position, use the following:

#my_list.insert(0, [13, 14, 15])

print(my_list)

#changing a value

my_list[2] = [100, 200, 300] # this replaces the original list with a new list. you can also change one value in the list if need be

#LOOPING OVER A LIST

for row in my_list:
    for element in row:
        print(element, end=' ')
    print()

