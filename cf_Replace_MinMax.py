n = int(input())
arr = list(map(int, input().split()))
mini_idx = arr.index(min(arr))
maxi_idx = arr.index(max(arr))
temp = arr[mini_idx]
arr[mini_idx] = arr[maxi_idx]
arr[maxi_idx] = temp
print(*arr)
