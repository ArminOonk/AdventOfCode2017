import math

with open('day20Input.txt', 'r') as f:
    data = f.readlines()


class Particle:
    def __init__(self, d):
        vals = d.split(' ')
        self.p = list(map(int, vals[0][vals[0].index('<') + 1: vals[0].index('>')].split(',')))
        self.v = list(map(int, vals[1][vals[1].index('<') + 1: vals[1].index('>')].split(',')))
        self.a = list(map(int, vals[2][vals[2].index('<') + 1: vals[2].index('>')].split(',')))
        self.alive = True

    def integrate(self):
        for i in range(0, 3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

    def distance(self, other):
        diff = []
        for i in range(0, 3):
            diff.append(self.p[i]-other.p[i])
        return sum(map(abs, diff))


state = []

for d in data:
    state.append(Particle(d))

cnt = 0
while True:
    for i in range(0, len(state)):
        for j in range(i + 1, len(state)):
            if state[i].distance(state[j]) == 0:
                state[i].alive = False
                state[j].alive = False

    state = [x for x in state if x.alive]

    for s in state:
        s.integrate()

    cnt += 1
    if cnt % 200:
        print('Surviving: ' + str(len(state)))
