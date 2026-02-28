class MathOperationEval:
    def __init__(self, equation: list[str]):
        self.equation: list[str] = equation
        self.error: bool = False
        self.operators: set[str] = {'+', '-', '*', '/'}

    def operation(self, v1: float, v2: float, oper: str) -> float:
        if oper == '+':
            return v1 + v2
        elif oper == '-':
            return v1 - v2
        elif oper == '*':
            return v1 * v2
        else:
            if not v2:
                self.error = True
                return 0
            return v1/v2

    def add_number(self, v2: float, stack: list[float | str]) -> list:
        if stack and stack[-1] in self.operators:
            opearator: str = stack.pop()
            if stack and isinstance(stack[-1], float):
                result = self.operation(float(stack.pop()), v2, opearator)
                self.add_number(result, stack)
        elif not stack:
            stack.append(v2)
        return stack

    def solving(self, start):
        cur_stack = []
        i = start
        while i < len(self.equation):
            if self.error:
                return 0, i
            el: str = self.equation[i]
            if el == ' ':
                i += 1
                continue
            if el.isalpha():
                self.error = True
                return 0, i
            elif el == '(':
                v2, i = self.solving(i + 1)
                self.add_number(v2, cur_stack)
            elif el == ')':
                if len(cur_stack) == 1:
                    return cur_stack[-1], i
                self.error = True
                return 0, i + 1
            elif el in self.operators:
                cur_stack.append(el)
            elif el.isdigit():
                self.add_number(float(el), cur_stack)
            i += 1
        if len(cur_stack) == 1:
            return cur_stack[-1], i+1

    def validate(self):
        stack_scobes = []
        for i in range(len(self.equation)):
            el = self.equation[i]
            if el.isalpha():
                self.error = True
                return
            elif el == '(':
                stack_scobes.append(el)
            elif el == ')':
                if not stack_scobes:
                    self.error = True
                    return
                stack_scobes.pop()
            if el == ' ':
                if (
                    (self.equation[i - 1].isdigit() and self.equation[i + 1].isdigit())
                    or (self.equation[i - 1] in self.operators and self.equation[i + 1] in self.operators)
                ):
                    self.error = True
                    return


def main():
    with open('input.txt', 'r') as file_in:
        equation: list[str] = list(file_in.readline().strip())
    math = MathOperation(equation)
    math.validate()
    result, i = math.solving(0)
    if math.error:
        print('WRONG')
    else:
        print(f'{result:g}')


if __name__ == '__main__':
    main()
