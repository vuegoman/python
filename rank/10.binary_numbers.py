import sys

def remain(n,r):
  if n<=1: 
    r.append(n)
  else:
    r.append(n%2)
    return remain(int(n/2), r)

n = int(input())
r = []

remain(n,r)

maxc = 0
c = 0
for i in range(len(r)):
  if r[i] == 1:
    c += 1
  else:
    c = 0
  if c > maxc:
    maxc = c
    
print(maxc)
maxc = sys.stdin.readline().strip()
