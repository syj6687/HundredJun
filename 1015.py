lenth = int(input())
numbers = list(map(int, input().split()))

p = [0 for i in range(lenth)]

cnt = 0

for i in range(1, 1001):
    for j in range(0, lenth):
        if(numbers[j] == i):
            p[j] = cnt
            cnt = cnt + 1

print(*p)
