user_data ={}
while True:
    name= input ("Enter the name or type 'stop' to stop the program: ")
    if name == "stop":
        break
    age = input (f"Enter the age for {name}: ")
    if not age.isdigit():
        print("Please enter a valid number for age. For example 23 ")
        continue
    user_data[name]=int(age)

searchname= input("Enter the name to search: ")
age = user_data.get(searchname)
if age:
    print(f"{searchname} is {age} years old")
else:
    print(f"No infomation was found for {searchname} in our database")