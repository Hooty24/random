import math


def init(x=156, y=56):
    global coordinates, direction, angle, tale, field
    coordinates = [x // 2 - 1, y // 2 - 1]
    direction = (0, 1)
    angle = 90
    tale = True
    field = [[" " for _ in range(x)] for _ in range(y)]


init()


def round(num, start=5):
    if int(str(num % 1)[2]) >= start:
        return int(num // 1) + 1
    return int(num // 1)


def update():
    for el in field:
        print(*el, sep='')


def goto(x, y):
    coordinates = [x, y]


def down():
    global tale
    tale = True


def up():
    global tale
    tale = False


def dot(r=0):
    if tale:
        for x in range(int(coordinates[0] - r), int(coordinates[0]) + r + 1):
            for y in range(int(coordinates[1]) - r, int(coordinates[1]) + r + 1):
                if (x - int(coordinates[0])) ** 2 + (y - int(coordinates[1])) ** 2 <= r ** 2:
                    field[y][x] = '.'


def forward(ln):
    for _ in range(ln + 1):
        global coordinates
        dot()
        coordinates = [coordinates[0] + direction[0], coordinates[1] - direction[1]]


fd = forward


def backward(ln):
    for _ in range(ln + 1):
        global coordinates
        dot()
        coordinates = [coordinates[0] - direction[0], coordinates[1] + direction[1]]


bk = backward


def left(degree):
    global angle, direction
    angle += degree
    radians = angle * math.pi / 180
    direction = (math.cos(radians), math.sin(radians))


lt = left


def right(degree):
    return lt(-degree)


rt = right
