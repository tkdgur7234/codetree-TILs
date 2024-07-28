arr = list(map(int, input().split()))
plus = 0
num = 0;
for i in range(0, len(arr)):
    if arr[i] >= 250:
        break
    plus += arr[i]
    num += 1
print(f"{plus} {plus/num:.1f}")