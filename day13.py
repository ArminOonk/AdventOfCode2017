with open('day13Input.txt', 'r') as f:
    data = f.readlines()


def get_fire_pos(t, r):
    x = t % (2 * (r - 1))
    if x < r:
        fire_loc = x % r
    else:
        fire_loc = (r - 2) - (x % r)
    return fire_loc


firewall = dict()
firewall_length = 0
for d in data:
    vals = list(map(int, d.split(':')))
    firewall[vals[0]] = vals[1]
    if vals[0] > firewall_length:
        firewall_length = vals[0]

print('Firewall length: ' + str(firewall_length))
position = 0
time = 0
severity = 0

while position <= firewall_length:
    if position in firewall:
        # print(str(time) + ': At firewall: ' + str(position))
        fire_loc = get_fire_pos(time, firewall[position])

        if fire_loc == 0:
            # print('Hit')
            severity += position * firewall[position]

    position += 1
    time += 1

print("End of firewall, severity: " + str(severity))