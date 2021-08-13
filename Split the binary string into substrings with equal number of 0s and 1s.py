string = input()
x = 0
y = 0
c = 0
for i in range(len(string)):
    if (string[i] == '0'):
        x = x + 1
    else:
        y = y + 1
    if x == y:
        c = c + 1
if x!=y:
    print("-1")
else:
    print(c)
