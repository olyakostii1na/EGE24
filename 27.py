file = open('k7b-1.txt')
s = file.readline()
max_len = 0
k = 0
for i in range(len(s)):
    if k % 3 == 0 and s[i] == 'E' or k % 3 == 1 and s[i] == 'A' or k % 3 == 2 and s[i] == 'B':
        k += 1
        max_len = max(k, max_len)
    elif s[i] == 'E':
        k = 1
    else:
        k = 0
print(max_len)