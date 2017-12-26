def dist(v):
    return sum(map(abs, v))


def get_position(s, t):
    ret = []
    ret.append(0.5 * s['a'][0] * t * t + s['v'][0] * t + s['p'][0])
    ret.append(0.5 * s['a'][1] * t * t + s['v'][1] * t + s['p'][1])
    ret.append(0.5 * s['a'][2] * t * t + s['v'][2] * t + s['p'][2])
    return ret


with open('day20Input.txt', 'r') as f:
    data = f.readlines()

state = []

for d in data:
    ret = dict()
    vals = d.split(' ')
    ret['p'] = list(map(int, vals[0][vals[0].index('<') + 1: vals[0].index('>')].split(',')))
    ret['v'] = list(map(int, vals[1][vals[1].index('<') + 1: vals[1].index('>')].split(',')))
    ret['a'] = list(map(int, vals[2][vals[2].index('<') + 1: vals[2].index('>')].split(',')))
    state.append(ret)

smallest_accel = 99999999999999999999
for i, s in enumerate(state):
    p = dist(s['p'])
    v = dist(s['v'])
    a = dist(s['a'])
    if a <= smallest_accel:
        smallest_accel = a
        print("Smallest accel: " + str(smallest_accel) + ' at ' + str(i) + ' p far away: ' + str(dist(get_position(s, 10000))))
