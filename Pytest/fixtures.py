import pytest

@pytest.fixture
def setup():
    print("Launch browser")
    print("Login")
    print("Browser products")
    yield 
    print("Log out")
    print("Close browser")


def test_AddItemtoCart(setup):
    print("Item added successfully..")

def test_RemoveItemtoCart():
    print("Item removed successfully..")