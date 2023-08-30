import sys
input = sys.stdin.readline

count, div = map(int,input().split())
inp_lis = list(map(int, input().split()))
sum = 0
sum_lis = [0]
rem = [0] * div
res = 0

for i in inp_lis:
  sum_lis.append(i + sum)
  sum += i

for i in range(count):
  sum_lis[i] = sum_lis[i] % div
  if sum_lis[i] == 0:
    res += 1
  rem[sum_lis[i]] += 1
for i in range(div):
  if rem[i] > 1:
    res += rem[i] * (rem[i] - 1) // 2

print (res)