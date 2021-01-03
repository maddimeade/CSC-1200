import random

count = 1
randomNum = random.randint(0,100)
userNum = int(input("Guess a random number between 1 and 100: "))

while(userNum != randomNum):
  if(count > 7):
    print("\nActually, never mind, you suck loser!")
    break
  elif(userNum < randomNum):
    count = count+1
    userNum = int(input("\nValue too low, try again: "))
  else:
    count = count+1
    userNum = int(input("\nValue too high, try again: "))

if(userNum == randomNum):
  print("\nGood job! You guessed the number! Big Brain!")