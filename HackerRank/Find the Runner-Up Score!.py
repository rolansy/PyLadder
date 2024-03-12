n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
m=arr[0]
r=0
for num in arr:
    if num<m:
        r=num
        break
print(r)