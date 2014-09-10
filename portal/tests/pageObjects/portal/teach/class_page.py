from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from teach_base_page import TeachBasePage

class TeachClassPage(TeachBasePage):
    def __init__(self, browser):
        super(TeachClassPage, self).__init__(browser)

        assert self.onCorrectPage('teach_class_page')

    def goToClassSettingsPage(self):
        self.browser.find_element_by_id('class_settings_button').click()
        return class_settings_page.TeachClassSettingsPage(self.browser)

    def deleteClass(self):
        self.browser.find_element_by_id('deleteClass').click()
        return self

    def cancelDelete(self):
        self.browser.find_element_by_xpath("//div[contains(@class,'ui-dialog')]//span[contains(text(),'Cancel')]").click()
        return self

    def confirmDelete(self):
        self.browser.find_element_by_xpath("//div[contains(@class,'ui-dialog')]//span[contains(text(),'Confirm')]").click()
        if self.onCorrectPage('teach_classes_page'):
            return classes_page.TeachClassesPage(self.browser)
        else:
            return self

    def isDeleteConfirmShowing(self):
        return self.browser.find_element_by_xpath("//div[contains(@class,'ui-dialog')]").is_displayed()

    def have_students(self):
        return self.elementExistsById('student_table')

    def does_student_exist(self, name):
        try:
            self.browser.find_element_by_xpath("//table[@id='student_table']//a[contains(text(),'{0}')]".format(name))
            return True
        except NoSuchElementException:
            return False
        return self.elementExistsByXPATH('student_table')

import classes_page
import class_settings_page
