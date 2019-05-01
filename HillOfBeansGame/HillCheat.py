import random

total = int(input("Enter total number of beans:\n"))

def hint():
	return total%(3+1)

def otherTurn():
	if total > 3:
		take = random.randint(1,3)
	else:
		take = total
	
	""" Removing the logic so the opponent takes a random amount
	take = total%(3+1)
	
	if take == 0:
		take += 1
	"""
	print ("Other player takes", str(take) +".")
	
	return take

print("There are ", total, "beans left.")

while True:
	print("Hint: You should take", hint(), "beans.")
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
				print("\nThe other player has won.");
				break
			else:
				print("There are ", total, "beans left.\n")