def get_max_index(mem):
    index = 0
    largest_val = 0

    for i in range(len(mem)):
        if mem[i] > largest_val:
            largest_val = mem[i]
            index = i
    return index


with open('day06Input.txt', 'r') as f:
    data = f.readlines()

memory = []
for v in data[0].split():
    memory.append(int(v))

nr_banks = len(memory)
nr_cycles = 0
history = []
history.append(' '.join(map(str, memory)))
repeat_state = ''
first = 0

while True:
    nr_cycles += 1
    index = get_max_index(memory)
    val = memory[index]

    memory[index] = 0
    for i in range(val):
        memory[(index + i + 1) % nr_banks] += 1

    current_state = ' '.join(map(str, memory))
    # print(str(nr_cycles) + ': ' + current_state)

    if current_state in history and not repeat_state:
        repeat_state = current_state
        print('First time: ' + str(nr_cycles) + ': ' + current_state)
        first = nr_cycles

    if repeat_state == current_state and nr_cycles != first:
        print('Second time: ' + str(nr_cycles) + ': ' + current_state)
        print('diff: ' + str(nr_cycles-first))
        break

    history.append(current_state)
