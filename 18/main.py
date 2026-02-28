class MathOperationEval:
    def __init__(self, expr: str):
        self.expr = expr
        self.operators = {'+', '-', '/', '*'}

    def _find_i_left(self, i: int) -> int:
        if i < 0:
            return -1
        while self.expr[i] == ' ':
            i -= 1
        return i

    def _find_i_right(self, i: int) -> int:
        if i > (len(self.expr) - 1):
            return -1
        while self.expr[i] == ' ':
            i += 1
        return i

    def validate(self):
        count_scobes = 0
        i = 0
        while i < len(self.expr):
            if self.expr[i].isalpha():
                return False
            elif self.expr[i] == ' ':
                left = self._find_i_left(i - 1)
                right = self._find_i_right(i + 1)
                if (
                    (left == -1 or right == -1)
                    or (self.expr[left].isdigit() and self.expr[right].isdigit())
                    or (self.expr[left] in self.operators and self.expr[right] in self.operators)
                ):
                    return False
            elif self.expr[i] in self.operators:
                left = self._find_i_left(i - 1)
                right = self._find_i_right(i + 1)
                if (
                    (left == -1 or right == -1)
                    or (self.expr[left] in self.operators)
                    or (self.expr[right] in self.operators)
                    or (self.expr[left] == '(')
                    or (self.expr[right] == ')')
                ):
                    return False
            elif self.expr[i] == '(':
                stack_scobes.append('(')



def main():
    with open('input.txt', 'r') as file_in:
        expr = file_in.readline().strip()
    expr_obj = MathOperationEval(expr)


if __name__ == '__main__':
    main()
