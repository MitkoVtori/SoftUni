def top_of_rocket(num):
    print('_'*((num+5)//2) + '^' + '_'*((num+5)//2))
    print('_' * (((num + 5) // 2)-1) + '/|\\' + '_' * (((num + 5) // 2)-1))
    print('_' * (((num + 5) // 2) - 2) + '/|||\\' + '_' * (((num + 5) // 2) - 2))

    n = 1
    while n <= (num//2):
        print('_' * (((num + 5) // 2) - (n+2)) + f'/{"."*n}|||{"."*n}\\' + '_' * (((num + 5) // 2) - (n+2)))
        n += 1

    print(f'_/{"."*(n-2)}|||{"."*(n-2)}\\_')


def middle_of_rocket(num):
    for row in range(number):
        print('_' * (((num + 5) // 2) - 1) + '|||' + '_' * (((num + 5) // 2) - 1))


def bottom_of_rocket(num):
    print('_' * (((num + 5) // 2) - 1) + '~~~' + '_' * (((num + 5) // 2) - 1))

    for n in range(num//2):
        print('_' * (((num + 5) // 2) - (n+2)) + f'//{"."*n}!{"."*n}\\\\' + '_' * (((num + 5) // 2) - (n+2)))


number = int(input())
top_of_rocket(number)
middle_of_rocket(number)
bottom_of_rocket(number)
