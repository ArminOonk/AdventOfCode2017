import string

with open('day16Input.txt', 'r') as f:
    data = f.readlines()

line = list(string.ascii_lowercase[0:16])
# line = list(string.ascii_lowercase[0:5])
# print('Line: ' + ''.join(line))

for _ in range(0, (1000000000) % 63):

    for m in data[0].split(','):
        if m[0] == 's':
            dist = len(line) - int(m[1:])
            # print("Spin: " + str(dist))
            line = line[dist:] + line[0:dist]
        elif m[0] == 'x':
            vals = m[1:].split('/')

            if len(vals) != 2:
                print('Unknown length: ' + m)
                break

            first = int(vals[0])
            second = int(vals[1])

            line[first], line[second] = line[second], line[first]
        elif m[0] == 'p':
            vals = m[1:].split('/')
            if len(vals) != 2:
                print('Unknown length: ' + m)
                break

            first = line.index(vals[0])
            second = line.index(vals[1])
            line[first], line[second] = line[second], line[first]
        else:
            print('Unknown stopping: ' + m)
            break

    if ''.join(line) == string.ascii_lowercase[0:16]:
        print("Loop repeat: " + str(_) + ' ' + str((_+1) % 63))

    if (_ % 100) == 0:
        print("Round: " + str(_))

print("Line: " + ''.join(line))
