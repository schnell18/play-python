from hello import hello

def test_argument():
    assert hello("world") == "Hello, world"

def test_default():
    assert hello() == "Hello, world"
