weight = float(input("enter your wieght in kg: "))
height = float(input("enter your height in meters: "))

bmi = weight / ( height * height )
print("your bmi is: ", bmi)

if (bmi <= 18.5):
    print("Underwieght")
elif (bmi <= 24.9):
    print("normal weight")
elif (bmi <= 29.9):
    print("Over weight")
else:
    print("obesity")

number = input("eneter a float number: ")

try:
    number = float(number)
    print("The number is: ", number)
except:
    print("invalid number")
