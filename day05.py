with open('day05Input.txt', 'r') as f:
    data = f.readlines()

offsets = []
steps = 0
cur_pos = 0

for d in data:
    offsets.append(int(d))

try:
    while True:
        jump = offsets[cur_pos]
        if jump >= 3:
            offsets[cur_pos] -= 1
        else:
            offsets[cur_pos] += 1
        cur_pos += jump
        steps += 1

except IndexError:
    print("Index error. cur_pos: " + str(cur_pos))

print("Number of steps: " + str(steps))
