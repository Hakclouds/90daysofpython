from math import sqrt
def sqrtcalculator():
   while True:
        try:
            number=int(input("Enter the number you are finding its square root: "))
            result= sqrt(number)
            print(f"The square root of {number} is {result} ")
        except  ValueError:
            print("You need to enter a postive number ")
        if number >=1:
            break
sqrtcalculator()