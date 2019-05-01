from tkinter import *
from tkinter import messagebox
import random

counter = 0
numberOfBeans = 15

def showMessageBox(gameMessage):
    messagebox.showinfo(title="Game Event",
                        message=gameMessage)

def otherTurn():
        global numberOfBeans
        if random.randint(1, 147)%3 == 0:
                take = numberOfBeans%(3+1)
        else:
                take = random.randint(1, 3)
		
        if take == 0:
                take += 1
	
        showMessageBox("Other player takes" + str(take) + ".")
	
        return take

def subtractBeans():
    global numberOfBeans
    numToTake = int(takeNumberValue.get())
    if (numToTake > numberOfBeans) or (numToTake > 3):
        showMessageBox("You can't take that many.\n")
    elif numToTake <= 0:
                showMessageBox ("You must take at least one bean.\n")
    else:
        numberOfBeans -= numToTake
        if numberOfBeans == 0:
                showMessageBox("\nYou have won!")
        else:
                        showMessageBox("There are " + str(numberOfBeans) + " beans left.")
                        numberOfBeans -= otherTurn()
                        if numberOfBeans == 0:
                                showMessageBox("\nThe other player has won.");
                        else:
                                showMessageBox("There are " + str(numberOfBeans) + "beans left.\n")

#This populates the board with our beans
def drawBoard(canvas):
    global numberOfBeans
    canvas.delete("all")
    startingX=0
    padding=10
    squareSize=30

    curBean=1
    row=1
    print("Max Square Size: " + str(int(((500-startingX)/(squareSize+padding)))))
    print("Max Beans: " + str(numberOfBeans))

    while curBean <= numberOfBeans:
        col=1
        while col < int(((300-startingX)/(squareSize+(padding*2)))):
            if curBean <= numberOfBeans:
                print("Current Bean/Row/Col: " + str(curBean) + "/" + str(row) + "/" + str(col))
                print("Coordinates are " +
                      str((col*padding) + ((col-1)*squareSize)) + ", " +
                      str((row * padding) + ((row-1)*squareSize)) + ", " +
                      str((col * padding) + (squareSize*(curBean))) + ", " +
                      str(((startingX * curBean + padding) * row) + squareSize + padding))
                canvas.create_oval((col*padding) + ((col-1)*squareSize),
                                        (row * padding) + ((row-1)*squareSize),
                                        (col * padding) + (squareSize*(col)),
                                        (row * padding) + ((row)*squareSize), fill="red")
                curBean+=1
                print("Current Bean: " + str(curBean))
                col+=1
            else:
                print("Go to next row")
                break
        row+=1

    print("Done, should be drawn...")

root = Tk(screenName="Hill of Beans")

countLabel = Label(root, text="Ethan")
countLabel.grid(row=0, column=0, columnspan=3)

numberOfBeansLabel = Label(root, text="Number of Beans: ")
numberOfBeansLabel.grid(row=1, column=0)

numberOfBeansValueLabel = Label(root, text=numberOfBeans)
numberOfBeansValueLabel.grid(row=1, column=1, sticky=W)

drawArea = Canvas(root, width=500, height=500)
drawArea.grid(row=4, column=0, columnspan=3)

drawArea.create_line(10, 10, 50, 50)
drawArea.create_rectangle(80, 80, 120, 120)
drawArea.create_oval(80, 80, 120, 120)
drawArea.create_polygon(200, 100, 400, 100, 300, 300, fill='blue')

takeNumberLabel = Label(root, text="How Many Beans to Take: ")
takeNumberLabel.grid(row=2, column=0)

takeNumberValue = Entry(root)
takeNumberValue.grid(row=2, column=1)

takeButton = Button(root, text="Take Beans or Something",
                    command=lambda:[subtractBeans(), drawBoard(drawArea)])
takeButton.grid(row=2, column = 2)

#closeButton = Button(root, text="Close This Thang", command=root.destroy)
#closeButton.grid(row=3, column=0, columnspan=3)

drawArea = Canvas(root, width=500, height=500)
drawArea.grid(row=4, column=0, columnspan=3)

drawArea.create_line(10, 10, 50, 50)
drawArea.create_rectangle(80, 80, 120, 120)
drawArea.create_oval(80, 80, 120, 120)
drawArea.create_polygon(200, 100, 400, 100, 300, 300, fill='blue')

drawBoard(drawArea)

root.mainloop()
