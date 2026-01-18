pal_list = list()

def is_palindrome(i):
    if str(i) == str(i)[::-1]: return True

for i in range(1, 10**6+1):
    if is_palindrome(i):
        pal_list.append(i)

sums_of_two = set()

for i in range(len(pal_list)):
    for j in range(i, len(pal_list)):
        sums_of_two.add(pal_list[i] + pal_list[j])

count = 0
for i in range(1, 10**6+1):
    if i not in sums_of_two and not is_palindrome(i):
        count += 1

print(count)
