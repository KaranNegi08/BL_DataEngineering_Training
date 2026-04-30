import re

class TransferError(Exception):
    pass

def valid_account(from_account):
    return re.match(r'\d{10}$', from_account)


def transfer(from_account, to_account, amount, balance):
    if not valid_account(from_account):
        raise TransferError("Sender Account number must contain 10 digits")

    if not valid_account(to_account):
        raise TransferError("Receiver Account number must contain 10 digits")

    if amount <= 0 or amount > balance:
        raise TransferError("Amount must be greater than 0 and amount must be less than balance")

    return True