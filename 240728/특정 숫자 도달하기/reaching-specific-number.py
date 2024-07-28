arr = list(map(int, input().split()))
plus = 0
for i in range(0, len(arr)):
    if arr[i] >= 250:
        break
    plus += arr[i]
print(f"{plus} {plus/i:.1f}")