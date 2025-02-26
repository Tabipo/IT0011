fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: "))
fullname = fname + " " + lname
slicename = fullname[0:3]
print()
print("Full Name: ", fullname)
print("Sliced Name: ", slicename)
print("Greeting Message: Hello {}! Welcome. You are {} years old.".format(slicename, age))