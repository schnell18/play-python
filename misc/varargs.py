def f(*args, **kwargs):
    print("Positional args:", args)

    for k, v in kwargs.items():
        print(f"{k} => {v}")


if __name__ == "__main__":
    f(1, 2, 3, 5, 6)
    f(1, 2, 3, 5, 6, item=133, qty=10, discount=0.9)
