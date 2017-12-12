
def get_score(txt):
    score = 0
    level = 0

    garbage = False
    ignore = False
    for t in txt:
        if ignore:
            ignore = False
            continue

        if garbage:
            if t == '!':
                ignore = True
            elif t == '>':
                garbage = False
        else:
            if t == '<':
                garbage = True
            if t == '{':
                level += 1
                score += level
            if t == '}':
                level -= 1

    return score


with open('day09Input.txt', 'r') as f:
    data = f.readlines()

for d in data:
    d = d.strip()
    score = get_score(d)
    if len(d) < 80:
        print('Input: ' + d + ' score: ' + str(score))
    else:
        print('score: ' + str(score))