import math

def up(x, y):
    return x, y+1


def down(x, y):
    return x, y-1


def left(x, y):
    return x-1, y


def right(x, y):
    return x+1, y


def increase(N, cur_point, x, y):
    pos_in_curve = cur_point - N*N
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

    return x, y, cur_point


endpoint = 312051
# endpoint = 1024
N = math.floor(math.sqrt(endpoint))
cur_point = N*N

if N%2 == 1:
    # odd
    x = int((N-1)/2)
    y = int((N-1)/2)
else:
    # even
    y = -int(N/2)
    x = y+1

print('N: ' + str(N))
print('x, y: ' + str(x) + ', ' + str(y))
print('cur point: ' + str(cur_point))
print('distance: ' + str(abs(x)+abs(y)))
print('---------------------------------')
for _ in range(cur_point, endpoint):
    x, y, cur_point = increase(N, cur_point, x, y)

print('N: ' + str(N))
print('x, y: ' + str(x) + ', ' + str(y))
print('cur point: ' + str(cur_point))
print('distance: ' + str(abs(x)+abs(y)))
