buffer = [0, 1]
# puzzle_input = 2017
puzzle_input = 328
current_pos = 1

for i in range(2, 50000000+1):
    index = (current_pos + puzzle_input) % (i)  # len(buffer)
    if index == 0:
        buffer.insert(index + 1, i)
    current_pos = index + 1

    # print(str(index) + ' ' + str(buffer) + ' len(buffer): ' + str(len(buffer)))
    # print(str(i) + ' ' + str(len(buffer)))

index_of_zero = buffer.index(0)

# print("Next value: " + str(buffer[current_pos + 1]))
print("Value after 0 value: " + str(buffer[index_of_zero + 1]) + ' index of zero: ' + str(index_of_zero))
