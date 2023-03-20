from functools import cmp_to_key


numbers = list(map(int, input().split()))
largest_number = sorted(numbers, key=cmp_to_key(lambda i, j: -1 if str(j) + str(i) < str(i) + str(j) else 1))
print(''.join(map(str, largest_number)))
