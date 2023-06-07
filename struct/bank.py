balance = 0


class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amt):
        self._balance += amt

    def withdraw(self, amt):
        self._balance -= amt

    def __str__(self):
        return f"balance={self._balance}"


def deposit(amt):
    global balance
    balance = balance + amt


def withdraw(amt):
    global balance
    balance = balance - amt


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)
    acct = Account()
    print(f"{acct}")
    acct.deposit(100)
    print(f"{acct}")


if __name__ == "__main__":
    main()
