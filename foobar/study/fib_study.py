def func(num):
    index = 0
    queue = [num]
    while True:
        value = queue[index]
        if value >= 2:
            queue.pop(index)
            queue.append(value - 1)
            queue.append(value - 2)
        else:
            if index == len(queue) - 1:
                break
            index += 1
    return len(queue)


def fibRec(n):
    if n < 2:
        return n
    else:
        return fibRec(n-1) + fibRec(n-2)


def fibIter(n):
    if n < 2:
        return n
    fibPrev = 1
    fib = 1
    for num in range(2, n):
        fibPrev, fib = fib, fib + fibPrev
    return fib


# generative
def fib_gene(n):
    front, rear = 1, 1
    while n > 0:
        yield front
        front, rear, n = rear, front + rear, n - 1


# iterative
def fib_iter(n):
    if n < 2:
        return 1
    fib_prev = 1
    fib = 1
    for x in range(2, n):
        fib_prev, fib = fib, fib_prev + fib
    return fib


print([x for x in fib_gene(6)])


print(fib_iter(7))