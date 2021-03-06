import pytest

from pageObjects.Login import Loginpage
@pytest.mark.usefixtures("setup")
class Test_001_login:
    BaseURL = "https://admin-demo.nopcommerce.com/login?"
    username="admin@yourstore.com"
    password="admin"

    def test_homepagetitle(self,setup):
        self.driver =setup
        self.driver.get(self.BaseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpasswordvalue(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False







