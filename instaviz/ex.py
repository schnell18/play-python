import instaviz

def fn():
    a = 1
    b = a + 1
    return b

#print(fn.__code__.co_filename)
instaviz.show(fn)

