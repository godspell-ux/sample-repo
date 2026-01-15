print("Hello World!!!")

name = input("Enter your name: ")

if name == "James":
    print("You typed your first name.")
elif name == "Madriaga":
   print("You typed your last name.")
else:
   print("You typed neither your first nor last name.")

#LIST OPERATIONS
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#TUPLE OPERATIONS
coordinates = (10.0, 20.0)
print("X Coordinate:", coordinates[0])
print("Y Coordinate:", coordinates[1])

#SET OPERATIONS
unique_numbers = {1, 2, 3, 4, 5}
unique_numbers.add(6)
print(unique_numbers)

#DICTIONARY OPERATIONS
person = {"name": "James", "age": 21}
person["city"] = "PH"
print(person)

#FUNCTION DEFINITION AND CALL
def greet_user(username):
    print("Hello, " + username + "!")
greet_user(name)

#LOOP EXAMPLE
def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")