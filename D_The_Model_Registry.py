t = int(input())

def model_info(name, layers, lr = 0.01):
    print(f"Model: {name} Layers: {layers}, LR: {lr}")

for i in range (t):
    arr = list(input().split())

    if(len(arr) == 3):
        model_info(arr[0], arr[1], arr[2])
    else:
        model_info(arr[0], arr[1])



    