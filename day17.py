
buffer = [0]
# puzzle_input = 2017
puzzle_input = 328
current_pos = 0

for i in range(1, 2018):
    index = (current_pos + puzzle_input) % len(buffer)
    buffer.insert(index+1, i)
    current_pos = index + 1

    # print(str(index) + ' ' + str(buffer))

index_of_zero = buffer.index(0)

print("Next value: " + str(buffer[current_pos+1]))
print("Value after 0 value: " + str(buffer[index_of_zero+1]))
