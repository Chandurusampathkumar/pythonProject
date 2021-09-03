from selenium import webdriver

class Loginpage:
    textbox_username_name ="Email"
    textbox_password_name = "Password"
    button_login_xpath="//button[@class='button-1 login-button']"
    link_logout_linktext ="logout"

    def __init__(self,driver):
        self.driver = driver

    def setusername(self,username):
        self.driver.find_element_by_name(self.textbox_username_name).clear()
        self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)

    def setpasswordvalue(self,password):
        self.driver.find_element_by_name(self.textbox_password_name).clear()
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()