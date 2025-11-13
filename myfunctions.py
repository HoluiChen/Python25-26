import turtle
bob=turtle.Turtle()

def sun(x,y):
  jump(x,y)
  bob.pensize(10)
  bob.color("yellow")
  for times in range(10):
    polygon(3,20)
    bob.forward(30)
    bob.right(36)
  jump(16 + x,-75 + y)
  bob.pensize(20)
  bob.circle(30)
def polygon(sides, distance ):
  angle = 360 / sides
  for times in range(sides):
    bob.forward(distance)
    bob.left(angle)

def star(color,distance):
    bob.width(5)
    angle=135
    for times in range(8):
      bob.forward(distance)
      bob.left(angle)
      
def comet(c, distance, angle):
  bob.color(c)
  for times in range(10):
    bob.pensize(times / 2)
    bob.forward(distance)
    bob.left(angle)

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()

def home():
  bob.penup()
  bob.home()
  bob.pendown()

def rainbow():
  bob.width(20)
  bob.color("red")
  bob.circle(60)
  bob.color("orange")
  bob.circle(50)
  bob.color("yellow")
  bob.circle(40)
  bob.color("green")
  bob.circle(30)
  bob.color("blue")
  bob.circle(20)
  bob.color("purple")
  bob.circle(10)

def plus(c,distance):
  bob.color(c)
  for times in range(4):
    bob.forward(distance)
    bob.left(90)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(90)

def spiral(distance,angle):
    for number in range(distance):
        bob.forward(number * 4)
        bob.left(angle)

def stair(distance, amount):
     for times in range( amount ):
         bob.forward( distance )
         bob.left( 90 )
         bob.forward( distance )
         bob.right( 90 )
def circle(radius,c):
  bob.pencolor(c)
  bob.circle(radius)
