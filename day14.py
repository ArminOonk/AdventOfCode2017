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
    for x in range(0, 16):
        h = 0
        for y in range(0, 16):
            h ^= l[x * 16 + y]

        dense_hash.append(h)
    return dense_hash


def find_first_empty(g):
    found_nonempty = True
    x = -1
    y = -1
    while found_nonempty:
        found_nonempty = False

        for _x in range(0, 128):
            for _y in range(0, 128):
                if g[_x][_y] == '1':
                    # print("Found not empty at: " + str(_x) + ', ' + str(_y))
                    x = _x
                    y = _y
                    found_nonempty = True
                    break
            if found_nonempty:
                break
        if found_nonempty:
            break
    return x, y


grid = []
used_cnt = 0
for _x in range(0, 128):
    # row = knot_hash('flqrgnkx-' + str(_x))  # Example
    row = knot_hash('ljoxqyyw-' + str(_x))  # Input

    hash_str = list(''.join(format(x, '08b') for x in row))
    # hash_str = hash_str.replace('1', '#').replace('0', '.')

    used_cnt += hash_str.count('1')
    grid.append(hash_str)

group_cnt = 0
while True:
    group_members = []
    x, y = find_first_empty(grid)
    if x != -1 and y != -1:
        group_members.append((x, y))
        grid[x][y] = '0'
        nr_members_group = 0

        while group_members:
            new_group_members = []
            for c in group_members:
                _x, _y = c

                if _x + 1 < 128 and grid[_x + 1][_y] == '1':
                    new_group_members.append((_x + 1, _y))
                if _x - 1 >= 0 and grid[_x - 1][_y] == '1':
                    new_group_members.append((_x - 1, _y))
                if _y + 1 < 128 and grid[_x][_y + 1] == '1':
                    new_group_members.append((_x, _y + 1))
                if _y - 1 >= 0 and grid[_x][_y - 1] == '1':
                    new_group_members.append((_x, _y - 1))

                grid[_x][_y] = '0'
                nr_members_group += 1

            group_members = new_group_members
        group_cnt += 1
        if group_cnt < 10:
            print("Group nr: " + str(group_cnt) + " has " + str(nr_members_group) + ' members')
    else:
        break

print('Group count: ' + str(group_cnt))

print('Number of squares used: ' + str(used_cnt))
for _x in range(0, 8):
    print(grid[_x][0:8])
