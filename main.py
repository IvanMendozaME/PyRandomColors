import turtle as t
import random

amount_colors = 30
colors_array = []
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
colors = [(87, 248, 169), (57, 11, 49), (178, 5, 110), (56, 38, 12), (215, 242, 83), (14, 24, 63), (192, 250, 223),
            (45, 6, 191), (6, 209, 96), (12, 49, 28), (240, 240, 184), (160, 164, 8), (222, 59, 189), (239, 114, 206), (112, 156, 243), (9, 101, 188), (129, 106, 13), (13, 138, 67), (254, 226, 252), (242, 153, 74), (17, 95, 49), (239, 169, 222), (183, 6, 4), (97, 87, 241), (183, 169, 242), (77, 95, 13), (233, 9, 209), (194, 222, 246), (195, 232, 3), (54, 40, 250)] 
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
def drawing_dots(colors):    
    for j in range(1,101):

             tim.dot(20, random.choice(colors))
             tim.forward(50)
            
             if j % 10 == 0:
                tim.setheading(90)
                tim.forward(50)
                tim.setheading(180)
                tim.forward(500)
                tim.setheading(0)
    tim.hideturtle()

drawing_dots(colors)

screen = t.Screen()
screen.exitonclick()