file = open('24-5.txt')
s = file.readline()
k = 0
max_len = 0
for i in range(len(s) - 1):
    if s[i] == '(' and s[i] == s[i + 1]:
        k += 1
        max_len = max(k, max_len)
print(max_len)