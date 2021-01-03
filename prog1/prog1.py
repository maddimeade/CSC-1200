#prog1.py
#Maddison Davenport
#Computer Science
#2/4/2020
#Monthly Budget Program

#inputting name
name =  input("Enter your name: ")

#printing name
print("\nHello, " + name)

#inputting monthly income
monthlyIncome = float(input("\nPlease enter your monthly income: $"))

#specifying start of input for expenses
print("\nPlease enter your monthly expenses!")

rent = float(input("\nPlease enter your monthly rent: $"))
water = float(input("Please enter your monthly water bill: $"))
electric = float(input("Please enter your monthly electric bill: $"))
phone = float(input("Please enter your monthly phone bill: $"))
internet = float(input("Please enter your monthly internet bill: $")) 
car = float(input("Please enter your monthly car payment: $"))
gas = float(input("Please enter your monthly gas cost: $"))
other = float(input("Please enter your other monthly expenses: $"))

#calculating the total of all expenses
totalExpenses = rent + water + electric + phone + internet + car + gas + other

#finding total by subtracting  monthly income by monthly expenses
totalMoney = monthlyIncome - totalExpenses

#printing user's monthly total money after expenses
print("\n" + name + ", you have $" + str(totalMoney) + ".")

#if they have a negative amount, printing advice
if totalMoney < 0:
  print("You should manage your money better!")

#if they have 0 or positive balance, printing congrats
else:
  print("Good Job!")
