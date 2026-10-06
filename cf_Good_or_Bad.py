t = int(input())
while(t > 0):
    strr = input()
    countt1 = strr.count("101")
    countt2 = strr.count("010")
    if(countt1 == 0 and countt2 == 0):
        print("Bad")
    else:
        print("Good")
    t -= 1