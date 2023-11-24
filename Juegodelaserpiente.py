import turtle
import time
import random

posponer=  0.1

#Configuracion de la ventana

ven= turtle.Screen()
ven.title("Serpiente")
ven.bgcolor("Black")
ven.setup(width=600, height= 600)
ven.tracer(0)

#Comida
Comida=turtle.Turtle()
Comida.speed(0)
Comida.shape("circle")
Comida.color("Red")
Comida.penup()
Comida.goto(0,100)


#Diseño de la cabeza de la serpiente
cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("White")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "Stop"

#Funciones 
def arriba():
    cabeza.direction="up"
def abajo():
    cabeza.direction="down"
def izquierda():
    cabeza.direction= "left"
def derecha():
    cabeza.direction= "right"
def mov():
    if cabeza.direction == "up":
        y=cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction == "down":
        y=cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "left":
        x=cabeza.xcor() 
        cabeza.setx(x-20)
    if cabeza.direction == "right":
        x=cabeza.xcor() 
        cabeza.setx(x+20)

#Teclado
ven.listen()    
ven.onkeypress(arriba, "Up")
ven.onkeypress(abajo, "Down")
ven.onkeypress(izquierda, "Left")
ven.onkeypress(derecha, "Right")

while True:
    ven.update()

    if cabeza.distance(Comida)<20:
       x= random.randint(-280,280)
       y= random.randint(-280,280)
       Comida.goto(x,y)
    mov()
    time.sleep(posponer)

turtle.mainloop()
