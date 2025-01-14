try:
    age = int(input("How old are you?: "))
    print(f"You are {age} years old")
except ValueError:
    print("Pls insert a number as your age")