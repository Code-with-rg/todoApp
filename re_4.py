import re

name = input("Enter Name : ")

match = re.match(r"((\w{3,}))", name)


print(match)
# x = "name is True" if match else "this is not valid name"

# print(x)pu
