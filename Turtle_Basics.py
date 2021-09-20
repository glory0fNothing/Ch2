import turtle
turtle.forward(100)
turtle.right(45)
turtle.forward(100)

turtle.setheading(0)
turtle.forward(50)
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(100)

turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(50)

turtle.reset() #does not reset background color
turtle.circle(100)

turtle.dot()
#turtle.pensize (width)
#.pencolor(color) - ('red')
turtle.bgcolor('red')
turtle.setup(560, 680)
#turtle.clear() - take drawings only out
#turtle.clearscreen() - everything reset

turtle.clearscreen()
turtle.goto(0, 100)
turtle.goto(-100, 0)
turtle.goto(0, 0)

#.pos() - shows position
#.xcor() - x coordinate
#.ycor - y coordinate

#turtle.speed(speed) - 1 through 10
#if 0, the turtle moves instantly (no animation)

#turtle.hideturtle() - graphics still drawn but no turtle seen
#.showturtle() - shows turtle again

#.write(text) - display text in window
turtle.write('Hello World')

turtle.clearscreen()
turtle.hideturtle()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
