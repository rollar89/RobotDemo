from selenium import webdriver


class Extendedlib(object):

    #   Switch to the new window that has just opened
    @staticmethod
    def switch_to_new_window(driver):
        driver.switch_to_window(driver.window_handles[-1])

    #   Close the new window (currently open) and switch to original window
    @staticmethod
    def close_and_switch_to_original_window(driver):
        driver.close()
        driver.switch_to_window(driver.window_handles[0])




