friends = ["madhan", "naveen", "vijay", "ajay", "sekar"]
print(friends)
print(friends[2])  # index start from 0
print(friends[-2])  # reverse index starts from -1
print(friends[1:])  # access range of elements in list
print(friends[1:4])
friends[-1] = "gnana sekar"
print(friends)

lucky_numbers = [3, 5, 1, 7, 3, 9, 10]
friends.extend(lucky_numbers)  # appends list to another list
print(friends)
friends.append("dinesh")  # append an element at the end of the list
print(friends)
friends.insert(1, "harish")  # insert elements in the middle
print(friends)
friends.remove(1)  # removes particular index
print(friends)
friends.pop()  # to remove last element
print(friends)
print(friends.index("ajay"))  # finds index of the given element
lucky_numbers.sort()  # sorts the list
friends = ["madhan", "naveen", "vijay", "ajay", "sekar"]
friends.sort()  # a list with various data types cannot be sorted
print(lucky_numbers)
print(friends)
lucky_numbers.reverse() # reverses the list
print(lucky_numbers)
lucky_numbers_copy = lucky_numbers.copy()
lucky_numbers.append(100)
lucky_numbers_copy.append(10000)
print(lucky_numbers)
print(lucky_numbers_copy)