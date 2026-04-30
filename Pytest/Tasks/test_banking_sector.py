import pytest
from banking_sector import transfer, TransferError

def  test_valid_transfer():
    from_account="9632580147"
    to_account="7894561230"
    amount=1000
    balance=5000

    assert transfer(from_account,to_account,amount,balance) ==True

def  test_invalid_amount():
    from_account="9632580147"
    to_account="7894561230"
    amount=0
    balance=5000

    with pytest.raises(TransferError, match="Amount must be greater than 0 and amount must be less than balance"):
        transfer(from_account,to_account,amount,balance)


def  test_invalid_accountnumber():
    from_account="96325801475"
    to_account="7894561230"
    amount=100
    balance=5000

    with pytest.raises(TransferError, match="Sender Account number must contain 10 digits"):
        transfer(from_account,to_account,amount,balance)


def  test_invalid_balance():
    from_account="9632580147"
    to_account="7894561230"
    amount=100
    balance=0

    with pytest.raises(TransferError, match="Amount must be greater than 0 and amount must be less than balance"):
        transfer(from_account,to_account,amount,balance)