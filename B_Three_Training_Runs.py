def average(a, b, c):
    return (a + b + c) / 3

a, b , c = map(int, input().split())
ans = average(a, b, c)
print(ans)