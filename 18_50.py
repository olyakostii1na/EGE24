file = open('18_49.txt')
s = file.readline()
n = 3
sum = 0
max_sum = 0
a = []
while s != '':
    a.append(int(s))
    s = file.readline()
for i in range(len(a) - n):
    for j in range(i + n, len(a)):
        sum = a[i] + a[j]
        if sum > max_sum:
            max_sum = max(sum, max_sum)
        else:
            max_sum = 0
print(max_sum)