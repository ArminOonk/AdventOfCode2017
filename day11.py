import math

with open('day11Input.txt', 'r') as f:
    data = f.readlines()

diag_dx = math.cos(math.radians(30))
diag_dy = math.sin(math.radians(30))

# print('Diag: ' + str(diag_dx) + ", " + str(diag_dy))
for line in data:
    x = 0
    y = 0

    dist_max = 0
    for l in line.split(','):
        l = l.strip()
        if l == 'n':
            y += 1
        elif l == 's':
            y -= 1
        elif l == 'ne':
            x += diag_dx
            y += diag_dy
        elif l == 'se':
            x += diag_dx
            y -= diag_dy
        elif l == 'nw':
            x -= diag_dx
            y += diag_dy
        elif l == 'sw':
            x -= diag_dx
            y -= diag_dy
        else:
            print('Unknown directions: ' + l)

        steps_x = int(round(abs(x)/diag_dx))
        if steps_x*diag_dy > abs(y):
            steps_y = 0
        else:
            steps_y = abs(int(round(abs(y)-steps_x*diag_dy)))
        dist = steps_x+steps_y

        if dist > dist_max:
            dist_max = dist

    steps_x = int(round(abs(x)/diag_dx))
    if steps_x*diag_dy > abs(y):
        print('y travel larger as required because of x')
        steps_y = 0
    else:
        steps_y = abs(int(round(abs(y)-steps_x*diag_dy)))
    print("End coordinate: " + str(x) + ", " + str(y) + " Steps x: " + str(steps_x) + ", " + str(steps_y) + " total: " + str(steps_x+steps_y))
    print('Largest distance: ' + str(dist_max))

