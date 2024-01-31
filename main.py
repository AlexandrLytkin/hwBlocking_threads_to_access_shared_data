import threading


class BankAccount:

    def __init__(self, amount=1_000):
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount -= amount


def deposit_task(account, amount):
    for _ in range(5):
        with threading.Lock():
            account.deposit(amount)
            print(f'Deposited {amount}, new balance is {account.amount}')


def withdraw_task(account, amount):
    for _ in range(5):
        with threading.Lock():
            account.withdraw(amount)
            print(f'Withdrew {amount}, new balance is {account.amount}')


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
