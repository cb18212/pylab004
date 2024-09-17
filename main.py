import turtle

"""PUT YOUR FUNCTIONS HERE"""

def draw_square(t, length):
	"""draws a square with the given side length"""
	for _ in range(4):
		t.foreward()
		t.left()

def draw_circle(t, radius):
	"""Draws a circle with the given radius"""
	t.circle(radius)

def draw_polygon(t, sides, length):
	"""Draws a regular polygon with a given number of sides and side length."""
	angle = 360/sides
	for _ in range(sides):
		t.forward(length)
		t.left(angle)

#create a turtle object
t = turtle.Turtle()

#hide the turtle and set speed
t.speed(10)
#t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")

#set the width and height of the screen
screen.setup(width=600, height=600)

#clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
draw_polygon(t, 5, 100)

# Close the turtle graphics window when clicked
turtle.exitonclick()