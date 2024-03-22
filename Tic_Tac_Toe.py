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


def drawx(x, y, size=50):
    """ Se define una función llamada drawx que dibuja un jugador X
    en las coordenadas especificadas (x, y)
    tilizamos color para modificar el color
    widtch para establecer el ancho
    Se centra la figura"""
    color('red')
    width(15)
    up()
    goto(x - size / 2, y - size / 2)
    down()
    goto(x + size / 2, y + size / 2)
    up()
    goto(x + size / 2, y - size / 2)
    down()
    goto(x - size / 2, y + size / 2)
    occupied_cells.add((x, y))


def drawo(x, y, size=50):
    """ Se define una función llamada drawo que dibuja un jugador O
    en las coordenadas especificadas (x, y)
    utilizamos color para modificar el color
    widtch para establecer el ancho
    Se centra la figura """
    color('blue')
    width(15)
    up()
    goto(x, y - size / 2)
    down()
    circle(size / 2)
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
    cuando se hace clic en la pantalla.que se hizo clic, dependiendo
    de cuyo turno sea.
    Establece el tamaño del jugador X o O
    Verifica si la casilla está ocupada
    Dibuja una X o una O en el cuadro"""
    size = 50
    x = round(x / 133) * 133
    y = round(y / 133) * 133
    if (x, y) in occupied_cells:
        print("¡Casilla ocupada! Intenta en otra casilla.")
        return
    draw = drawx if state['player'] == 0 else drawo
    draw(x, y, size)
    update()
    state['player'] = 1 - state['player']


state = {'player': 0}


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
