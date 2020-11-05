import sys

n = int(sys.stdin.readline().strip())
d = dict()

for i in range(n):
  a = list(sys.stdin.readline().strip().split(' '))
  d[a[0]] = a[1]

q = sys.stdin.readline().strip()

while q:
  if d.get(q):
    print(q + "="+ d.get(q))
  else:
    print("Not found")
  q = sys.stdin.readline().strip()