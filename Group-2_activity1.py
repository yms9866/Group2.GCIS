import turtle

'''The following function draws hexagon with a given side_length and border_color and fills it with a given hex_color.'''
def hexagon(side_length,border_color,hex_color):
    turtle.color(border_color)
    turtle.fillcolor(hex_color)
    turtle.begin_fill()
    turtle.forward(side_length)
    turtle.left(60)
    turtle.forward(side_length)
    turtle.left(60)
    turtle.forward(side_length)
    turtle.left(60)
    turtle.forward(side_length)
    turtle.left(60)
    turtle.forward(side_length)
    turtle.left(60)
    turtle.forward(side_length)
    turtle.end_fill()

'''The following function draws a circle with a given radius and border_color and fills it with a given circle_color.'''
def circle(radius,border_color,circle_color):
    """radius = int, circle_color = str,  border_color = str"""
    turtle.color(border_color)
    turtle.fillcolor(circle_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

'''The following function draws hexagon with a given length and border_color and fills it with a given square_color.'''
def square(length,border_color,square_color):
    turtle.color(border_color)
    turtle.fillcolor(square_color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.end_fill()


'''The following function sets the turtle to the given heading (0 to 360) and to the given x and y coordinate value.'''
def setPos(heading,x,y):
    turtle.setheading(heading)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


def pattern(hex_color,circle_color,square_color,border_color):
    
    # The first row (hexagon, circle, square)
    setPos(0,-150,150) # the turtle is positioned at (-150,150) on the xy coordinate with heading 0 (to the east)
    hexagon(50,border_color,hex_color) # starting from (-150,150) it draws hexagon with side_length of 50 and the turtle ends at its starting point (-150,150)
    setPos(0,0,150) # this takes the turtle to (0,150)
    circle(50,border_color,circle_color)
    setPos(0,75,150)
    square(90,border_color,square_color)
    
    # The second row (hexagon, circle, square)
    setPos(0,-35,30)
    hexagon(50,border_color,hex_color)
    setPos(0,120,30)
    circle(50,border_color,circle_color)
    setPos(0,195,30)
    square(90,border_color,square_color)
    
    # The third row (hexagon, circle, square)
    setPos(0,100,-90)
    hexagon(50,border_color,hex_color)
    setPos(0,250,-90)
    circle(50,border_color,circle_color)
    setPos(0,325,-90)
    square(90,border_color,square_color)

def main(): 
    w = input('Enter the color what you want to fill the hexagon with. ')
    x = input('Enter the color what you want to fill the circle with. ')
    y = input('Enter the color what you want to fill the square with. ')
    z = input('Enter the color what you want for the border of the shapes. ')
    turtle.tracer(True)
    turtle.bgcolor('black')
    pattern(w,x,y,z)
    turtle.done()
main()


