def countingValleys(steps, path):
    path = list(path)
    v = 0
    valleys = 0
    for step in path:
        if step == 'U':
            v += 1
            if v == 0:
                valleys += 1
        else:
            v -= 1
    return valleys

steps=12
path='DDUUDDUDUUUD'
print(countingValleys(steps, path)) 