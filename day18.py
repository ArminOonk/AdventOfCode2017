with open('day18Input.txt', 'r') as f:
    data = f.readlines()

registers = dict()
cnt = 0
sound_playing = 0


def get_value(v):
    try:
        ret = int(v)
    except:
        if v in registers:
            ret = registers[v]
        else:
            ret = 0
    return ret


def set_value(reg, v):
    if reg not in registers:
        registers[reg] = 0
    registers[reg] = get_value(v)


while True:
    try:
        command = [x.strip() for x in data[cnt].split(' ')]
        if command[0] == 'snd':
            sound_playing = get_value(command[1])
        elif command[0] == 'set':
            set_value(command[1], command[2])
        elif command[0] == 'add':
            set_value(command[1], get_value(command[1]) + get_value(command[2]))
        elif command[0] == 'mul':
            set_value(command[1], get_value(command[1]) * get_value(command[2]))
        elif command[0] == 'mod':
            set_value(command[1], get_value(command[1]) % get_value(command[2]))
        elif command[0] == 'rcv':
            if sound_playing:
                print("Sound playing: " + str(sound_playing))
                break
        elif command[0] == 'jgz':
            val = get_value(command[1])
            if val:
                cnt += get_value(command[2])
                continue
        else:
            print("Unknown command")
            break
        cnt += 1

        print(str(cnt) + ' Registers')
        for key, value in registers.items():
            print(key + ': ' + str(value))

    except IndexError as ex:
        print("Index error: " + str(ex))
        print("Index cnt: " + str(cnt))
        break

print('Registers')
for key, value in registers.items():
    print(key + ': ' + str(value))