from sys import maxsize


def maximum_pancake_sum(pancake, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    max_numbers = []
    numbers = []
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        curr_num = pancake[i]

        if max_so_far + curr_num == 0:
            max_ending_here = 0
            numbers = []
            s = i + 1
            continue

        max_ending_here += curr_num
        numbers.append(curr_num)

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        elif max_ending_here == max_so_far:
            if len(numbers) > len(max_numbers):
                max_numbers = numbers
                start = i - (len(numbers) - 1)
                end = i
                numbers = []

        if max_ending_here < 0:
            max_ending_here = 0
            if len(numbers) > len(max_numbers):
                max_numbers = numbers
            numbers = []
            s = i + 1

    return f"{max_so_far} {start} {end}"


pancake = list(map(int, input().split()))
print(maximum_pancake_sum(pancake, len(pancake)))
