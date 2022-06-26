file = open('24 (5).txt')
s = file.readline()
st = ''
for i in range(len(s) - 2):
    if s[i] == s[i + 2]:
        st += s[i + 1]

bukva = ''
max = -1
for i in range(len(st)):
    if st.count(st[i]) > max:
        bukva = st[i]
        max = st.count(st[i])
print(bukva)