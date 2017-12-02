with open('day02Input.txt', 'r') as f:
    data = f.readlines()

spreadsheet = []
for d in data:
    vals = d.replace('\t', ' ').split(' ')
    row = []
    for v in vals:
        row.append(int(v))
    spreadsheet.append(row)

checksum = 0
for row in spreadsheet:
    txt = ''
    for cell in row:
        txt += str(cell) + ' '
    print(txt)
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            a = row[i]
            b = row[j]
            # print('testing: '+ str(a)+ ' ' + str(b))
            if max([a, b]) % min([a, b]) == 0:
                print('Evenly divible: ' + str(a) + ' ' + str(b))
                checksum += int(max([a, b]) / min([a, b]))

                # checksum += max(row) - min(row)
print('Checksum: ' + str(checksum))
