file = open('24-j4.txt')
s = file.readline()
k = 0
for i in range(len(s) - 5):
    if s[i] != 'J' and s[i + 5] != 'J':
        if s[i + 1] == 'B' and s[i + 2] == 'O' and s[i + 3] == s[i + 4] == 'S':
            k += 1
print(k)