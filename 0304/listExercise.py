# list 列表小练习
import random
counts = [0] * 6
for _ in range(6000):
    face = random.randint(1,6)
    counts[face -1] += 1
for face in range(1,7):
    print(f'{face}点出现了{counts[face - 1]}次')