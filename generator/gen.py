import cProfile

cProfile.run('sum((i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0))')
cProfile.run('sum([i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0])')

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

val = countdown(10)
next(val)
next(val)
next(val)
next(val)
next(val)
next(val)
next(val)
next(val)
next(val)
next(val)
next(val)
