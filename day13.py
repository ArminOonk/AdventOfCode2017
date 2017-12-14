with open('day13Input.txt', 'r') as f:
    data = f.readlines()


def get_fire_pos(t, r):
    x = t % (2 * (r - 1))
    if x < r:
        fire_loc = x % r
    else:
        fire_loc = (r - 2) - (x % r)
    return fire_loc


def walk_firewall(t0, firewall, firewall_length):
    p = 0
    severity = 0
    t = t0
    hit_cnt = 0

    while p <= firewall_length:
        if p in firewall:
            if get_fire_pos(t, firewall[p]) == 0:
                severity += p * firewall[p]
                hit_cnt += 1

        p += 1
        t += 1
    return severity, hit_cnt


firewall = dict()
firewall_length = 0
for d in data:
    vals = list(map(int, d.split(':')))
    firewall[vals[0]] = vals[1]
    if vals[0] > firewall_length:
        firewall_length = vals[0]

# print('Firewall length: ' + str(firewall_length))
severity, _ = walk_firewall(0, firewall, firewall_length)
print("End of firewall, severity: " + str(severity))

start_time = 0
while True:
    _, hit = walk_firewall(t0=start_time, firewall=firewall, firewall_length=firewall_length)
    if hit == 0:
        break
    start_time += 1

    if start_time % 1000 == 0:
        print("Time: " + str(start_time))

print("Correct start time: " + str(start_time))
