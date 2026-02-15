class Heap:
    def __init__(self):
        self.heap = []

    def add(self, value):
        self.heap.append(value)
        cur_index = len(self.heap) - 1
        parent_index = (cur_index - 1) // 2
        while (cur_index > 0) and (value > self.heap[parent_index]):
            self.heap[cur_index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[cur_index]
            )
            cur_index = parent_index
            parent_index = (cur_index - 1) // 2
        return

    def pop(self):
        result = self.heap[0]
        cur_value = self.heap.pop()
        if len(self.heap) == 0:
            return result
        self.heap[0] = cur_value
        cur_index = 0
        while True:
            i_first_child, i_second_child = (cur_index * 2 + 1), (cur_index * 2 + 2)
            if i_first_child >= len(self.heap):
                break
            elif i_second_child >= len(self.heap):
                first_child, second_child = self.heap[i_first_child], -1
            else:
                first_child, second_child = self.heap[i_first_child], self.heap[i_second_child]
            if cur_value < max(first_child, second_child):
                if first_child > second_child:
                    self.heap[cur_index], self.heap[i_first_child] = first_child, cur_value
                    cur_index = i_first_child
                else:
                    self.heap[cur_index], self.heap[i_second_child] = second_child, cur_value
                    cur_index = i_second_child
            else:
                break
        return result

    def __str__(self):
        return ' '.join(map(str, self.heap))


def main():
    heap = Heap()
    with open('input.txt', 'r') as file_in:
        count_operation = int(file_in.readline().strip())
        for _ in range(count_operation):
            operation = file_in.readline().strip().split()
            command = operation[0]
            if command == '0':
                value = int(operation[1])
                heap.add(value)
            elif command == '1':
                print(heap.pop())


if __name__ == '__main__':
    main()
