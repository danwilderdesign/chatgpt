''' 
Basic Python game using PythonTurtle

The initial setup for this code was built using ChatGPT. The 
    - The prompt: generate basic python game with movable character
'''

import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Python Game")
wn.bgcolor("black")

# Create the turtle
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()

# Create the coin
coin = turtle.Turtle()
coin.color("gold")
coin.shape("circle")
coin.penup()
coin.goto(200, 100)

# Define the movement functions
def move_left():
    player.setheading(180)
    x = player.xcor()
    x -= 20
    player.setx(x)

def move_right():
    player.setheading(0)
    x = player.xcor()
    x += 20
    player.setx(x)

def move_up():
    player.setheading(90)
    y = player.ycor()
    y += 20
    player.sety(y)

def move_down():
    player.setheading(270)
    y = player.ycor()
    y -= 20
    player.sety(y)

# Define the collision detection function
def check_collision():
    x_dist = player.xcor() - coin.xcor()
    y_dist = player.ycor() - coin.ycor()
    dist = ((x_dist ** 2) + (y_dist ** 2)) ** 0.5

    if dist < 20:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        coin.goto(x, y)

# Bind the movement functions to the arrow keys
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")

# Create the background objects
for i in range(50):
    bg_obj = turtle.Turtle()
    bg_obj.speed(0)
    bg_obj.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    bg_obj.goto(x, y)
    shapes = ["circle", "square", "triangle", "turtle"]
    shape = random.choice(shapes)
    bg_obj.shape(shape)
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    color = random.choice(colors)
    bg_obj.color(color)
    size = random.randint(10, 100)
    bg_obj.shapesize(size / 10)

# Start the game loop
while True:
    check_collision()
    wn.update()
