with open('day10Input.txt', 'r') as f:
    data = f.readlines()


def part1():
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


def part2(txt):
    skip_size = 0
    current_position = 0
    l = []
    for i in range(0, 256):
        l.append(i)

    length_list = []
    for d in txt:
        length_list.append(ord(d))

    length_list.append(17)
    length_list.append(31)
    length_list.append(73)
    length_list.append(47)
    length_list.append(23)

    for _ in range(0, 64):
        for length in length_list:
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

    dense_hash = []
    for x in range(0,16):
        h = 0
        for y in range(0,16):
            h ^= l[x*16+y]

        dense_hash.append(h)
    print('Dense hash: ' + ''.join('{:02x}'.format(x) for x in dense_hash))

    # print('Final hashed list: ' + ' '.join(str(x) for x in l))
    print('Result: ' + str(l[0] * l[1]))

part2(data[0])