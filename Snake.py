from select import select
from sys import stdin
from random import randint


def show_field():
    print('\n' * 3)
    print(f'Score: {k}')
    for _ in arr:
        print(*_)


def gen_apple():
    global apple
    while True:
        apple = [randint(1, y - 1), randint(0, x - 1)]
        if apple != head and all(apple != l for l in tale):
            break
    arr[apple[0]][apple[1]] = '@'


def snake(direction):
    global head, tale, k
    if (head[0], head[1]) != (apple[0], apple[1]):
        arr[tale[0][0]][tale[0][1]] = '.'
    else:
        tale.insert(0, tale[0])
        k += 1
        gen_apple()
    for z in range(len(tale) - 1):
        tale[z] = tale[z + 1][:]
    tale[z + 1] = head[:]
    arr[tale[0][0]][tale[0][1]], arr[tale[1][0]][tale[1][1]] = '*', '*'
    match direction:
        case 'right':
            if head[1] == x - 1:
                head[1] = -1
            head[1] += 1
            arr[head[0]][head[1]] = '*'
        case 'left':
            if head[1] == 0:
                head[1] = x
            head[1] -= 1
            arr[head[0]][head[1]] = '*'
        case 'up':
            if head[0] == 0:
                head[0] = y
            head[0] -= 1
            arr[head[0]][head[1]] = '*'
        case 'down':
            if head[0] == y - 1:
                head[0] = -1
            head[0] += 1
            arr[head[0]][head[1]] = '*'


def start():
    global x, y, head, tale, arr, k, dr, br
    arr = [['.'] * 16 for _ in range(10)]
    head = [0, 3]
    tale = [[0, 0], [0, 1], [0, 2]]
    arr[tale[0][0]][tale[0][1]] = '*'
    arr[tale[1][0]][tale[1][1]] = '*'
    arr[tale[2][0]][tale[2][1]] = '*'
    arr[head[0]][head[1]] = '*'
    x = len(arr[0])
    y = len(arr)
    k = 0
    dr = 'd'
    br = dr
    gen_apple()
    show_field()


actions = {
    'w': 'up',
    'a': 'left',
    's': 'down',
    'd': 'right'
}

start()

while True:
    if all(head != m for m in tale):
        g, h, p = select([stdin], [], [], 0.15)
        if g:
            dr = stdin.readline().strip()
            if dr == '':
                dr = br
            br = dr
            snake(actions[dr])
            show_field()
        else:
            snake(actions[dr])
            show_field()

    else:
        print('You Lose')
        print('Your Score:', k)
        input('If you want to continue press Enter')
        start()
