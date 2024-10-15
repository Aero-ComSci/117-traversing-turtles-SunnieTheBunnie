#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.pencolor(new_color)
  my_turtles.append(t)

direction = 90

# starting point for all the drwaings
startx = 0
starty = 0
z = 5

# draws each picture
for t in my_turtles:
  t.setheading(direction)
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.right(100-z)     
  t.forward(50+z)
  z=z+5
  direction = t.heading()

#	sets coordinates for the next drawing
  startx = t.xcor()
  starty = t.ycor()

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.pencolor(new_color)
  my_turtles.append(t)

direction = 90

# starting point for all the drwaings
startx = 0
starty = 0
z = 5

# draws each picture
for t in my_turtles:
  t.setheading(direction)
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.right(100-z)     
  t.forward(50+z)
  z=z+5
  direction = t.heading()

#	sets coordinates for the next drawing
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
