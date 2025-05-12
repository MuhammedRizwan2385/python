#store the names and birthdays of n persons into a dictionary and read a name to search and return the birthday date corresponding to that name
n=int(input("enter the limit: "))
birthday_dict={}
for i in range(n):
    name=input(f"Enter the name of person {i+1}: ")
    birthday=input(f"Enter the birthday of person {i+1}: ")
    birthday_dict[name]=birthday
name_to_search=input("enter the name to search: ")
print("The birthday is on : ", birthday_dict.get(name_to_search,"This name doesn't exist") )
