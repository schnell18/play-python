import instaviz

def fib(n):
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

instaviz.show(fib)

