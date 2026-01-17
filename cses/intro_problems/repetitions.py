dna_seq = input()
max_len = 0
i = 0

for j in range(len(dna_seq)+1):
    if j == len(dna_seq):
        max_len = max(max_len, (j - i))
        break

    if dna_seq[i] != dna_seq[j]:
        max_len = max(max_len, (j - i))
        i = j

print(max_len)