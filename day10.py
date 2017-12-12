with open('day10Input.txt', 'r') as f:
    data = f.readlines()

skip_size = 0
current_position = 0
l = []
for i in range(0, 256):
    l.append(i)

for d in data[0].split(','):
    length = int(d)
    selection = []

    index = current_position
    for i in range(0, length):
        selection.append(l[index])
        index = (index + 1) % len(l)

    index = current_position
    for j in selection[::-1]:
        l[index] = j
        index = (index + 1) % len(l)

    current_position = (current_position + length + skip_size) % len(l)
    skip_size += 1


# print('Final hashed list: ' + ' '.join(str(x) for x in l))
print('Result: ' + str(l[0] * l[1]))