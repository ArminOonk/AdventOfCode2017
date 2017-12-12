with open('day08Input.txt', 'r') as f:
    data = f.readlines()

register = dict()
largest_register = ''
largest_value = -99999999999999999999999

for d in data:
    vals = d.split()

    target = vals[0]
    if target not in register:
        register[target] = 0

    change = 1
    if vals[1] == 'dec':
        change = -1

    change = change * int(vals[2])

    condition = vals[4]
    if condition not in register:
        register[condition] = 0

    if vals[5] == '>':
        if register[condition] > int(vals[6]):
            register[target] += change
    elif vals[5] == '<':
        if register[condition] < int(vals[6]):
            register[target] += change
    elif vals[5] == '<=':
        if register[condition] <= int(vals[6]):
            register[target] += change
    elif vals[5] == '>=':
        if register[condition] >= int(vals[6]):
            register[target] += change
    elif vals[5] == '==':
        if register[condition] == int(vals[6]):
            register[target] += change
    elif vals[5] == '!=':
            if register[condition] != int(vals[6]):
                register[target] += change
    else:
        print('Unknown operator: ' + vals[5])

    if register[target] > largest_value:
        largest_value = register[target]
        largest_register = target

print('Runtime largest register is ' + largest_register + ' with value ' + str(largest_value))

largest_register = ''
largest_value = -99999999999999999999999

for key, value in register.items():
    if value > largest_value:
        largest_value = value
        largest_register = key

print('Finished largest register is ' + largest_register + ' with value ' + str(largest_value))