with open('day22Input.txt', 'r') as f:
    data = f.readlines()


def coord_str(c):
    return str(c[0]) + "," + str(c[1])


def coord(txt):
    return list(map(int, txt.split(',')))


def move(d, pos):
    if d == 'n':
        pos[1] += 1
    elif d == 'e':
        pos[0] += 1
    elif d == 's':
        pos[1] -= 1
    else:
        pos[0] -= 1
    return pos


dir_list = ['n', 'e', 's', 'w']


def rot_left(d):
    return dir_list[dir_list.index(d) - 1]


def rot_right(d):
    return dir_list[(dir_list.index(d) + 1) % len(dir_list)]


cur_pos = [0, 0]


def show(x0=-5, y0=-5, width=10, height=10):
    txt = ''

    for y in range(y0+height, y0, -1):
        for x in range(x0, x0 + width):
            if coord_str([x, y]) in grid:
                if cur_pos[0] == x and cur_pos[1] == y:
                    txt += '[#]'
                else:
                    txt += ' # '
            else:
                if cur_pos[0] == x and cur_pos[1] == y:
                    txt += '[.]'
                else:
                    txt += ' . '
        txt += '\n'
    print(txt)


grid = dict()
size = len(data)
infect_cnt = 0
cur_dir = 'n'

print('Size: ' + str(size))
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "#":
            grid[coord_str([x-int(size/2), int(size/2) - y])] = True

for k, v in grid.items():
    print(k)

for _ in range(10000):
    if coord_str(cur_pos) in grid:
        print(str(_) + ' infected current dir: ' + cur_dir)
        cur_dir = rot_right(cur_dir)  # infected
        print('current dir: ' + cur_dir)
        del grid[coord_str(cur_pos)]  # cleaned
    else:
        print(str(_) + ' clean current dir: ' + cur_dir)
        cur_dir = rot_left(cur_dir)  # clean
        grid[coord_str(cur_pos)] = True  # Infect
        infect_cnt += 1
    move(cur_dir, cur_pos)

print('Grid: ')
show()
print('Number of infected: ' + str(infect_cnt))
