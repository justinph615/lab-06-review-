
import sys #coding: utf-8

print("Welcome to BMI: Body Mass Index Calculator")

userWeight = input("Enter your weight (in pounds): ")
userHeight = input("Enter your height (in inches): ")
userHeightFloat = float(userHeight)

myBMIpy = round((703 * float(userWeight)) / (userHeightFloat * userHeightFloat), 2)
print("Your BMI is " + str(myBMIpy) + "%")


