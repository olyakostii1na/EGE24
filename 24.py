file = open('24-j3.txt')
s = file.readline()

k_tik = s.count('TIK')
k_tok = s.count('TOK')
print(k_tik + k_tok)
