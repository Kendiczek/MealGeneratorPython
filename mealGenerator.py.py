
import random
from datetime import date

with open("breakfast.txt","r") as file_br:
    breakfast = file_br.read().splitlines()
with open("lunch.txt","r") as file_lu:
    lunch = file_lu.read().splitlines()
with open("dinner.txt","r") as file_din:
    dinner = file_din.read().splitlines()
with open("light_mid_afternoon_meal.txt","r") as file_lig:
    light_mid_afternoon_meal = file_lig.read().splitlines()
with open("supper.txt","r") as file_supp:
    supper = file_supp.read().splitlines() 

today = date.today()

print(" ")
print("Your today's menu for",today,"is below:")
print(" ")
print("1st meal: ",(random.choice(breakfast)))
print("2nd meal: ",(random.choice(lunch)))
print("3rd meal: ",(random.choice(dinner)))
print("4th meal: ", (random.choice(light_mid_afternoon_meal)))
print("5th meal: ",(random.choice(supper)))
print(" ")