numberOfNotBeans = 15
thisTurn = 0

def aiTurn():
    take = numberOfNotBeans%(3+1)
    if take == 0:
        take += 1
    print ("Other player takes", str(take) +".")
    return take

while numberOfNotBeans > 0:
    print("It is Player" + str((thisTurn%2+1)) + "'s turn.")
    print("There are", numberOfNotBeans, "not beans left in the not pile...")
    if thisTurn%2+1 == 1:
        numberOfNotBeansToTake = int(input("How many not beans do you want to take? "))
        if numberOfNotBeansToTake > 3:
            print("You can't take more than 3 not beans!")
        elif numberOfNotBeansToTake < 1:
            print("You have to take at least one")
        else:
            numberOfNotBeans -= numberOfNotBeansToTake
            if numberOfNotBeans > 0:
                thisTurn += 1
    else:
        numberOfNotBeans -= aiTurn()
        if numberOfNotBeans > 0:
                thisTurn += 1


print("Player" + str((thisTurn%2+1)) + " wins the game!")