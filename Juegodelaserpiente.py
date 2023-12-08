import turtle
import time
import random

posponer = 0.1

# Configuración de la ventana

ven = turtle.Screen()
ven.title("Serpiente")
ven.bgcolor("Black")
ven.setup(width=600, height=600)
ven.tracer(0)

# Comida
Comida = turtle.Turtle()
Comida.speed(0)
Comida.shape("circle")
Comida.color("Red")
Comida.penup()
Comida.goto(0, 100)

# cuerpo de la serpiente
segmentos = []

# Diseño de la cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("White")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "Stop"

# Funciones
def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
ven.listen()
ven.onkeypress(arriba, "Up")
ven.onkeypress(abajo, "Down")
ven.onkeypress(izquierda, "Left")
ven.onkeypress(derecha, "Right")

while True:
    ven.update()
    # COLISIONES CON EL BORDE
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "Stop"

        # Esconder los segmentos
        for seg in segmentos:
            seg.hideturtle()
            seg.goto(1000, 1000)  # Mover fuera del alcance
        # Limpiar lista
        segmentos.clear()

    if cabeza.distance(Comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        Comida.goto(x, y)
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.penup()
        nuevo_segmento.color('grey')
        segmentos.append(nuevo_segmento)

    # Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    
    
    mov()
    time.sleep(posponer)

turtle.mainloop()
