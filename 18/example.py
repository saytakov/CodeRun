def parse_expression(expr):
    tokens = list(expr.replace(' ', ''))
    pos = 0

    def parse_primary():
        nonlocal pos
        if tokens[pos] == '1':
            pos += 1
            return 1
        elif tokens[pos] == '0':
            pos += 1
            return 0
        elif tokens[pos] == '!':
            pos += 1
            return int(not parse_primary())
        elif tokens[pos] == '(':
            pos += 1
            result = parse_or_xor()
            if tokens[pos] == ')':
                pos += 1
            return result

    def parse_and():
        nonlocal pos
        left = parse_primary()
        while pos < len(tokens) and tokens[pos] == '&':
            pos += 1
            right = parse_primary()
            left = left & right
        return left

    def parse_or_xor():
        nonlocal pos
        left = parse_and()
        while pos < len(tokens) and tokens[pos] in '|^':
            op = tokens[pos]
            pos += 1
            right = parse_and()
            if op == '|':
                left = left | right
            else:
                left = left ^ right
        return left

    return parse_or_xor()


def main():
    expr = input().strip()
    print(parse_expression(expr))

if __name__ == '__main__':
    main()