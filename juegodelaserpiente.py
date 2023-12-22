import turtle
import time
import random

posponer = 0.1
score = 0
highscore = 0
manzanas_comidas = 0
velocidad_doble = False

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

# Manzana Amarilla
manzana_amarilla = turtle.Turtle()
manzana_amarilla.speed(0)
manzana_amarilla.shape("square")
manzana_amarilla.color("yellow")
manzana_amarilla.penup()
manzana_amarilla.hideturtle()
manzana_amarilla.goto(0, 0)

segmentos = []

# Marcador de puntuación
text = turtle.Turtle()
text.speed(0)
text.color("White")
text.penup()
text.goto(0, 260)
text.hideturtle()
text.write("Score=0    High Score=0", align="center", font=("Courier", 24, "normal"))

# Diseño de la cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("White")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "Up"

# Función para crear un nuevo segmento de la serpiente
def crear_segmento():
    segmento = turtle.Turtle()
    segmento.speed(0)
    segmento.shape('square')
    segmento.penup()
    segmento.color('grey')
    return segmento

# Función para incrementar el contador de manzanas comidas
def incrementar_manzanas_comidas():
    global manzanas_comidas
    manzanas_comidas += 1
    mostrar_manzana_amarilla()

# Funciones de movimiento
def arriba():
    if cabeza.direction != "Down":
        cabeza.direction = "Up"

def abajo():
    if cabeza.direction != "Up":
        cabeza.direction = "Down"

def izquierda():
    if cabeza.direction != "Right":
        cabeza.direction = "Left"

def derecha():
    if cabeza.direction != "Left":
        cabeza.direction = "Right"

def mov():
    if cabeza.direction == "Up":
        cabeza.sety(cabeza.ycor() + 20)
    elif cabeza.direction == "Down":
        cabeza.sety(cabeza.ycor() - 20)
    elif cabeza.direction == "Left":
        cabeza.setx(cabeza.xcor() - 20)
    elif cabeza.direction == "Right":
        cabeza.setx(cabeza.xcor() + 20)

# Función para mostrar la manzana amarilla después de comer 5 manzanas
def mostrar_manzana_amarilla():
    global manzanas_comidas
    if manzanas_comidas % 5 == 0 and manzanas_comidas > 0:
        if not manzana_amarilla.isvisible():
            ven.ontimer(aparecer_manzana_amarilla, 0)

# Función para hacer que la manzana amarilla aparezca
def aparecer_manzana_amarilla():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    manzana_amarilla.goto(x, y)
    manzana_amarilla.showturtle()
    ven.ontimer(desaparecer_manzana_amarilla, 5000)

# Función para hacer que la manzana amarilla desaparezca
def desaparecer_manzana_amarilla():
    manzana_amarilla.hideturtle()

# Función para activar la velocidad doble
def activar_velocidad_doble():
    global posponer, velocidad_doble
    posponer /= 2
    velocidad_doble = True
    ven.ontimer(desactivar_velocidad_doble, 10000)  # 10000 milisegundos = 10 segundos

# Función para desactivar la velocidad doble
def desactivar_velocidad_doble():
    global posponer, velocidad_doble
    posponer *= 2
    velocidad_doble = False

# Configuración de teclado
ven.listen()
ven.onkeypress(arriba, "Up")
ven.onkeypress(abajo, "Down")
ven.onkeypress(izquierda, "Left")
ven.onkeypress(derecha, "Right")

# Bucle principal
while True:
    ven.update()

    # Resto del código...

    # Colisiones con la manzana amarilla
    if cabeza.distance(manzana_amarilla) < 20:
        if manzana_amarilla.isvisible():
            manzana_amarilla.hideturtle()
            if not velocidad_doble:  # Evita que la velocidad doble se active repetidamente
                activar_velocidad_doble()
            manzanas_comidas = 0

    # Resto del código...

    # Colisiones con los bordes
    if (
        cabeza.xcor() > 290
        or cabeza.xcor() < -290
        or cabeza.ycor() > 290
        or cabeza.ycor() < -290
    ):
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "Up"

        # Esconder los segmentos
        for seg in segmentos:
            seg.hideturtle()
            seg.goto(1000, 1000)
        # Limpiar lista
        segmentos.clear()

        # Resetear marcador
        score = 0
        text.clear()
        text.write(
            "Score: {}       High Score: {}".format(score, highscore),
            align="center",
            font=("Courier", 20, "normal"),
        )

    # Resto del código...

    # Colisiones con la comida
    if cabeza.distance(Comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        Comida.goto(x, y)

        nuevo_segmento = crear_segmento()
        segmentos.append(nuevo_segmento)

        # Aumento de puntaje y contador de manzanas comidas
        score += 10
        incrementar_manzanas_comidas()

        if score > highscore:
            highscore = score

        text.clear()
        text.write(
            "Score: {}       High Score: {}".format(score, highscore),
            align="center",
            font=("Courier", 20, "normal"),
        )

    # Resto del código...

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

    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "Up"

            # Eliminar los segmentos
            for segmento in segmentos:
                segmento.hideturtle()

            # Limpiar segmentos
            segmentos.clear()

            # Resetear marcador
            score = 0
            text.clear()
            text.write(
                "Score: {}       High Score: {}".format(score, highscore),
                align="center",
                font=("Courier", 20, "normal"),
            )

    time.sleep(posponer)

turtle.bye()
