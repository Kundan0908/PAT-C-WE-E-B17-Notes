from hrm_login import User

def test_login_positive():
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    login = User(url)
    output = login._login()
    assert output == True, "Test Failed due to login error"

def test_login_negative():
    url = 'https://google.com'
    login = User(url)
    output = login._login()
    assert output == False, "Test Passed with no errors"