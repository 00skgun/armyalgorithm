import sys

input = sys.stdin.readline

size, qus = map(int, input().split())
sum_lis = [0],[0]
inp_lis = [],[]
for i in range(size):
  sum = 0
  inp_lis[i].append(list(map(int, input().split())))
  for j in inp_lis[i]:
    sum = sum + j
    sum_lis[i].append(sum)

for i in range(size):
  sum = 0
  for j in range(size):
    sum = sum + sum_lis[j][i]
    sum_lis[j][i] = sum

x_1, y_1, x_2, y_2 = map(int, input().split())
print(sum_lis[x_1][y_1] - sum_lis[x_2][y_2])