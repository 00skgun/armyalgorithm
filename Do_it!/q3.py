import sys

input = sys.stdin.readline
a = input
data, qus = map(int, input().split())
inp_lis = list(map(int, input().split()))

n = 0
sum_lis = [0]

for i in inp_lis:
  sum_lis.append(i + n)
  n = i + n

for i in range(qus):
  q_a, q_b = map(int, input().split())
  print(sum_lis[q_b] - sum_lis[q_a - 1])
