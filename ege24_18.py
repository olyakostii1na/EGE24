file = open('24 (4).txt')
s = file.readline()
st = ''
for i in range(len(s) - 1):
    if s[i] == 'A':
        st += s[i + 1]

bukva = ''
maxx = -1

for i in range(len(st)):
    if st.count(st[i]) > maxx:
        bukva = st[i]
        maxx = st.count(st[i])
print(bukva)
