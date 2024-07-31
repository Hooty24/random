from random import choice


def interpret(code):
    def move():
        nonlocal i, j
        i, j = i + direction[0], j + direction[1]

    code = [list(i) for i in code.split('\n')]
    i, j = 0, 0
    stack = []
    output = []
    direction = (0, 1)
    while True:
        el = code[i][j]
        match el:
            case el if el in '0123456789':
                stack.append(int(el))
            case '+':
                stack[-2:] = [stack[-2] + stack[-1]]
            case '-':
                stack[-2:] = [stack[-2] - stack[-1]]
            case '*':
                stack[-2:] = [stack[-2] * stack[-1]]
            case '/':
                if stack[-1] != 0:
                    stack[-2:] = [stack[-2] // stack[-1]]
                else:
                    stack[-2:] = [0]
            case '%':
                if stack[-1] != 0:
                    stack[-2:] = [stack[-2] % stack[-1]]
                else:
                    stack[-2:] = [0]
            case '!':
                stack[-1] = int(not stack[-1])
            case '`':
                stack[-2:] = [int(stack[-2] > stack[-1])]
            case '_':
                direction = (0, 1) if stack.pop() == 0 else (0, -1)
            case '|':
                direction = (1, 0) if stack.pop() == 0 else (-1, 0)
            case ':':
                if stack:
                    stack.append(stack[-1])
                else:
                    stack.append(0)
            case '\\':
                if len(stack) < 2:
                    stack.append(0)
                else:
                    stack[-1], stack[-2] = stack[-2], stack[-1]
            case '$':
                stack.pop()
            case '#':
                move()
            case '.':
                output.append(str(stack.pop()))
            case '"':
                move()
                while True:
                    el = code[i][j]
                    if el == '"':
                        break
                    stack.append(ord(el))
                    move()
            case ',':
                output.append(chr(stack.pop()))
            case ' ':
                pass
            case 'p':
                y, x, v = stack.pop(), stack.pop(), stack.pop()
                code[y][x] = chr(v)
            case 'g':
                y, x = stack.pop(), stack.pop()
                stack.append(ord(code[y][x]))
            case '@':
                break
            case '>':
                direction = (0, 1)
            case '<':
                direction = (0, -1)
            case '^':
                direction = (-1, 0)
            case 'v':
                direction = (1, 0)
            case '?':
                direction = choice(((0, 1), (0, -1), (-1, 0), (1, 0)))
        move()
    return ''.join(output)


code = '62*1+v>01p001>+v>\\:02p\\:02gv\n     0       ^             <\n     .         :p\n     "         .1\n        v 0," "<0\n     "  >1g12-+:|\n     ,          @\n     >^\n'
print(interpret(code))
