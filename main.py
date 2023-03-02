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
  my_turtles.append(t)

#This states the starting location for the turtle
startx = 0
starty = 0
direction = 90
#This makes it so every turtle starts at  startx and starty and it also states the starting distance for the turtle to move and turn
for t in my_turtles:
  t.setheading(direction)
  t.penup()
  t.goto(startx, starty)
  new_color = turtle_colors.pop()
  t.pendown()
  t.fillcolor(new_color)
  t.pencolor(new_color)
  t.right(45)     
  t.forward(50)
  direction = t.heading()
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()