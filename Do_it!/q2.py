sub = int(input())
res_lis = list(map(int, input().split()))

total = 0
max = 0
for i in res_lis:
  total = total + i
  if max < i:
    max = i
avg = total * 100 / max / sub
print(avg)
