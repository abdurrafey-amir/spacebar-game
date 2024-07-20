import time
import turtle


turtle.hideturtle()
turtle.up()
turtle.goto(-250, 0)
turtle.bgcolor('#142F44')
turtle.color('#F6683B')

start = 0
spacePress = 0
turtle.write("Press Left for space game 1, Right for space game 2", font=("Arial", 15, "bold"))

game1Playing = False
game1end = False
game2Playing = False
game2end = False
timerActive = False


def left():
    global game1Playing, start
    game1Playing = True
    start = time.time()
    turtle.clear()
    turtle.goto(-150, 0)
    turtle.write("Click space as much as possible", font=("Arial", 15, "bold"))

def right():
    global game2Playing
    game2Playing = True
    turtle.clear()
    turtle.goto(-150, 0)
    turtle.write("Click space as much as possible", font=("Arial", 15, "bold"))

def TimerActivate():
    global game2end
    timeVal = 5

    for i in range(timeVal):
        turtle.clear()
        turtle.goto(-105, 0)
        turtle.write("Seconds Remaining: " + str(timeVal - i), font=("Arial", 15, "bold"))
        time.sleep(1)
    game2end = True

def space():
    global game1Playing, spacePress, timerActive, game2Playing
    spacePressAmt = 100
    if game1Playing:
        spacePress += 1
        turtle.clear()
        end = time.time()
        turtle.goto(-75, 0)
        turtle.write(str(spacePress) + "/" + str(spacePressAmt) + " Presses!", font=("Arial", 15, "bold"))
        if spacePress >= spacePressAmt:
            end = time.time()
            turtle.clear()
            turtle.goto(-100, 0)
            turtle.write("Time is " + str(round(end-start, 2)) + " seconds!", font=("Arial", 15, "bold"))
            game1Playing = False
    elif game2Playing:
        spacePress += 1
        if timerActive == False:
            timerActive = True
            TimerActivate()
        if game2end:
            turtle.clear()
            turtle.goto(-50, 0)
            turtle.write(str(spacePress) + " Presses!", font=("Arial", 15, "bold"))
            game2Playing = False

turtle.onkey(space, "space")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.listen()
turtle.mainloop()