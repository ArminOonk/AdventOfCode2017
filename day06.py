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

while True:
    nr_cycles += 1
    index = get_max_index(memory)
    val = memory[index]

    memory[index] = 0
    for i in range(val):
        memory[(index + i + 1) % nr_banks] += 1

    current_state = ' '.join(map(str, memory))
    print(str(nr_cycles) + ': ' + current_state)

    if current_state in history:
        break
    history.append(current_state)
