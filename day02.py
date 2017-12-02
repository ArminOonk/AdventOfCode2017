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
    checksum += max(row) - min(row)
print('Checksum: ' + str(checksum))
