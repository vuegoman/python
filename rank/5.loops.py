n = int(input())

for i in range(0, 10):
  # print(str(n) + " x " + str(i+1) + " = " + str(n*(i+1)))
  product = n*i
  print('{} x {} = {}'.format(n, i, product))