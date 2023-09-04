import sys
input = sys.stdin.readline

count, div = map(int,input().split())
inp_lis = list(map(int, input().split()))
sum = 0
sum_lis = [0] * count
rem = [0] * div
sum_lis[0] = inp_lis[0]
res = 0

for i in range(1,count):
  sum_lis[i] =sum_lis[i-1] + inp_lis[i]

for i in range(count):
  sum_lis[i] = sum_lis[i] % div
  if sum_lis[i] == 0:
    res += 1
  rem[sum_lis[i]] += 1
for i in range(div):
  if rem[i] > 1:
    res += (rem[i] * (rem[i] - 1) // 2)

print (res)