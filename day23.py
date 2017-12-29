with open('day23Input.txt', 'r') as f:
    data = f.readlines()

cnt = 0
registers = dict()
registers['a'] = 1
registers['b'] = 0
registers['c'] = 0
registers['d'] = 0
registers['e'] = 0
registers['f'] = 0
registers['g'] = 0
registers['h'] = 0
mul_cnt = 0


def get_value(v):
    try:
        ret = int(v)
    except:
        if v in registers:
            ret = registers[v]
        else:
            if v == 'a':
                ret = 1
            else:
                ret = 0
    return ret


def set_value(reg, v):
    if reg not in registers:
        registers[reg] = 0
    registers[reg] = get_value(v)


try:
    while True:
        jump_dist = 1
        vals = data[cnt].strip().split(' ')
        if vals[0] == 'set':
            set_value(vals[1], get_value(vals[2]))
        elif vals[0] == 'sub':
            set_value(vals[1], get_value(vals[1]) - get_value(vals[2]))
        elif vals[0] == 'mul':
            set_value(vals[1], get_value(vals[1]) * get_value(vals[2]))
            mul_cnt += 1
        elif vals[0] == 'jnz':
            if get_value(vals[1]):
                jump_dist = get_value(vals[2])
        else:
            print('Illegal instruction')
            break

        print(str(cnt) + ' ' + data[cnt].strip())
        for k, v in registers.items():
            print(k + ': ' + str(v))

        input()
        cnt += jump_dist

except IndexError as ex:
    print('Program finished: ' + str(ex))


print("mul called: " + str(mul_cnt) + ' times')
print("register h is: " + str(registers['h']))
