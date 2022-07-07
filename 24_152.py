file = open('24-j9.txt')
s = file.readline()
k = 0
for i in range(len(s)):
    if s[i] == s[-i]:
        print(s[i], s[-i])
        k += 1
print(k)