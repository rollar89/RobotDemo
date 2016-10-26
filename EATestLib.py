from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class EATestLib(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.Username = (By.CSS_SELECTOR, "[#userName > p:nth-child(1) > input:nth-child(1)]")
        self.Password = (By.CSS_SELECTOR, "[#userName > p:nth-child(2) > input:nth-child(1)]")
        self.Login = (By.CSS_SELECTOR, "[#userName > p:nth-child(3) > input:nth-child(1)]")
        self.Title = (By.CSS_SELECTOR, ["#TitleId"])
        self.Inat = (By.CSS_SELECTOR, ["#Initial"])
        self.Firstname = (By.CSS_SELECTOR, ["#FirstName"])
        self.Middlename = (By.CSS_SELECTOR, ["#MiddleName"])
        self.Lastname = (By.CSS_SELECTOR, ["#LastName"])
        self.Gender = (By.CSS_SELECTOR, ["#details > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > input:nth-child(2)"])
        self.Language = (By.CSS_SELECTOR, ["#details > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) > input:nth-child(2)"])
        self.Language2 = (By.CSS_SELECTOR, ["div.detail_box:nth-child(12) > span:nth-child(1) > input:nth-child(2)"])
        self.HTTP_Link = (By.CSS_SELECTOR, ["div.detail_box:nth-child(3) > p:nth-child(2) > a:nth-child(2)"])
        self.country = (By.CSS_SELECTOR, ["#Country"])
        self.Generate_link = (By.CSS_SELECTOR, ["#details > div:nth-child(4) > p:nth-child(1) > input:nth-child(2)"])
    def Auto_login(self):
        # Open the site
        self.driver.get('http://executeautomation.com/demosite/Login.html')

        # Then Login with User credentials
        user = self.driver.find_element(*self.Username)
        user.send_keys('Rola')
        Password = self.driver.find_element(*self.Password)
        Password.send_keys('khalaf')
        Login = self.driver.find_element(*self.Login)
        Login.click()

    def Fill_Data(self):
        # Wait 5S until the content of the webpage displays properly
        time.sleep(5)

        # Then, fill the data form
        selectT = Select(self.driver.find_element(*self.Title))
        selectT.select_by_visible_text('Ms.')
        Initial = self.driver.find_element(*self.Inat)
        Initial.send_keys('1')
        FirstN = self.driver.find_element(*self.Firstname)
        FirstN.send_keys('Rola')
        MiddleN = self.driver.find_element(*self.Middlename)
        MiddleN.send_keys('Khalaf')
        selectF = self.driver.find_element(*self.Gender)
        selectF.click()
        selectH = self.driver.find_element (*self.Language)
        selectH.click()

    def HTML_Popup (self):
        # Navigate to HTTP Popup
        HTML_P = self.driver.find_element(*self.HTTP_Link)
        HTML_P.click()

        # Wait 5S until the content of the webpage displays properly
        time.sleep(5)

        #   Switch to the new window that has just opened
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.maximize_window()

        # Then, fill the data form
        selectT = Select(self.driver.find_element(*self.Title))
        selectT.select_by_visible_text('Ms.')
        Initial = self.driver.find_element(*self.Inat)
        Initial.send_keys('1')
        FirstN = self.driver.find_element(*self.Firstname)
        FirstN.send_keys('Rola')
        MiddleN = self.driver.find_element(*self.Middlename)
        MiddleN.send_keys('Khalaf')
        LastN = self.driver.find_element(*self.Lastname)
        LastN.send_keys('Shunnaq')
        selectG = self.driver.find_element(*self.Language2)
        selectG.click()
        selectC = Select(*self.country)
        selectC.select_by_visible_text('UK')

        # Close the new window (currently open) and switch to original window
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def Alert_P(self):
        # Navigate to Generate Popup
        generate = self.browser.find_element(*self.Generate_link)
        generate.click()

        # Then Dismiss the Alert
        alert = self.browser.switch_to.alert()
        alert.dismiss()

        #   Close the new window (currently open) and switch to original window
        #self.browser.close()
        #self.browser.switch_to_window(self.browser.window_handles[0])

