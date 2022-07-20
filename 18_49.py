file = open('18_49.txt')
s = file.readline()
n = 7
a = []
k = 0
diap = list(range(1500, 2000))
while s != '':
    a.append(int(s))
    s = file.readline()
for i in range(len(a) - n):
    for j in range(i + n, len(a)):
        if a[i] + a[j] in diap:
            k += 1
print(k)