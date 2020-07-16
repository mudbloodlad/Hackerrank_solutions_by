import os
import turtle
import time 
import random

delay = 0.04

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Snake head 
head = turtle.Turtle()
head.speed(20)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(20)
food.shape("circle")
food.color("cyan")
food.penup()
food.goto(0,100)
food.direction = "stop"

segments = []


#defining movement functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

#keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#snake movement
def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+10)

    if head.direction =="down":
        y = head.ycor()
        head.sety(y-10)

    if head.direction =="left":
        x = head.xcor()
        head.setx(x-10)

    if head.direction =="right":
        x = head.xcor()
        head.setx(x+10)



#main game loop
while True:
    wn.update()

    # Check for a collision
    if head.distance(food) <20:
        # Move food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segment first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    time.sleep(delay)


wn.mainloop()