def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


if __name__ == "__main__":
    first, last = input("What's your name? ").split(" ")
    print(f"Hello, {first}")

    coins = [100, 50, 25]
    print(total(*coins), "Knuts")
    coins2 = {"galleons": 100, "sickles": 50, "knuts": 25}
    print(total(galleons=100, sickles=50, knuts=25), "Knuts")
    print(total(**coins2), "Knuts")

