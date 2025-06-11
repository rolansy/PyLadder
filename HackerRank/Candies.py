def candies(n, arr):
    candies = [1] * n

    # Left to right: if right child has higher rating, give more candies than left
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            candies[i] = candies[i-1] + 1

    # Right to left: if left child has higher rating, give more candies than right
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    return sum(candies)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()