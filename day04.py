with open('day04Input.txt', 'r') as f:
    data = f.readlines()

valid_cnt = 0
for d in data:
    vals = d.split()
    is_valid = True
    for i in range(len(vals)):
        for j in range(i+1, len(vals)):
            a = ''.join(sorted(vals[i]))
            b = ''.join(sorted(vals[j]))
            if a == b:
                is_valid = False
    # print(' '.join(vals) + ' is_valid '+ str(is_valid))
    if is_valid:
        valid_cnt += 1
print('Total nr valid: ' + str(valid_cnt))

