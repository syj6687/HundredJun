sum, len = map(int, input().split())
numbers = []


for i in range(len, 101):
    if(sum%len == 0):
        j = int(sum/len - (len-1)/2)
        for k in range(j, j+len):
            numbers.append(k)
        break


print(*numbers)



