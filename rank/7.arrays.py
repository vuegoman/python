if __name__ == '__main__':
  # n = int(input().strip())
  n = 4

  arr = list(map(int, input().rstrip().split()))
  # arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
  print(arr)
  # arr = [int(arr_temp) for arr_temp in '1 2 3 4 5'.split(' ')]

  reversed_array = []
  for i in range(n):
    reversed_array.append(arr[n-i-1])
  output_string = ''
  for i in range(len(reversed_array)):
    output_string += str(reversed_array[i]) + ' '

print(' '.join(str(i) for i in reversed_array))