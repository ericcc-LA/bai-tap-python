'''
bai 3 :  Encapsulation (private attributes)
'''


class BankAccount:
    def __init__(self, owner, account_number, initial_balance=0):

        self.__owner = owner
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền nạp phải lớn hơn 0")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền rút phải lớn hơn 0")
            return

        if amount > self.__balance:
            print("Số dư không đủ")
            return
        self.__balance -= amount

    def get_balance(self):

        return self.__balance

    def get_owner(self):
        return self.__owner

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("Số tiền chuyển phải lớn hơn 0")
            return
        if amount > self.__balance:
            print("Số dư không đủ để chuyển")
            return
        self.withdraw(amount)
        other_account.deposit(amount)


if __name__ == "__main__":
    acc1 = BankAccount("Minh", "123456", 1000)
    acc1.deposit(500)
    print(acc1.get_balance())

    acc1.withdraw(200)
    print(acc1.get_balance())

    acc2 = BankAccount("An", "654321", 500)
    acc1.transfer(acc2, 300)
    print(acc1.get_balance())
    print(acc2.get_balance())
