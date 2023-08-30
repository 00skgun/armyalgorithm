import sys

input = sys.stdin.readline

size, qus = map(int, input().split())
inp_lis = [[0] * (size + 1)]
sum_lis = [[0] * (size + 1) for _ in range(size + 1)]
for i in range(size):
  inp_row = [0] + [int(x) for x in input().split()]
  inp_lis.append(inp_row)

for i in range(1, size + 1):
  for j in range(1, size + 1):
      sum_lis[i][j] = sum_lis[i][j - 1] + sum_lis[i - 1][j] - sum_lis[i - 1][j - 1] + inp_lis[i][j]
for _ in range(qus):
  x_1, y_1, x_2, y_2 = map(int, input().split())
  print(sum_lis[x_2][y_2] - sum_lis[x_1 - 1][y_2] - sum_lis[x_2][y_1 - 1] + sum_lis[x_1 - 1][y_1 - 1])