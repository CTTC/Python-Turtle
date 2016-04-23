import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(90)
        some_turtle.right(90)

        
def draw_arrow(some_turtle):
    for i in range(1,5):
        some_turtle.forward(50)
        if i % 2 == 0:
            some_turtle.right(120)
        else:
            some_turtle.right(60)
        
def draw_leaf(turtle):
    base = turtle.pos()
    turtle.circle(100,75)
    turtle.goto(base)
    turtle.circle(-100,75)
    turtle.goto(base)

def tree(some_turtle, length, angle, scale):
    if length < 10:
        return
    some_turtle.forward(length)
    some_turtle.right(angle)
    tree(some_turtle, length * scale, angle, scale)
    some_turtle.left(angle)
    tree(some_turtle, length * scale, angle, scale)
    some_turtle.left(angle)
    tree(some_turtle, length * scale, angle, scale)
    some_turtle.right(angle + 180)  # turn around
    some_turtle.forward(length) # go back to the original position
    some_turtle.right(180)       # turn back to the original orientation
    
def draw_art():
    window = turtle.Screen()
    window.bgcolor("#E5FFF3")

    '''
    angie = turtle.Turtle()
    angie.color("blue")
    angie.speed(12)
    for i in range(1,37):
        draw_arrow(angie)
        angie.right(10)
    '''
    '''
    hatt = turtle.Turtle()
    hatt.color("#FF4D4D")
    hatt.speed("fastest")
    hatt.width(2)
    hatt.left(90)
    tree(hatt,80, 30, 0.7)
    '''
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.width(2)
    brad.color("blue","green")
    brad.speed("fastest")
    brad.begin_fill()
    
    for i in range(72):
        draw_square(brad)
        brad.right(5)
    brad.end_fill()
    brad.ht()
    
    angie = turtle.Turtle()
    angie.color("orange")
    angie.width(4)
    angie.speed("fastest")
    angie.right(90)
    angie.forward(300)
    angie.left(62)
    for i in range(9):
        draw_leaf(angie)
        angie.left(20)

    angie.ht()
    window.exitonclick()


draw_art()
