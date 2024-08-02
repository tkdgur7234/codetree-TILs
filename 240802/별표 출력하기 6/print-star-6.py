n = int(input())
cnt = 2*n - 1
for i in range(2*n-1):
    if i >= n:
        spc = 2*n-2 - i
    else:
        spc = i
    for k in range(spc):
        print(" ", end=" ")
    for j in range(cnt):
        print("*", end=" ")
    print()
    if i < n -1:
        cnt -= 2
    else:
        cnt += 2