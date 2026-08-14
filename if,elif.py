# 🎯 Python Challenge: Age Category Finder
# Write a program that:
# Asks the user to enter their age using input().
# Converts that input to an integer using int().
# Checks the age using if/elif/else.
# Prints the correct message.

# Rules:
# If age is less than 13 → print "You are a child."
# If age is between 13 and 19 → print "You are a teenager."
# If age is 20 or above → print "You are an adult."

age=int(input("Enter the age:"))
if age<13:
    print("You are child")
elif age>=13 and age<=19:
    print("You are a teenager")
else:
    print("You are an adult")