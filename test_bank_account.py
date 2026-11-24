import pytest
from bank_account import Account

@pytest.fixture(autouse=True)
def reset():
    Account.existing.clear()

@pytest.fixture
def account():
    account=Account("001","Jarifa",500)
    return account


def test_1_valid_account_create():
    account=Account("001","Jarifa",500)
    assert account.acc_num=="001"
    assert account.name=="Jarifa"
    assert account.balance==500

def test_2_account_without_acc_num():
    with pytest.raises(TypeError):
        Account(name="Jarifa", balance=1000)

def test_3_account_without_name():
    with pytest.raises(TypeError):
        Account(acc_num="001", balance=1000)

def test_4_account_without_balance():
    with pytest.raises(TypeError):
            
        Account(acc_num="001", name="Jarifa")

def test_5_account_with_empty_acc_num():
    with pytest.raises(ValueError):
        Account("", "Jarifa", 1000)

def test_6_account_with_empty_name():
    with pytest.raises(ValueError):
        Account("001", "", 1000)

def test_7_account_with_negative_balance():
    with pytest.raises(ValueError):
        Account("001", "Jarifa", -1000)

def test_8_account_with_zero_balance():  
    with pytest.raises(ValueError):
        Account("001", "Jarifa", 0)

@pytest.mark.parametrize("amount, expected_balance", [(500, 1000),(100.50, 600.50),(1, 501),(0.5,500.5)])
def test_9_valid_deposit(account, amount, expected_balance):
    account.deposit(amount)

    assert account.balance == pytest.approx(expected_balance)

@pytest.mark.parametrize("amount", [-100,-50,0,-1.4])
def test_10_invalid_deposit(account, amount):
    with pytest.raises(ValueError):
        account.deposit(amount)
    assert account.balance == 500

@pytest.mark.parametrize("amount, expected_balance", [(100, 400),(50.50, 449.50),(1, 499),(0.5,499.5)])
def test_11_valid_withdraw(account, amount, expected_balance):
    account.withdraw(amount)
    assert account.balance==pytest.approx(expected_balance)

@pytest.mark.parametrize("amount", [-100,-50,0,-1.4])
def test_12_invalid_withdraw(account, amount):
    with pytest.raises(ValueError):
        account.withdraw(amount)
    assert account.balance==500

def test_13_withdraw_more_than_balance(account):
    account.withdraw(600)
    assert account.balance==500

def test_14_check_balance(account):
    assert account.check_balance()==500

def test_15_check_balance_after_deposit(account):
    account.deposit(200)
    assert account.check_balance()==700

def test_16_check_balance_after_withdraw(account):
    account.withdraw(200)
    assert account.check_balance()==300

def test_17_display_account(account):
    account.display()
    assert account.acc_num=="001"
    assert account.name=="Jarifa"
    assert account.balance==500


def test_18_duplicate_account_with_existing_number():
    Account("1234", "Jarifa", 1000)
    with pytest.raises(ValueError, match="Account already exists"):
        Account("1234", "Rahim", 2000)

def test_19_create_exact_duplicate():
    Account("1234", "Jarifa", 1000)
    with pytest.raises(ValueError, match="Account already exists"):
        Account("1234", "Jarifa", 1000)

def test_20_create_unique_account(capsys):
    acc1 = Account("1234", "Jarifa", 1000)
    acc2 = Account("5678", "Rahim", 2000)
    captured = capsys.readouterr()
    assert acc1.acc_num != acc2.acc_num
    assert "Account created successfully." in captured.out