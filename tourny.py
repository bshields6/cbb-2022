with open('Scores.txt') as f:
    data = f.read().splitlines()

for i in data:
    if 'Tournament' not in i:
        print(i)