with open('day19Input.txt', 'r') as f:
    data = f.readlines()

vert = '|'
hor = '-'
cross = '+'

grid = []
for d in data:
    grid.append(list(d.rstrip()))


def get_val(coord):
    row, col = coord

    if row >= len(grid):
        return ' '
    if col >= len(grid[row]):
        return ' '

    return grid[row][col]


for i in range(0, len(grid[0])):
    print(str(i) + ' ' + grid[0][i])
    if grid[0][i] != ' ':
        current_point = (0, i)
        current_dir = 'down'
        print('Start point: 0,' + str(i))

txt = ''
cnt = 0

while True:
    # print('Current point: ' + str(current_point) + ' direction: ' + current_dir)
    val = get_val(current_point)
    if val == ' ':
        print('We are on an empty spot')
        break

    if val != vert and val != hor and val != cross:
        txt += val

    if current_dir == 'right':
        if val == cross:
            if get_val((current_point[0] + 1, current_point[1] + 0)) != ' ':
                next_point = (current_point[0] + 1, current_point[1] + 0)
                current_dir = 'down'
            elif get_val((current_point[0] - 1, current_point[1] + 0)) != ' ':
                next_point = (current_point[0] - 1, current_point[1] + 0)
                current_dir = 'up'
        else:
            if get_val((current_point[0] + 0, current_point[1] + 1)) != ' ':
                next_point = (current_point[0] + 0, current_point[1] + 1)

    elif current_dir == 'left':
        if val == cross:
            if get_val((current_point[0] + 1, current_point[1] + 0)) != ' ':
                next_point = (current_point[0] + 1, current_point[1] + 0)
                current_dir = 'down'
            elif get_val((current_point[0] - 1, current_point[1] + 0)) != ' ':
                next_point = (current_point[0] - 1, current_point[1] + 0)
                current_dir = 'up'
        else:
            if get_val((current_point[0] + 0, current_point[1] - 1)) != ' ':
                next_point = (current_point[0] + 0, current_point[1] - 1)

    elif current_dir == 'up':
        if val == cross:
            if get_val((current_point[0] + 0, current_point[1] + 1)) != ' ':
                next_point = (current_point[0] + 0, current_point[1] + 1)
                current_dir = 'right'
            elif get_val((current_point[0] + 0, current_point[1] - 1)) != ' ':
                next_point = (current_point[0] + 0, current_point[1] - 1)
                current_dir = 'left'
        else:
            if get_val((current_point[0] - 1, current_point[1] + 0)) != ' ':
                next_point = (current_point[0] - 1, current_point[1] + 0)

    elif current_dir == 'down':
        if val == cross:
            if get_val((current_point[0] + 0, current_point[1] + 1)) != ' ':
                next_point = (current_point[0] + 0, current_point[1] + 1)
                current_dir = 'right'
            elif get_val((current_point[0] + 0, current_point[1] - 1)) != ' ':
                next_point = (current_point[0] + 0, current_point[1] - 1)
                current_dir = 'left'
        else:
            if get_val((current_point[0] + 1, current_point[1] + 0)) != ' ':
                next_point = (current_point[0] + 1, current_point[1] + 0)

    if next_point == current_point:
        print('No change')
        break

    current_point = next_point
    cnt += 1

print('Letter found: ' + txt + ' steps: ' + str(cnt+1))