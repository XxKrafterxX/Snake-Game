# Libraries
import turtle
import time
import random
import winsound

# Screen setup
wn = turtle.Screen()
wn.title("Snake Game by Donnaven Wolff, June 2020")
wn.bgcolor("#d0d8d9")
wn.setup(width=600,height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Score
score = 0
highScore = 0

segments = []

# Movement
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x + -20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Controls and changing direction
def moveUp():
    head.direction = "up"
def moveDown():
    head.direction = "down"
def moveLeft():
    head.direction = "left"
def moveRight():
    head.direction = "right"

# Keyboard inputs
wn.listen()  # make sure to check for keypresses
if head.direction != "down":
    wn.onkeypress(moveUp, "Up")
if head.direction != "up":
    wn.onkeypress(moveDown, "Down")
if head.direction != "right":
    wn.onkeypress(moveLeft, "Left")
if head.direction != "left":
    wn.onkeypress(moveRight, "Right")

# Main game loop
while True:
    wn.update()

    # Border collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        winsound.PlaySound("loseGame.wav", winsound.SND_ASYNC)
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear segments list
        segments.clear()

    # Food collision
    if head.distance(food) < 20:
        # Move food to random location
        ranX = random.randint(-290, 290)
        ranY = random.randint(-290, 290)
        food.goto(ranX, ranY)

        # Add segment to snake
        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("square")
        newSegment.color("#168721")
        newSegment.penup()
        segments.append(newSegment)

        winsound.PlaySound("pointScored.wav", winsound.SND_ASYNC)

        # Increase score
        score += 1000


        if score > highScore:
            highScore = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

    # Make segments follow head
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to head
    if len(segments) > 0:
        headX = head.xcor()
        headY = head.ycor()
        segments[0].goto(headX, headY)

    move()
    # Head and body collision
    for segment in segments:
        if segment.distance(head) < 20:
            winsound.PlaySound("loseGame.wav", winsound.SND_ASYNC)
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear segments list
            segments.clear()


    time.sleep(.1)

# (IGNORE) Mainloop
wn.mainloop()
