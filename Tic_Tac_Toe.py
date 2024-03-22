"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?


    importan funciones y objetos específicos de turtle.
    los cuales se utilizan para dibujar gráficos en la pantalla.
    De freegames se importa linera dibujar líneas en la pantalla. """
from turtle import up, goto, down, circle, update
from turtle import setup, hideturtle, tracer, onscreenclick, done
from turtle import color, width
from freegames import line


""" Definimos un conjunto para almacenar las casillas ocupadas """
occupied_cells = set()


def grid():
    """ Se define una función llamada grid que dibuja el tablero
    tic-tac-toe dibujando cuatro líneas """
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """ Se define una función llamada drawx que dibuja un jugador X
    en las coordenadas especificadas (x, y)
    tilizamos color para modificar el color
    widtch para el tamaño"""
    color('blue')
    width(15)
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)
    occupied_cells.add((x, y))


def drawo(x, y):
    """ Se define una función llamada drawo que dibuja un jugador O
    en las coordenadas especificadas (x, y)
    utilizamos color para modificar el color
    widtch para el tamaño"""
    color('red')
    width(15)
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)
    occupied_cells.add((x, y))


def floor(value):
    """ Esta define una función llamada floor que redondea hacia abajo
    un valor dado al múltiplo de 133 más cercano."""
    return ((value + 200) // 133) * 133 - 200
    """ Se inicializa un diccionario state con una clave 'player' establecida
    en 0, y una lista players que contiene las funciones drawx y drawo."""


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Se define una función llamada tap que se manda llamar
    cuando se hace clic en la pantalla. Dibuja una X o una O en el cuadro
    que se hizo clic, dependiendo de cuyo turno sea."""
    x = floor(x)
    y = floor(y)
    if (x, y) in occupied_cells:
        print("¡Casilla ocupada! Intenta en otra casilla.")
        return
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


""" Establece las dimensiones de la ventana de dibujo. """
setup(420, 420, 370, 0)
"""se usa para dibujar las X y O, sin que el cursor sea visible."""
hideturtle()
"""Controla si las actualizaciones del lienzo se muestran en tiempo
   real o no."""
tracer(False)
"""Esta función se llama para dibujar el tablero."""
grid()
update()
""" Cuando el jugador hace clic en la ventana, se llama a la función tap(x, y)
    que se encarga de manejar el clic y realizar las acciones necesarias """
onscreenclick(tap)
""" mantiene la ventana de dibujo abierta hasta que se cierre manualmente."""
done()
