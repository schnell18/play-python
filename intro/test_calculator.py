import pytest
from calculator import square

def main():
    test_square()

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_possitive():
    assert square(2) == 4
    assert square(3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

#     # assert square(3) == 9

# def test_square():
#     # assert square(2) == 4
#     # assert square(3) == 9
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")

if __name__ == "__main__":
    main()
