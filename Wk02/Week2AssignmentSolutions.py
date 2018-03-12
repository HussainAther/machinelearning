class Rectangle:
    """
    Rectangle for Part A
    """
    def __init__(self, height, width):
        """Initialize a new rectangle object."""
        self.height = height
        self.width = width

    def get_size(self):
        """Return the size of the rectangle."""
        return self.height * self.width

my_rectangle = Rectangle(2, 10)
assert my_rectangle.get_size() == 20
assert Rectangle(10, 10).get_size() == 100
assert Rectangle(10, 30).get_size() == 300
assert Rectangle(28, 2).get_size() == 56
assert Rectangle(10, 10).get_size() == 100

class Pet:
    """
    Pet for Part B
    """
    def __init__(self, name):
        self.name = name
    
    def make_noise(self):
        return self.noise

class Dog(Pet):
    """Initialize the class Dog"""
    noise = "bark"

class Cat(Pet):
    """Initialize the class Cat"""
    noise = "meow"

pet1 = Dog("sherlock")
assert pet1.make_noise() == "bark"
assert pet1.name == "sherlock"

pet2 = Cat("rex")
assert pet2.make_noise() == "meow"
assert pet2.name == "rex"

class Bank:
    """
    Bank class
    """


class BankAccount:
    """
    Bank Account for Part C
    """
    def __init__(self):
        """
        Initialize the class BankAccount
        """
        Bank.__init__(self)
        self.balance = 0

    def deposit(self, amount):
        """
        Deposit money in the bank account.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraw money from the bank account.
        """
        self.balance -= amount

    def check_balance(self):
        """
        Check the current balance in the bank account.
        """
        return self.balance

acc = BankAccount()
acc.deposit(100.0)
acc.deposit(200.0)
acc.withdraw(250.0)
assert acc.check_balance() == 50.0
acc.withdraw(10.0)
acc.deposit(30.0)
assert acc.check_balance() == 70.0
assert len(BankAccount.deposit.__doc__) > 10
assert len(BankAccount.withdraw.__doc__) > 10

class DebitAccount(BankAccount):
    """
    Debit Account for Part D
    """
    def __init__(self):
        """
        Initialize the class DebitAccount
        """
        Bank.__init__(self)
        self.balance = 0

    def deposit(self, amount):
        """
        Deposit money in the debit account.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraw money from the debit account. Cannot go below 0.
        """
        if self.balance - amount < 0:
            return False
        else:
            self.balance -= amount
            return True

    def check_balance(self):
        """
        Check the current balance in the debit account.
        """
        return self.balance

assert issubclass(DebitAccount, BankAccount)

debit = DebitAccount()
debit.deposit(30.0)
debit.deposit(20.0)
assert debit.check_balance() == 50.0
result = debit.withdraw(10.0)
assert debit.check_balance() == 40.0
assert result is True

result = debit.withdraw(90.0)
assert debit.check_balance() == 40.0
assert result is False
