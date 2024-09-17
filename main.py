import turtle
import math
"""PUT YOUR FUNCTIONS HERE"""

def draw_square(t, length):
	"""draws a square with the given side length"""
	draw_polygon(t, 4, length)

def draw_rectangle(t, h, w):
	for i in range(4):
		if i % 2 == 0:
			t.forward(w)
		else:
			t.forward(h)
		t.left(90)


def draw_circle(t, radius):
	"""Draws a circle with the given radius"""
	t.circle(radius)

def draw_polygon(t, sides, length):
	"""Draws a regular polygon with a given number of sides and side length."""
	angle = 360/sides
	for _ in range(sides):
		t.forward(2*math.pi*length/sides)
		t.left(angle)

def draw_pumpkin(t, x, y, radius):
	"""Draws a pumpkin (orange circle) at the given (x,y) location"""
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.fillcolor("orange")
	t.begin_fill()
	t.circle(radius)
	t.end_fill()

	#draws the stem
	stem_width = radius//2
	t.penup()
	t.goto(x-(stem_width/4),y+(2*radius))
	t.pendown()
	t.fillcolor("green")
	t.begin_fill()
	draw_rectangle(t, radius // 2, radius // 5)
	t.end_fill()

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
draw_pumpkin(t,0,0, 100)
#for i in range(100):
#	draw_polygon(t, i+3, 50)

# Close the turtle graphics window when clicked
turtle.exitonclick()