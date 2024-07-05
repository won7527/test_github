N, B = map(int, input().split())
num: str = ''
while(N):
    temp_num: str = ''
    if N % B >= 10:
        temp_num = chr(N % B - 10 + ord('A'))
    else:
        temp_num = str(N % B)
    num += temp_num
    N //= B
print(num[::-1])