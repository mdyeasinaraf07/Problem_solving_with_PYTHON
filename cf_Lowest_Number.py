n = int(input())
arr = list(map(int, input().split()))
# lowest_num = arr[0]
# lowest_num_index = 1;
# for i in range(1, n):
#     if arr[i] < lowest_num:
#         lowest_num = arr[i]
#         lowest_num_index = i + 1
lowest_num = min(arr)
lowest_num_index = arr.index(lowest_num) + 1


print(lowest_num, lowest_num_index)