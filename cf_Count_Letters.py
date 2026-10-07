strr = input()
char_countt = {}
for char in strr:
    char_countt[char] = char_countt.get(char, 0) + 1

for char, countt in sorted(char_countt.items()):
    print(f"{char} : {countt}")