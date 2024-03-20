sum, len = map(int, input().split())
numbers = []

# if(sum % 2 == 0):
#     if(type(sum / len) != "int"):
#         numbers = [0 for i in range(len)]
#         for i in range(0, len):
#             numbers[i] = int((sum/len) - (len/2) + i + 0.5)



if(sum % 2 == 0): #짝수
    for i in range(len, 101):
        if(i % 2 == 0):
            print("1")
        if((sum / i) % 2 == 0 and i != 2 and i % 2 == 0): #가운데 짝수
            print(i)
            numbers = [0 for i in range(i)]
            for j in range(0, i):
                numbers[j] = int((sum / i) - ((i - 1) / 2) + j)
            break



else: #홀수
    if(len == 2):#예외처리
        if(sum % 2 == 1):
            numbers = [int((sum - 1) / 2), int((sum - 1) / 2 + 1)]
        else:
            print(1)
            #정석





print(*numbers)

