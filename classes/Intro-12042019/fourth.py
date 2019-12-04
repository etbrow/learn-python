currentYear = 2019

myBirthYear = int(input("What year were you born? "))
while True:
    curAge = currentYear - myBirthYear
    #curAge = 15

    if curAge <= 13:
        print("You aren't allowed to be here!!")
        print("It's because you are", curAge)
    elif curAge > 13 and curAge < 18:
        print("You should ask you parent before you enter...")
    else:
        print("You may enter!")

print("This is the end of the program")