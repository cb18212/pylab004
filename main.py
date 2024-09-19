import turtle
import math
import random

"""PUT YOUR FUNCTIONS HERE"""

def moveto(t, x,y):
	t.penup()
	t.goto(x, y)
	t.pendown()

def draw_square(t, length):
	"""draws a square with the given side length"""
	draw_polygon(t, 4, length)

def draw_rectangle(t, h, w):
	for length in [w,h,w,h]:
		t.forward(length)
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
	t.goto(x,y-radius/2)
	t.pendown()
	t.fillcolor("orange")
	t.begin_fill()
	t.circle(radius)
	t.end_fill()

	#draws the stem
	stem_width = radius//2
	t.penup()
	t.goto(x-(stem_width/4),(y+1.5*radius))
	t.pendown()
	t.fillcolor("green")
	t.begin_fill()
	draw_rectangle(t, radius // 2, radius // 5)
	t.end_fill()

def lantern(t, x,y, size):
	draw_pumpkin(t, x, y, 100)
	draw_eye(t, x-55, y+50, 30)
	draw_eye(t, x+35, y+50, 30)
	draw_mouth(t, x, y, 100)
	t.setheading(0)
	
def draw_eye(t,x,y,size):
	"""draws one triangular eye at x,y"""
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.fillcolor("yellow")
	t.begin_fill()
	draw_polygon(t,3,size)
	t.end_fill()

def draw_mouth(t, x, y, width):
	"""draws a jagged mouth using a series of connected lines"""
	t.penup()
	t.goto(x-width/2,y)
	t.pendown()
	t.fillcolor("yellow")
	t.begin_fill()
	t.left(60)
	for _ in range(5):
		for i in (-120, 120):
			t.forward(width/(5))
			t.left(i)
	t.end_fill()

def draw_star(t,x,y,size):
	"""draws a star at the given (x,y position)"""
	moveto(t, x, y)
	t.fillcolor("white")
	t.begin_fill()
	draw_polygon(t, 5, size)
	t.end_fill()

def draw_sky(t, num_stars):
	"""Draws a starry sky with the given number of stars"""
	for _ in range(num_stars):
		x = random.randint(-300, 300)
		y = random.randint(-300,300)
		size = random.randint(3,10)
		draw_star(t,x,y,size)

#create a turtle object
t = turtle.Turtle()

#hide the turtle and set speed
t.speed(5000)
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
t.speed(0)
draw_sky(t,10)
t.speed(10)

#draw_pumpkin(t,0,0, 100)
#lantern(t,-150,150, 5)
#draw_eye(t, -40-15, 50, 30)
#draw_eye(t, 40-15, 50, 30)
#draw_mouth(t, 0, 0, 100)

# Draw three jack-o-lanterns
lantern(t, -150, -150, 100)

lantern(t, 0, -150, 80)

lantern(t, 150, -150, 100)


# Close the turtle graphics window when clicked
turtle.exitonclick()