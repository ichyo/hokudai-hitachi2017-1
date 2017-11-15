import sys
import random

v, e = map(int, sys.stdin.readline().split())
for _ in range(e):
    _, _, _ = sys.stdin.readline().split()

vm, em = map(int, sys.stdin.readline().split())

for _ in range(em):
    _, _ = sys.stdin.readline().split()

ans = random.sample([i+1 for i in range(vm)], k=v)

for i, x in enumerate(ans):
    print("{} {}".format(i+1, x))

