#Lambda funtion examples...

who_is_grater = lambda a, b: a if a > b else b
print(who_is_grater(10, 25))
#############################################################
# lambda + map() funcionality
names = ["alice", "bob", "charlie"]
uppercase = list(map(lambda i:i.upper(), names))
print(uppercase)
#############################################################
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [i for i in numbers if i%2==0]
print(even_numbers)
square_list = (list(map(lambda i:i*i,even_numbers)))
print(square_list)