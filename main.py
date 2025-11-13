from myfunctions import*
from random import randint

bob.speed(0)
turtle.bgcolor("black")
turtle.colormode(255)
turtle.tracer(0)
    
for times in range(256):
    num=randint(5,10)
    c = ( times, 0, 255 - times )
    bob.width(num)
    comet(c,times, 30)
    bob.right(30)

home()
for times in range(256):
    bob.width(10)
    c = ( 0, times, 255-times )
    plus(c,times/3)
    bob.right(45)   

home()
for times in range(50):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    c =(r,g,b)
    circle(50,c)
    bob.left(91)

home()
bob.pencolor("cyan")
bob.width(3)
spiral(50,121)

home()
bob.color("white")
for times in range(5):
    bob.left(times*10+72)
    spiral(50, 15)
    home()
