file = open('k8-1.txt')
s = file.readline()
k = 0
max_len = 0
for i in range(len(s) - 2):
    if s[i] != s[i - 1] != s[i + 1]:
        k += 1
        max_len = max(k, max_len)
print(max_len)
