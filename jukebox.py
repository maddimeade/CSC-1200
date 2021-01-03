print("Welcome to the Jukebox!\n")

choice = int(input("Please enter one of the following options:\n     1. Classic Rock\n     2. Alternative\n     3. Pop\nChoice: "))

#Classic Rock
if choice == 1:
	songChoice = int(input("\n\nPlease choose a song\n     1. Dreams - Fleetwood Mac\n     2. Bohemian Rhapsody - Queen\n     3. Wish You Were Here - Pink Floyd\nChoice: "))
	if songChoice == 1:
	  print("\nNow Playing: Dreams - Fleetwood Mac")
	elif songChoice == 2:
	  print("\nNow Playing: Bohemian Rhapsody - Queen")
	elif songChoice == 3:
	  print("\nNow Playing: Wish You Were Here - Pink Floyd ")
	else:
	  print("Invalid song option. Try again later.")

#Alternative
elif choice == 2:
	songChoice = int(input("\n\nPlease choose a song\n     1. Use Somebody - Kings of Leon\n     2. Blister in the Sun - Violent Femmes\n     3. Feel It Still - Portugal. The Man\nChoice: "))
	if songChoice == 1:
		print("Now Playing: Use Somebody - Kings of Leon") 
	elif songChoice == 2:
		print("Now Playing: Blister in the Sun - Violent Femmes")
	elif songChoice == 3:
		print("Now Playing: Feel It Still - Portugal. The Man")
	else: 
		print("Invalid song choice. Try again later.")

#Pop
elif choice == 3:
	songChoice = int(input("\n\nPlease choose a song\n     1. Truth Hurts - Lizzo\n     2. 7 rings - Ariana Grande\n     3. Ain't It Fun - Paramore\nChoice: "))
	if songChoice == 1:
		print("Now Playing: Truth Hurts - Lizzo") 
	elif songChoice == 2:
		print("Now Playing: 7 rings - Ariana Grande")
	elif songChoice == 3:
		print("Now Playing: Ain't It Fun - Paramore")
	else: 
		print("Invalid song choice. Try again later.")
  
else:
	print("Invalid option. Try again later")
