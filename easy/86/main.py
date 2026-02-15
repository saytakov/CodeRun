def change_summ(clients, name, summ, multiple=1):
    if name in clients:
        clients[name] += summ * multiple
    else:
        clients[name] = summ * multiple
    return


def main():
    clients = {}
    with open('input.txt', 'r') as file_in:
        operation = file_in.readline().strip().split()
        while operation:
            command = operation[0]
            if command == 'DEPOSIT' or command == 'WITHDRAW':
                name = operation[1]
                summ = int(operation[2])
                multiple = 1
                if command == 'WITHDRAW':
                    multiple = -1
                change_summ(clients, name, summ, multiple)
            elif command == 'BALANCE':
                name = operation[1]
                if name in clients:
                    print(clients[name])
                else:
                    print('ERROR')
            elif command == 'TRANSFER':
                name_1 = operation[1]
                name_2 = operation[2]
                summ = int(operation[3])
                change_summ(clients, name_1, summ, multiple=-1)
                change_summ(clients, name_2, summ, multiple=1)
            elif command == 'INCOME':
                percent = int(operation[1])
                for name, bank_account in clients.items():
                    if bank_account > 0:
                        clients[name] += int(bank_account * (percent / 100))
            operation = file_in.readline().strip().split()


if __name__ == '__main__':
    main()
