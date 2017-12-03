import math


def up(x, y):
    return x, y + 1


def down(x, y):
    return x, y - 1


def left(x, y):
    return x - 1, y


def right(x, y):
    return x + 1, y


def increase(N, cur_point, x, y):
    if cur_point == N * N:
        N += 1

    pos_in_curve = cur_point - N * N
    if N % 2 == 0:
        # even
        if pos_in_curve == 0:
            x, y = left(x, y)
            cur_point += 1
        elif pos_in_curve <= N:
            x, y = up(x, y)
            cur_point += 1
        else:
            x, y = right(x, y)
            cur_point += 1
        pass
    else:
        # odd
        if pos_in_curve == 0:
            x, y = right(x, y)
            cur_point += 1
        elif pos_in_curve <= N:
            x, y = down(x, y)
            cur_point += 1
        else:
            x, y = left(x, y)
            cur_point += 1

    return N, cur_point, x, y


def part1():
    endpoint = 312051
    # endpoint = 1024
    N = math.floor(math.sqrt(endpoint))
    cur_point = N * N

    if N % 2 == 1:
        # odd
        x = int((N - 1) / 2)
        y = int((N - 1) / 2)
    else:
        # even
        y = -int(N / 2)
        x = y + 1

    print('N: ' + str(N))
    print('x, y: ' + str(x) + ', ' + str(y))
    print('cur point: ' + str(cur_point))
    print('distance: ' + str(abs(x) + abs(y)))
    print('---------------------------------')
    for _ in range(cur_point, endpoint):
        Nn, cur_point, x, y = increase(N, cur_point, x, y)

    print('N: ' + str(N))
    print('x, y: ' + str(x) + ', ' + str(y))
    print('cur point: ' + str(cur_point))
    print('distance: ' + str(abs(x) + abs(y)))


def get_val(spiral, x, y):
    sum = 0

    for key, s in spiral.items():
        if x == (s['x'] + 1) and y == s['y']:
            sum += s['val']
        if x == s['x'] - 1 and y == s['y']:
            sum += s['val']
        if x == s['x'] and y == s['y'] + 1:
            sum += s['val']
        if x == s['x'] and y == s['y'] - 1:
            sum += s['val']
        if x == (s['x'] + 1) and y == s['y']+1:
            sum += s['val']
        if x == s['x'] + 1 and y == s['y'] - 1:
            sum += s['val']
        if x == s['x'] - 1 and y == s['y'] + 1:
            sum += s['val']
        if x == s['x'] - 1 and y == s['y'] - 1:
            sum += s['val']
    return sum


def create_spiral(spiral, N, cur_pos, x, y):
    if N % 2 == 1:
        x, y, = right(x, y)
        cur_pos += 1
        spiral[cur_pos] = {'x': x, 'y': y, 'val': get_val(spiral, x, y)}
        for _ in range(N):
            x, y, = down(x, y)
            cur_pos += 1
            spiral[cur_pos] = {'x': x, 'y': y, 'val': get_val(spiral, x, y)}
        for _ in range(N):
            x, y, = left(x, y)
            cur_pos += 1
            spiral[cur_pos] = {'x': x, 'y': y, 'val': get_val(spiral, x, y)}
    else:
        x, y, = left(x, y)
        cur_pos += 1
        spiral[cur_pos] = {'x': x, 'y': y, 'val': get_val(spiral, x, y)}
        for _ in range(N):
            x, y, = up(x, y)
            cur_pos += 1
            spiral[cur_pos] = {'x': x, 'y': y, 'val': get_val(spiral, x, y)}
        for _ in range(N):
            x, y, = right(x, y)
            cur_pos += 1
            spiral[cur_pos] = {'x': x, 'y': y, 'val': get_val(spiral, x, y)}
    return spiral, x, y, cur_pos


cur_point = 1
x = 0
y = 0
N = 1

spiral = dict()
spiral[cur_point] = {'x': x, 'y': y, 'val': 1}

for N in range(1, 10):
    spiral, x, y, cur_point = create_spiral(spiral, N, cur_point, x, y)

s = spiral[cur_point]
print('Last: Current pos: ' + str(cur_point) + ' x,y ' + str(s['x']) + ', ' + str(s['y']) + ' val: ' + str(s['val']))
# for cur_pos, d in spiral.items():
#     _x = d['x']
#     _y = d['y']
#     _val = d['val']
#     print('Current pos: ' + str(cur_pos) + ' x,y ' + str(_x) + ', ' + str(_y) + ' val: ' + str(_val))

for cur_pos, d in spiral.items():
    if d['val'] > 312051:
        print('First value written greater than 312051 is: ' + str(d['val']))
        break