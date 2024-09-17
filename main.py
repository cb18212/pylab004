import turtle
import math
"""PUT YOUR FUNCTIONS HERE"""

def draw_square(t, length):
	"""draws a square with the given side length"""
	draw_polygon(t, 4, length)

def draw_circle(t, radius):
	"""Draws a circle with the given radius"""
	t.circle(radius)

def draw_polygon(t, sides, length):
	"""Draws a regular polygon with a given number of sides and side length."""
	angle = 360/sides
	for _ in range(sides):
		t.forward(2*math.pi*length/sides)
		t.left(angle)

#create a turtle object
t = turtle.Turtle()

#hide the turtle and set speed
t.speed(10)
#t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
t.color("green")

#set the width and height of the screen
screen.setup(width=600, height=600)

#clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
for i in range(100):
	draw_polygon(t, i+3, 50)

# Close the turtle graphics window when clicked
turtle.exitonclick()