n = int(input())
arr = list(map(int, input().split()))

even_num = list(filter(lambda x: x % 2 == 0, arr))
square_num = list(map(lambda x: x **2, even_num))

print(square_num)