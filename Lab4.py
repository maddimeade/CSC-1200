#Maddison Davenport
#Lab 4
#2/13/2020
#Part 1 - While loop/ decimal to binary
#Part 2 - For loop/ pyramid of letters

baseTen = int(input("Enter a base 10 number: "))
s = ""

while baseTen>0:
  s = str(baseTen%2) + s
  baseTen = baseTen//2

print(s)

num = int(input("\nEnter a number: "))
letter = input("Enter a letter: ")

j = "" 

for i in range(0, num):
  j = j + letter
  print(j)