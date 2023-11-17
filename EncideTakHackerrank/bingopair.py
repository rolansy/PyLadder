def count_bingo_pairs(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                count += 1
    return count

n = int(input())
a = list(map(int, input().split()))
m = int(input())

initial_count = count_bingo_pairs(a)

for _ in range(m):
    l, r = map(int, input().split())
    a[l-1:r] = reversed(a[l-1:r])
    count = count_bingo_pairs(a)
    print("odd" if count % 2 != initial_count % 2 else "even")