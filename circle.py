import turtle
loadWindow = turtle.Screen()
turtle.colormode(255)


turtle.speed(5)

for i in range(100):
    circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()
