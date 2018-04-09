class BankAccount:
    """ Class that handles bank account operations """
    def __init__(self):
        """ Initial balance is zero """
        self.balance = 0.0
    
    def deposit(self, amount):
        """ Deposit amount to account """
        self.balance += amount
    
    def withdraw(self, amount):
        """ Withdraws amount from account """
        self.balance -= amount
    
    def check_balance(self):
        """ Returns current balance on account """
        return self.balance


class DebitAccount(BankAccount):
    """ Class that handles debit account operations """
    def withdraw(self, amount):
        """ Withdraws amount from account only if there are sufficient funds """
        if self.balance - amount < 0.0:
            return False

        self.balance -= amount
        return True

class SSNException(Exception):
    """Check for exceptions in the social security number"""
    def __init__(self, m):
        """Initialize the class Exception"""
        self.message = m
    def __str__(self):
        """Return the message"""
        return self.message

def verify_ssn(SSN):
    """Verify if the SSN is valid"""
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    if len(SSN) != 11:
        raise SSNException("Not a valid SSN")
    if SSN[0] not in numbers or SSN[1] not in numbers or SSN[2] not in numbers or SSN[4] not in numbers or SSN[5] not in numbers or SSN[7] not in numbers or SSN[8] not in numbers or SSN[9] not in numbers or SSN[10] not in numbers or SSN[3]!="-" or SSN[6]!="-":
        raise SSNException("Not a valid SSN")
    return

class Client:
    """Describe a client's personal information"""
    def __init__(self, name, ssn):
        """Initialize the class Client with name and SSN"""
        self.__name = name
        self.__ssn = ssn
        verify_ssn(ssn)

class BankClient(Client):
    """Describes the bank of a client"""
    def __init__(self, name, ssn):
        """Initialize the class BankClient"""
        self.organization = "Bank of Bethesda"
        self.__name = name
        self.__ssn = ssn
        verify_ssn(ssn)

    def add_accounts(self, accounts):
        """Assign bank accounts to bank client"""
        self.accounts = accounts
    def check_balance__(self):
        """Return the sum of all balances from the account"""
        return sum(self.balance)
