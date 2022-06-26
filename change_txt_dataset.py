import os

with open('chicken/data/chicken2/training.txt', 'w') as out:
    for img in [f for f in os.listdir("chicken/data/chicken2" + '/train') if f.endswith('jpg')]:
        out.write('chicken/data/chicken2/train/' + img + '\n')


with open('chicken/data/chicken2/valid.txt', 'w') as out:
    for img in [f for f in os.listdir('chicken/data/chicken2' + '/valid') if f.endswith('jpg')]:
        out.write('chicken/data/chicken2/valid/' + img + '\n')
