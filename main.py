number = int(input("Enter the number to check"))
print("Number to be checked :", number)

if number%2==0 :
    print("This in an even number")

else:
    print("This number is odd")

height = float(input("Enter your height in cm: "))
weight = float(input("enter your weight in kg:" ))

BMI = weight / (height/100)**2

print("Your BMI is" , BMI)

if BMI <= 18.4:
    print("you are underweight.")
elif BMI<= 24.9:
    print("you are healthy")
elif BMI<= 29.9:
    print("you are overweight")
elif BMI<= 34.9:
    print("you are severel over weight")
elif BMI<= 39.9:
    print("you are obese")
else:
    print("you are severly obese")


num = int(input("Enter number to check"))

if num>50:
  print("number is grater than 50")
  if num%2==0:
    print("and it is even too")
  else:
    print("and it is odd")

else:
 print("This number is lesser that 50") 

import datetime

current_time = datetime.datetime.now()

print("Timenow at greenwich meridian is :", end = "")
print(current_time)

import calendar
print("/n", calendar.calendar(2024))