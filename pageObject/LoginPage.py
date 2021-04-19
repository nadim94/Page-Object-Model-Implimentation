class LoginPage():
    # All Locator Define or element Identification
    textbox_email_id = "Email"
    textbox_pass_id = "Password"
    login_button_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
    logout_link_xpath = "/html/body/div[3]/div[1]/div/div/ul/li[3]/a"

    # Action Define
    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_pass_id).clear()
        self.driver.find_element_by_id(self.textbox_pass_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_id(self.logout_link_xpath).click()



