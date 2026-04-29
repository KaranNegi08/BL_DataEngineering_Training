import pytest

def test_Login():
    print("Login successfull..")

@pytest.mark.regression
def test_Logoff():
    print("Log off successfull")

# @pytest.mark.skip(reason=None)
@pytest.mark.sanity
def test_Calculation():
    assert  10 in [20,50,4,10]

@pytest.mark.sanity
def test_greet():
    print("Hello Sir...")

