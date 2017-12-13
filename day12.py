with open('day12Input.txt', 'r') as f:
    data = f.readlines()

programs = dict()
for x in range(0, len(data)):
    programs[x] = 0
group = 1

while True:
    connected_list = []
    for key, value in programs.items():
        if value == 0:
            connected_list = [key]

    if not connected_list:
        print('Nr of groups: ' + str(group - 1))
        break

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
    for c in connected_list:
        programs[c] = group
    group += 1

    # print(';'.join(vals))
# print('Number of programs connected: ' + str(nr_connected))

