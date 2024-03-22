"""Memory, puzzle game of number pairs.
"""

from random import shuffle
from turtle import up, goto, down, color, begin_fill, forward
from turtle import left, end_fill, clear, shape, stamp
from turtle import write, update, ontimer, setup, addshape
from turtle import hideturtle, tracer, onscreenclick, done

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2   # a
state = {'mark': None}
hide = [True] * 64
found = 0
finish = False


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        global found
        found += 1
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        if found == 32:   # a
            global finish
            finish = True


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):   # a
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    global finish

    if finish is False:
        update()
        ontimer(draw, 100)
    else:
        endGame()


def endGame():
    clear()
    goto(-110, 0)
    color('black')
    write("Game Over", font=('Arial', 30, 'normal'))
    update()
    ontimer(endGame, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
