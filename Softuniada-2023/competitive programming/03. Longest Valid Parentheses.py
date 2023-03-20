def valid_parentheses_combinations(expression):
    symbols = []
    current_symbols = []

    for index, char in enumerate(expression):
        try:
            if char == "(":
                if expression[index + 1] == ")":
                    current_symbols.append(char), current_symbols.append(expression[index + 1])

                else:
                    if len(current_symbols) > len(symbols):
                        symbols = current_symbols
                    current_symbols = []
        except IndexError:
            break

    if len(current_symbols) > len(symbols):
        symbols = current_symbols

    return len(symbols)


expression = input()
print(valid_parentheses_combinations(expression))
