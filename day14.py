def knot_hash(key):
    skip_size = 0
    current_position = 0
    l = []
    for i in range(0, 256):
        l.append(i)

    length_list = []
    for d in key:
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
    return dense_hash

grid = []
used_cnt = 0
for x in range(0, 128):
    row = knot_hash('ljoxqyyw-' + str(x))

    hash_str = ''.join(format(x, '08b') for x in row)
    # hash_str = hash_str.replace('1', '#').replace('0', '.')

    used_cnt += hash_str.count('1')
    grid.append(hash_str)

print('Number of squares used: ' + str(used_cnt))
for x in range(0, 8):
    print(grid[x][0:8])
