total = int(input("Enter total number of beans:\n"))

def otherTurn():
	take = total%(3+1)
	
	if take == 0:
		take += 1
	
	print ("Other player takes", str(take) +".")
	
	return take

print("There are ", total, "beans left.")

while True:
	numToTake = int(input("How many do you want to take?\n"))
	
	if (numToTake > total) or (numToTake > 3):
		print("You can't take that many.\n")
	elif numToTake <= 0:
		print ("You must take at least one bean.\n")
	else:
		total -= numToTake
		if total == 0:
			print("\nYou have won!")
			break
		else:
			print("There are ", total, " beans left.")
			total -= otherTurn()
			if total == 0:
				print("\nThe other player has won.")
				break
			else:
				print("There are ", total, "beans left.\n")