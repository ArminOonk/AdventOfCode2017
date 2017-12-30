state = 'a'
steps = 12134527
# steps = 6
cursor = 0

tape = dict()


def set_value(v):
    if v == 1:
        tape[cursor] = 1
    else:
        if cursor in tape:
            del tape[cursor]


def get_value(c):
    if c in tape:
        return 1
    return 0


for _ in range(steps):
    val = get_value(cursor)
    if state == 'a':
        if val == 0:
            set_value(1)
            cursor += 1
            state = 'b'
        else:
            set_value(0)
            cursor -= 1
            state = 'c'
    elif state == 'b':
        if val == 0:
            set_value(1)
            cursor -= 1
            state = 'a'
        else:
            set_value(1)
            cursor += 1
            state = 'c'
    elif state == 'c':
        if val == 0:
            set_value(1)
            cursor += 1
            state = 'a'
        else:
            set_value(0)
            cursor -= 1
            state = 'd'
    elif state == 'd':
        if val == 0:
            set_value(1)
            cursor -= 1
            state = 'e'
        else:
            set_value(1)
            cursor -= 1
            state = 'c'
    elif state == 'e':
        if val == 0:
            set_value(1)
            cursor += 1
            state = 'f'
        else:
            set_value(1)
            cursor += 1
            state = 'a'
    elif state == 'f':
        if val == 0:
            set_value(1)
            cursor += 1
            state = 'a'
        else:
            set_value(1)
            cursor += 1
            state = 'e'
# if state == 'a':
#     if val == 0:
#         set_value(1)
#         cursor += 1
#     else:
#         set_value(0)
#         cursor -= 1
#     state = 'b'
# elif state == 'b':
#     if val == 0:
#         set_value(1)
#         cursor -= 1
#     else:
#         set_value(1)
#         cursor += 1
#     state = 'a'

print('Checksum: ' + str(len(tape)))