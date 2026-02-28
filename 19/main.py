class MathOperationEval:
    def __init__(self, expr: str):
        self.expr = expr.replace(' ', '')
        self.pos = 0

    def parse_el(self):
        el = self.expr[self.pos]
        self.pos += 1
        if el == '1':
            return 1
        elif el == '0':
            return 0
        elif el == '!':
            return int(not self.parse_el())
        elif el == '(':
            result = self.parse_or_xor()
            if self.expr[self.pos] == ')':
                self.pos += 1
            return result

    def parse_and(self):
        left = self.parse_el()
        while self.pos < len(self.expr) and self.expr[self.pos] == '&':
            self.pos += 1
            right = self.parse_el()
            left = left & right
        return left

    def parse_or_xor(self):
        left = self.parse_and()
        while self.pos < len(self.expr) and self.expr[self.pos] in '^|':
            op = self.expr[self.pos]
            self.pos += 1
            right = self.parse_and()
            if op == '^':
                left = left ^ right
            else:
                left = left | right
        return left

    def result(self):
        return self.parse_or_xor()


def main():
    with open('input.txt', 'r') as file_in:
        expr = MathOperationEval(file_in.readline().strip())
    print(expr.result())


if __name__ == '__main__':
    main()
