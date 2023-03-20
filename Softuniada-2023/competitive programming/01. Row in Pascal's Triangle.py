from math import factorial


def triangle_of_pascal(num):
    lines = []

    for i in range(num+1):
        for j in range(i + 1):
            lines.append(factorial(i) // (factorial(j) * factorial(i - j)))

    return ' '.join([str(n) for n in lines[-(num+1):]])


number = int(input())
print(triangle_of_pascal(number))
