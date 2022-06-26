file = open('24-s1.txt')
s = file.readline()
count = 0
while s != '':
    if s.count('J') > s.count('E'):
        count += 1
    s = file.readline()

print(count)