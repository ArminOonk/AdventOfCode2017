with open('day21Input.txt', 'r') as f:
    data = f.readlines()

book = dict()
pat = '.#./..#/###'


def flip_x(p):
    vals = p.split('/')
    flip = []
    for v in vals:
        flip.append(v[::-1])
    return '/'.join(flip)


def flip_y(p):
    vals = p.split('/')
    return '/'.join(vals[::-1])


def rot90(p):
    vals = p.split('/')
    flip = []
    for v in vals:
        flip.append([' '] * len(vals))

    for x in range(0, len(vals)):
        for y in range(0, len(vals)):
            x_rot = len(vals) - y - 1
            y_rot = x
            flip[x_rot][y_rot] = vals[x][y]

    flip_str = []
    for f in flip:
        flip_str.append(''.join(f))
    return '/'.join(flip_str)


def rot180(p):
    return rot90(rot90(p))


def rot270(p):
    return rot90(rot180(p))


def show(p):
    print(p.replace('/', '\n') + '\n')


def all_options(p):
    ret = []
    ret.append(p)
    ret.append(rot90(p))
    ret.append(rot180(p))
    ret.append(rot270(p))

    ret.append(flip_x(p))
    ret.append(flip_x(rot90(p)))
    ret.append(flip_x(rot180(p)))
    ret.append(flip_x(rot270(p)))

    ret.append(flip_y(p))
    ret.append(flip_y(rot90(p)))
    ret.append(flip_y(rot180(p)))
    ret.append(flip_y(rot270(p)))

    return ret


def insert_book(_key, _value):
    # print('insert: ' + _key + ' --> ' + _value)

    if _key in book:
        # print('key ' + key + ' already in book. New value: ' + value + ' old value: ' + book[key])
        if _value != book[_key]:
            print('Same key: ' + _key + ' , different value. New value: ' + _value + ' old value: ' + book[_key])
    book[_key] = _value


for d in data:
    vals = d.split(' => ')
    for ao in all_options(vals[0]):
        insert_book(ao, vals[1].rstrip())

iteration = 0

for _ in range(0, 5):
    vals = pat.split('/')
    image = []
    size = len(vals)

    if size % 2 == 0:
        image_tmp = []
        for v in vals:
            image_tmp.append([v[x:(x + 2)] for x in range(0, len(v), 2)])

        for y in range(0, size, 2):
            i_tmp = []
            for x in range(0, int(size / 2)):
                i_tmp.append(image_tmp[y][x] + '/' + image_tmp[y + 1][x])
            image.append(i_tmp)
    else:
        image_tmp = []
        for v in vals:
            image_tmp.append([v[x:(x + 3)] for x in range(0, len(v), 3)])

        for y in range(0, size, 3):
            i_tmp = []
            for x in range(0, int(size / 3)):
                i_tmp.append(image_tmp[y][x] + '/' + image_tmp[y + 1][x] + '/' + image_tmp[y + 2][x])
            image.append(i_tmp)

    for x in range(0, len(image)):
        for y in range(0, len(image)):
            image[x][y] = book[image[x][y]]

    ret = []
    for img in image:
        block_size = len(img[0].split('/'))
        for x in range(0, block_size):
            txt = ''
            for i in img:
                vals = i.split('/')
                txt += vals[x]
            ret.append(txt)

    pat = '/'.join(ret)
    print(pat.replace('/', "\r\n"))
    iteration += 1
    print('iteration: ' + str(iteration) + ' number on: ' + str(pat.count('#')))
