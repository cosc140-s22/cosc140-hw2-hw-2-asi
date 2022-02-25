#######################################################
#Asianna Sample
# COSC 140 Homework 2, "face" problem
#
#######################################################
import turtle
dumbo = turtle.Turtle()
screen = dumbo.getscreen()
screen.title("Picture")
screen.setworldcoordinates(0, 0, 400, 400)
dumbo.speed('fastest')
dumbo.fillcolor("purple")
 
# function for creation of eye
def dcirc(col,rad):
    dumbo.down()
    dumbo.fillcolor(col)
    dumbo.begin_fill()
    dumbo.circle(rad)
    dumbo.end_fill()
    dumbo.up()
 
 
# draw face
dumbo.fillcolor('brown')
dumbo.begin_fill()
dumbo.circle(150)
dumbo.end_fill()
dumbo.up()
 
# draw eyes
dumbo.goto(-40, 120)
dcirc('white', 15)
dumbo.goto(-37, 125)
dcirc('black', 5)
dumbo.goto(40, 120)
dcirc('white', 15)
dumbo.goto(40, 125)
dcirc('black', 5)
 
# draw nose
dumbo.goto(0, 80)
dcirc('orange', 8)
 
# draw face
dumbo.goto(-40, 90)
dumbo.down()
dumbo.right(90)
dumbo.circle(40, 180)
dumbo.up()
# draw face
dumbo.down()
dumbo.right(90)
dumbo.circle(40, 180)
dumbo.up()

# draw face
dumbo.goto(-40, 170)
dumbo.down()
# dumbo.right(90)
dumbo.circle(40, 180)
dumbo.up()


#Eyebrows
dumbo.goto(-60,150)
dumbo.fillcolor('black')
dumbo.pendown()
dumbo.begin_fill()
dumbo.forward(40) 
dumbo.left(90)
dumbo.forward(10) 
dumbo.left(90) 
dumbo.forward(40) 
dumbo.left(90) 
dumbo.forward(10) 
dumbo.left(90)
dumbo.end_fill()
dumbo.penup()

#Other eyebrow
dumbo.goto(15,150)
dumbo.pendown()
dumbo.fillcolor('black')
dumbo.pendown()
dumbo.begin_fill()
dumbo.forward(40) 
dumbo.left(90)
dumbo.forward(10) 
dumbo.left(90) 
dumbo.forward(40) 
dumbo.left(90) 
dumbo.forward(10) 
dumbo.left(90)
dumbo.end_fill()
dumbo.penup()

#ears 
dumbo.goto(40,290)
dumbo.pendown()
dumbo.forward(100)
dumbo.left(120)
dumbo.forward(100)
dumbo.left(120)
dumbo.forward(100)
dumbo.penup()

#ear2
dumbo.goto(-70,380)
dumbo.pendown()
dumbo.forward(100)
dumbo.left(120)
dumbo.forward(100)
dumbo.left(120)
dumbo.forward(100)







# dumbo.goto(-40,89)

 

screen.exitonclick()



# def stararm():
#   s = 100
#   for i in range (70):
#     dumbo.forward(s)
#     dumbo.right(120)
#     s = s - 3
  


# def main():
#   dumbo.penup()
#   dumbo.goto(0,90)
#   dumbo.setposition(0,40)
#   dumbo.pendown()
#   stararm()
#   dumbo.setposition(0,90)
#   dumbo.left(180)
#   stararm()
  
#   # turtle.setworldcoordinates(30, 50)

#   screen.exitonclick()


# main()





