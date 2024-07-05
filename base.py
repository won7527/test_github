B, N = input().split()
B: str = B[::-1]
N: int = int(N)
num: int = 0
for i in range(len(B)):
    temp_num = 0
    if 'A' <= B[i] <= 'Z':
        temp_num = ord(B[i]) - ord('A') + 10
    else:
        temp_num = int(B[i])
    num += temp_num * (N ** i)
print(num)