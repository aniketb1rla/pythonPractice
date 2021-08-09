import turtle
a_turtle = turtle.Turtle()
i = 0
def square():
  
  a_turtle.forward(100)
  a_turtle.right(90)
  a_turtle.forward(100)
  a_turtle.right(90)
  a_turtle.forward(100)
  a_turtle.right(90)
  a_turtle.forward(100)
  a_turtle.left(90+45)
  a_turtle.forward(142)
  a_turtle.left(45+90)
  a_turtle.forward(100)
  
def pattern():

  a_turtle.right(90)
  a_turtle.forward(100)
  a_turtle.right(45)
  a_turtle.forward(100)
  a_turtle.right(45)
  a_turtle.forward(100)
  a_turtle.right(45)
  a_turtle.forward(100)

for i in range(10):
  square()
  pattern()
  square()
