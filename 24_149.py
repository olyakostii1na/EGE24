file = open('24-s2.txt')
s = file.readline()
bukva = ''
for i in range(len(s) - 2):
    if s[i] == 'X' and s[i + 2] == 'Z':
        bukva += s[i + 1]
bukva_v_otvet = ''
max_count = 0
for i in range(len(bukva)):
    if bukva.count(bukva[i]) > max_count:
        max_count = bukva.count(bukva[i])
        bukva_v_otvet = bukva[i]
print(bukva_v_otvet, max_count)