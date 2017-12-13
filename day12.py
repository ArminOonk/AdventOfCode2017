with open('day12Input.txt', 'r') as f:
    data = f.readlines()

connected_list = [0]

nr_connected = len(connected_list)
prev_nr = 0

while nr_connected != prev_nr:
    prev_nr = nr_connected
    for d in data:
        vals = map(int, d.replace('<->', ',').split(','))
        connected = False
        for v in vals:
            if v in connected_list:
                connected = True
                break

        if connected:
            for v in vals:
                if v not in connected_list:
                    connected_list.append(v)
    nr_connected = len(connected_list)
    # print(';'.join(vals))
print('Number of programs connected: ' + str(nr_connected))

