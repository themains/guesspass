import sys
import random

filename = sys.argv[1]
sample_size = int(sys.argv[2])
reservoir = []

with open(filename, 'r') as f:
    for i, line in enumerate(f):
        if i < sample_size:
            reservoir.append(line)
        else:
            r = random.randint(0, i)
            if r < sample_size:
                reservoir[r] = line

for line in reservoir:
    print(line, end='')
