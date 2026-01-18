n = int(input())

def main():
    if str(n) == str(n)[::-1]:
        return [n]

    pal_list = list()
    pal_set = set()

    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            pal_list.append(i)
            pal_set.add(i)

    for pal in pal_list:
        if n - pal in pal_set:
            return [pal, n - pal]

    pal_triples = list()
    for i in range(len(pal_list)):
        for j in range(i, len(pal_list)):
            if n - (pal_list[i] + pal_list[j]) in pal_set:
                pal_triples.append([pal_list[i], pal_list[j], n - (pal_list[i] + pal_list[j])])
        if len(pal_triples) == 1:
            return pal_triples[0]
        elif len(pal_triples) > 1:
            return max(pal_triples, key=lambda triple: max(triple))

print(' '.join(map(str, main())))
