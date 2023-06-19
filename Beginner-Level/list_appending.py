if __name__ == '__main__':
    # How many instructions
    N = int(input())

    # empty list
    data = []

    # order
    for _ in range(N):
        command = input().split()
        order, *num = command

        # according to order
        if order == "append":
            data.append(int(num[0]))
        if order == "pop":
            if len(num) == 0:
                data.pop()
            else:
                data.pop(int(num[0]))
        if order == "sort":
            data.sort()
        if order == "remove":
            data.remove(int(num[0]))
        if order == "insert":
            data.insert(int(num[0]), int(num[1]))
        if order == "reverse":
            data.reverse()
        if order == "print":
            print(data)
