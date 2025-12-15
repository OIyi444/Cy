'''
#Part A
class register():
    def __init__ (self, name, age, membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type

    def getname():
        while True:
            try:
                name = input("Enter your name: ")
                return name
            except TypeError:
                print("Invalid inpur, try again")

    def getage():
        while True:
            try:
                age = int(input("Enter your age: "))
                if age < 12:
                    print("Not eligible for membership")
                elif age >= 12 and age <=60:
                    print("Standard membership granted")
                else:
                    print("Senior membership granted")
                return age
            except TypeError:
                print("Invalid input, try again")

    def getmembership_type():
        while True:
            try:
                membership_type = int(input("1.adult, 2.junior, 3.senior, 4.student, 5.family"))
                if membership_type == 1:
                    return("adult")
                elif membership_type == 2:
                    return("junior")
                elif membership_type == 3:
                    return("senior")
                elif membership_type == 4:
                    return("student")
                elif membership_type == 5:
                    return("family")
                else:
                    print("Please enter(1-5):")
               
            except TypeError:
                print("Invalid input, try again")
    

registeration_info = []

print("==Welcome to Swimming Pool Membership System==")
username = register.getname()
userage = register.getage()
membership = register.getmembership_type()
registeration_info.append(username)
registeration_info.append(userage)
registeration_info.append(membership)
print(f"{username},{userage}, Thanks for become our member: {membership}")
print(registeration_info)
'''

'''
#Part B
class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author:{self.author}")


books ={"title": {"Python 101", "data Science"}, 
        "Auther": {"Phlip Robbins", "jannah Mohd"}}

title = input("Enter book title: ")
author = input("Enter book author: ")
books["title"].add(title)
books["Auther"].add(author)

with open ("books.txt", "w") as file:
    for title, author in books.item():
        file.write (f"{title}: {author}\n")

with open ("books.txt", "r") as file:
    lines = file.readlines()

print("\nBook List from file: ")
for line in lines:
    title, author = line.strip().split(":")
    b = books(title, author)
    b = Book.display_info()
'''