from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
import config
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import yaml
from yaml.loader import SafeLoader
import os
import logging
from datetime import datetime, timedelta
from pathlib import Path


class Config:
    @classmethod
    def read_config(self, section, key):
        with open(r'C:\Users\47790147\PycharmProjects\SSOApplication\lib_folder\config.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data[section][key]


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.logging = logging.basicConfig(filename='SSOApplication_logs.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    def __username_section(self):
        self.driver.find_element(by=By.XPATH, value=Config.read_config('Login', 'login_with_sso_btn')).click()
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config('Login', 'login_username'))))
        except (TimeoutException, NoSuchElementException):
            pass
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config('Login', 'login_username')) \
            .send_keys(Config.read_config('Login', 'username'))
        self.driver.find_element(By.XPATH, Config.read_config('Login', 'signin_1')).click()
        return True

    def __password_section(self):
        wait_ele = WebDriverWait(self.driver, timeout=20)
        wait_ele.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config('Login', 'login_password'))))
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config('Login', 'login_password')) \
            .send_keys(Config.read_config('Login', 'password'))
        self.driver.find_element(By.XPATH, Config.read_config('Login', 'signin_1')).click()
        return True

    def __otp_section(self):
        self.driver.switch_to.default_content()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config('Login', 'otp'))))
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config('Login', 'otp')) \
            .send_keys(input("Enter OTP : "))
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config('Login', 'submit')).click()
        return True

    def login_main(self):
        if self.__username_section() and self.__password_section():
            try:
                if self.__otp_section():
                    return True
            except:
                return False
        return False

class UserManagement:

    def __init__(self, driver):
        self.driver = driver

    def click_user_management_option(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.XPATH, Config.read_config('UserManagement', 'userManagement_btn'))))
            self.driver.find_element(By.XPATH, Config.read_config('UserManagement', 'userManagement_btn')).click()
            return True
        except:
            return False

    def click_create_new_button(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config('UserManagement', 'createnew'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'createnew')).click()
            return True
        except:
            return False

    def fill_user_details(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement', 'emailaddress'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'emailaddress')). \
                send_keys(Config.read_config('UserManagement_InputData', 'emailaddress'))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'username')). \
                send_keys(Config.read_config('UserManagement_InputData', 'username'))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'pwd')). \
                send_keys(Config.read_config('UserManagement_InputData', 'pwd'))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'confirm_pwd')). \
                send_keys(Config.read_config('UserManagement_InputData', 'confirm_pwd'))
            if self.__role_selection() and self.__application_selection():
                self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'firstname')). \
                    send_keys(Config.read_config('UserManagement_InputData', 'firstname'))
                self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'lastname')). \
                    send_keys(Config.read_config('UserManagement_InputData', 'lastname'))
                self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'phonenumber')). \
                    send_keys(Config.read_config('UserManagement_InputData', 'phonenumber'))
                self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'address')). \
                    send_keys(Config.read_config('UserManagement_InputData', 'address'))
                self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'city')). \
                    send_keys(Config.read_config('UserManagement_InputData', 'city'))
                self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'state')). \
                    send_keys(Config.read_config('UserManagement_InputData', 'state'))
                country = Select(
                    self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'country')))
                country.select_by_visible_text(Config.read_config('UserManagement_InputData', 'country'))
                self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'postalcode')). \
                    send_keys(Config.read_config('UserManagement_InputData', 'postalcode'))
                self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'superadmin')).click()
                return True
            return False
        except:
            return False

    def __select_tenant(self):
        try:
            ele = self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'role'))
            ActionChains(self.driver).move_to_element(ele).click().perform()
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement', 'tenant_admin'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'tenant_admin')).click()
            return True
        except:
            return False

    def __role_selection(self):
        try:
            ele = self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'role'))
            ActionChains(self.driver).move_to_element(ele).click().perform()
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement', 'tenant_admin'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'tenant_admin')).click()
            return True
        except:
            return False

    def __role_selection_update(self):
        try:
            ele = self.driver.find_element(By.CSS_SELECTOR,
                                           Config.read_config('UserManagement_Updateuser_Selectors', 'role'))
            ActionChains(self.driver).move_to_element(ele).click().perform()
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement_Updateuser_Selectors', 'customer'))))
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config('UserManagement_Updateuser_Selectors', 'customer')).click()
            return True
        except:
            return False

    def __application_selection_update(self):
        try:
            ele = self.driver.find_element(By.CSS_SELECTOR,
                                           Config.read_config('UserManagement_Updateuser_Selectors', 'application'))
            ActionChains(self.driver).move_to_element(ele).click().perform()
            wait_ele = WebDriverWait(self.driver, timeout=40)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement_Updateuser_Selectors', 'bi_reports'))))
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config('UserManagement_Updateuser_Selectors', 'bi_reports')).click()
            return True
        except:
            return False

    def __application_selection(self):
        try:
            ele = self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'application'))
            ActionChains(self.driver).move_to_element(ele).click().perform()
            wait_ele = WebDriverWait(self.driver, timeout=40)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement', 'bi_dashboard'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'bi_dashboard')).click()
            return True
        except:
            return False

    def click_save_button(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement', 'save')).click()
            return True
        except:
            return False

    def click_update_save_button(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config('UserManagement_Updateuser_Selectors', 'save')).click()
            return True
        except:
            return False

    def user_create_status(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement', 'creation_status'))))
            note = self.driver.find_element(By.CSS_SELECTOR,
                                            Config.read_config('UserManagement', 'creation_status')).text
            if note.__contains__('successful'):
                return True
            else:
                return False
        except:
            return False

    def search_user(self, mode=False, param=None):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement_Actions', 'search_bar'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement_Actions', 'search_bar')). \
                send_keys(param if mode else Config.read_config('UserManagement_InputData', 'emailaddress'))
            return True
        except:
            return False

    def __search_clear(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement_Actions', 'search_bar'))))
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config('UserManagement_Actions', 'search_bar')).clear()
            return True
        except:
            return False

    def edit_user(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20, poll_frequency=5)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement_Actions', 'search_table'))))
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config('UserManagement_Actions', 'search_table')).click()
            return True
        except:
            return False

    def __update_handy(self, field):
        ele = self.driver.find_element(By.CSS_SELECTOR,
                                       Config.read_config('UserManagement_Updateuser_Selectors', field))
        ele.clear()
        ele.send_keys(Config.read_config('UserManagement_UpdateData', field))

    def update_user_details(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement_Updateuser_Selectors', 'emailaddress'))))
            self.__update_handy(field='emailaddress')
            self.__update_handy(field='username')
            if self.__role_selection_update() and self.__application_selection_update():
                self.__update_handy(field='firstname')
                self.__update_handy(field='lastname')
                self.__update_handy(field='phonenumber')
                self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                self.__update_handy(field='address')
                self.__update_handy(field='city')
                self.__update_handy(field='state')
                self.__update_handy(field='postalcode')
                country = Select(self.driver.find_element(By.CSS_SELECTOR,
                                                          Config.read_config('UserManagement_Updateuser_Selectors',
                                                                             'country')))
                country.select_by_visible_text(Config.read_config('UserManagement_UpdateData', 'country'))
                chkbox = self.driver.find_element(By.CSS_SELECTOR,
                                                  Config.read_config('UserManagement_Updateuser_Selectors',
                                                                     'superadmin'))
                if chkbox.is_selected():
                    chkbox.click()
                chkbox.click()
                return True
            return False
        except:
            return False

    def __user_settings(self, mode=False, param=None):
        try:
            self.__search_clear()
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('UserManagement_Actions', 'search_bar'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('UserManagement_Actions', 'search_bar')). \
                send_keys(param if mode else Config.read_config('UserManagement_InputData', 'emailaddress'))
            time.sleep(5)
            wait_ele = WebDriverWait(self.driver, timeout=30)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config("UserManagement_Actions", "extract_email"))))
            email_txt = self.driver.find_element(By.CSS_SELECTOR,
                                                 Config.read_config("UserManagement_Actions", "extract_email")).text
            if email_txt and email_txt != '':
                self.driver.find_element(By.CSS_SELECTOR,
                                         Config.read_config('UserManagement_Actions', 'user_settings')).click()
                return email_txt
            return False
        except:
            return False

    def validate_settings_modal_tab(self, mode=False, param=None):
        try:
            table_email_id = self.__user_settings(mode, param)
            wait_ele = WebDriverWait(self.driver, timeout=30)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config("UserManagement_Actions", "tab_header"))))
            email_txt = self.driver.find_element(By.CSS_SELECTOR,
                                                 Config.read_config("UserManagement_Actions", "tab_header")).text
            if email_txt.strip().lower().__contains__(table_email_id.strip().lower()):
                return True
            return False
        except:
            return False

    def __close_modal_tab(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=30)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config("UserManagement_Actions", "modal_close_btn"))))
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config("UserManagement_Actions", "modal_close_btn")).click()
            return True
        except:
            return False

    def deactivate_user(self):
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located(
            (By.XPATH, Config.read_config("UserManagement_Actions", "deactivate_user"))))
        self.driver.find_element(By.XPATH, Config.read_config("UserManagement_Actions", "deactivate_user")).click()
        time.sleep(10)
        self.driver.refresh()
        self.search_user()
        try:
            wait_ele = WebDriverWait(self.driver, timeout=30)
            wait_ele.until(EC.visibility_of_element_located(
                (By.XPATH, Config.read_config("UserManagement_Actions", "disabled_status"))))
            if self.driver.find_element(By.XPATH, Config.read_config("UserManagement_Actions",
                                                                     "disabled_status")).text == 'Disabled':
                return True
            return False
        except:
            return False

    def activate_user(self):
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located(
            (By.XPATH, Config.read_config("UserManagement_Actions", "activate_user"))))
        self.driver.find_element(By.XPATH, Config.read_config("UserManagement_Actions", "activate_user")).click()
        try:
            self.driver.refresh()
            time.sleep(10)
            if self.__search_clear() and self.search_user():
                wait_ele = WebDriverWait(self.driver, timeout=30)
                wait_ele.until(EC.visibility_of_element_located(
                    (By.XPATH, Config.read_config("UserManagement_Actions", "enabled_status"))))
                enabled_txt = self.driver.find_element(By.XPATH, Config.read_config("UserManagement_Actions",
                                                                                    "enabled_status")).text
                if enabled_txt.__contains__('Active'):
                    return True
            return False
        except:
            return False

    def __enableTFA(self):
        if self.__search_clear():
            time.sleep(2)
            if self.__validate_settings_modal_tab():
                wait_ele = WebDriverWait(self.driver, timeout=30)
                wait_ele.until(EC.visibility_of_element_located(
                    (By.XPATH, Config.read_config("UserManagement_Actions", "enable_tfa"))))
                self.driver.find_element(By.XPATH,
                                         Config.read_config("UserManagement_Actions", "enable_tfa")).click()
                # try:
                #     wait_ele = WebDriverWait(self.driver, timeout=30)
                #     wait_ele.until(EC.visibility_of_element_located(
                #         (By.XPATH, Config.read_config("UserManagement_Actions", "enabled_status"))))
                #     if self.driver.find_element(By.XPATH, Config.read_config("UserManagement_Actions",
                #                                                              "enabled_status")).text == 'Active':
                #         return True
                #     return False
                # except:
                #     return False
        return False

    def __resetTFA(self):
        if self.__search_clear():
            self.__search_user()
            if self.__validate_settings_modal_tab():
                wait_ele = WebDriverWait(self.driver, timeout=30)
                wait_ele.until(EC.visibility_of_element_located(
                    (By.XPATH, Config.read_config("UserManagement_Actions", "reset_tfa"))))
                self.driver.find_element(By.XPATH,
                                         Config.read_config("UserManagement_Actions", "reset_tfa")).click()
                # try:
                #     wait_ele = WebDriverWait(self.driver, timeout=30)
                #     wait_ele.until(EC.visibility_of_element_located(
                #         (By.XPATH, Config.read_config("UserManagement_Actions", "enabled_status"))))
                #     if self.driver.find_element(By.XPATH, Config.read_config("UserManagement_Actions",
                #                                                              "enabled_status")).text == 'Active':
                #         return True
                #     return False
                # except:
                #     return False
        return False

    def __resetPWD(self):
        time.sleep(3)
        if self.__search_clear():
            time.sleep(3)
            self.__search_user()
            if self.__validate_settings_modal_tab():
                try:
                    wait_ele = WebDriverWait(self.driver, timeout=30)
                    wait_ele.until(EC.visibility_of_element_located(
                        (By.XPATH, Config.read_config("UserManagement_Actions", "reset_pwd"))))
                    self.driver.find_element(By.XPATH,
                                             Config.read_config("UserManagement_Actions", "reset_pwd")).click()
                    wait_ele = WebDriverWait(self.driver, timeout=30)
                    wait_ele.until(EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, Config.read_config("UserManagement_Actions", "error_page"))))
                    error_msg = self.driver.find_element(By.CSS_SELECTOR, Config.read_config("UserManagement_Actions",
                                                                                             "error_page")).text
                    if error_msg.lower().__contains__('error'): return False
                    return True
                except (NoSuchElementException, TimeoutException, TimeoutError):
                    return False
        return False

    def deleteUser(self, mode=False, param=None):
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(
            EC.visibility_of_element_located((By.XPATH, Config.read_config("UserManagement_Actions", "delete_user"))))
        self.driver.find_element(By.XPATH, Config.read_config("UserManagement_Actions", "delete_user")).click()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, Config.read_config("UserManagement_Actions", "delete_msg"))))
        delete_msg = self.driver.find_element(By.CSS_SELECTOR,
                                              Config.read_config("UserManagement_Actions", "delete_msg")).text
        if delete_msg.__contains__("delete"):
            time.sleep(20)
            self.driver.refresh()
            if self.__search_clear() and self.search_user(mode, param):
                wait_ele = WebDriverWait(self.driver, timeout=30)
                wait_ele.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, Config.read_config("UserManagement_Actions", "no_records_msg"))))
                try:
                    time.sleep(5)
                    self.driver.find_element(By.CSS_SELECTOR,
                                             Config.read_config("UserManagement_Actions", "no_records_msg"))
                    return True
                except (TimeoutException, NoSuchElementException, TimeoutError):
                    return False
            else:
                return False
        return False

    def delete_cdc_user(self, email):
        # if self.__search_clear() and self.search_user(mode=True, param=email):
        if self.search_user(mode=True, param=email):
            if self.validate_settings_modal_tab(mode=True, param=email):
                return self.deleteUser(mode=True, param=email)

    def __number_of_records(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config("UM_Refresh_Option",
                                                                                             "number_of_records"))))

        record = self.driver.find_element(By.CSS_SELECTOR, Config.read_config("UM_Refresh_Option",
                                                                              "number_of_records")).text
        return record

    def refresh(self):
        if self.__search_clear():
            time.sleep(3)
            self.driver.refresh()
            record = self.__number_of_records()
            self.driver.refresh()
            wait_ele = WebDriverWait(self.driver, timeout=30)
            wait_ele.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config("UM_Refresh_Option",
                                                                                                 "refresh_btn"))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config("UM_Refresh_Option", "refresh_btn")).click()
            time.sleep(3)
            record1 = self.__number_of_records()
            self.driver.refresh()
            time.sleep(3)
            if record == record1:
                return True
            else:
                False

    def toggle(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config("UM_Toggle_Option",
                                                                                             "toggle_btn"))))
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config("UM_Toggle_Option", "toggle_btn")).click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config("UM_Toggle_Option", "toggle_check_btn")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def sort_Email_Address(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("UM_Sorting_Fields",
                                                                                             "sort_email_address"))))
        self.driver.find_element(By.XPATH, Config.read_config("UM_Sorting_Fields", "sort_email_address")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def sort_First_Name(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("UM_Sorting_Fields",
                                                                                             "sort_first_name"))))
        self.driver.find_element(By.XPATH, Config.read_config("UM_Sorting_Fields", "sort_first_name")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def sort_Last_Name(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("UM_Sorting_Fields",
                                                                                             "sort_last_name"))))
        self.driver.find_element(By.XPATH, Config.read_config("UM_Sorting_Fields", "sort_last_name")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def sort_Status(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("UM_Sorting_Fields",
                                                                                             "sort_status"))))
        self.driver.find_element(By.XPATH, Config.read_config("UM_Sorting_Fields", "sort_status")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def sort_Verified_Status(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("UM_Sorting_Fields",
                                                                                             "sort_verified_status"))))
        self.driver.find_element(By.XPATH, Config.read_config("UM_Sorting_Fields", "sort_verified_status")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def __plus_btn_data(self, locator):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=15)
            wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("UM_Plus_Option",
                                                                                          locator))))
            data = self.driver.find_element(By.XPATH, Config.read_config("UM_Plus_Option", locator)).text
            if data is not None:
                return True
            else:
                return False
        except:
            return False

    def plus_btn(self):
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config("UM_Plus_Option",
                                                                                      "plus_option_btn"))))
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config("UM_Plus_Option", "plus_option_btn")).click()
        time.sleep(3)
        if self.__plus_btn_data("tenant_data"):
            if self.__plus_btn_data("role_data"):
                if self.__plus_btn_data("application_data"):
                    return True
        else:
            return False


class InvitationManagement:

    def __init__(self, driver):
        self.driver = driver

    def __select_tenant(self):
        try:
            time.sleep(5)
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'select_tenant'))))
            ele = self.driver.find_element(By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'select_tenant'))
            ActionChains(self.driver).move_to_element(ele).click().perform()
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'select_tenant_name'))))
            tenant_val = self.driver.find_element(By.CSS_SELECTOR,
                                                  Config.read_config('InvitationManagement', 'select_tenant_name')).text
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config('InvitationManagement', 'select_tenant_name')).click()
            return tenant_val
        except:
            return False

    def __role_selection(self):
        try:
            ele = self.driver.find_element(By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'select_role'))
            ActionChains(self.driver).move_to_element(ele).click().perform()
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'select_rolename'))))
            role_val = self.driver.find_element(By.CSS_SELECTOR,
                                                Config.read_config('InvitationManagement', 'select_rolename')).text
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config('InvitationManagement', 'select_rolename')).click()
            return role_val
        except:
            return False

    def __application_selection(self):
        try:
            ele = self.driver.find_element(By.CSS_SELECTOR,
                                           Config.read_config('InvitationManagement', 'select_application'))
            ActionChains(self.driver).move_to_element(ele).click().perform()
            wait_ele = WebDriverWait(self.driver, timeout=40)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'select_applicationname'))))
            app_val = self.driver.find_element(By.CSS_SELECTOR, Config.read_config('InvitationManagement',
                                                                                   'select_applicationname')).text
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config('InvitationManagement', 'select_applicationname')).click()
            ActionChains(self.driver).move_to_element(ele).click().perform()
            return app_val
        except:
            return False

    def __click_tenant_add_button(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=30)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config("InvitationManagement", "add_tenant_btn"))))
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config("InvitationManagement", "add_tenant_btn")).click()
            return True
        except:
            return False

    def click_save_button(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'save')).click()
            return True
        except:
            return False

    def click_Invitation_management_option(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.XPATH, Config.read_config('InvitationManagement', 'InvitationManagement_btn'))))
            self.driver.find_element(By.XPATH,
                                     Config.read_config('InvitationManagement', 'InvitationManagement_btn')).click()
            return True
        except:
            return False

    def click_invite_user_button(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'createnew'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'createnew')).click()
            return True
        except:
            return False

    def __fill_tenant_details(self):
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config("InvitationManagement", "addtenant")).click()
        tenent_val = self.__select_tenant()
        role_val = self.__role_selection()
        time.sleep(5)
        app_val = self.__application_selection()
        if self.__click_tenant_add_button():
            return tenent_val, role_val, app_val
        else:
            return False

    def fill_user_details(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'emailaddress'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'emailaddress')). \
                send_keys(Config.read_config('InvitationManagement_InputData', 'emailaddress'))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'firstname')). \
                send_keys(Config.read_config('UserManagement_InputData', 'firstname'))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'lastname')). \
                send_keys(Config.read_config('InvitationManagement_InputData', 'lastname'))
            return self.__cross_verify_tenant_details()
        except:
            return False

    def __cross_verify_tenant_details(self):
        tenent_val, role_val, app_val = self.__fill_tenant_details()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, Config.read_config("InvitationManagement", "card_title"))))
        card_title = self.driver.find_element(By.CSS_SELECTOR,
                                              Config.read_config("InvitationManagement", "card_title")).text
        role_selected = self.driver.find_element(By.CSS_SELECTOR,
                                                 Config.read_config("InvitationManagement", "role_selected")).text
        app_selected = self.driver.find_element(By.CSS_SELECTOR,
                                                Config.read_config("InvitationManagement", "application_selected")).text
        if tenent_val.lower() == card_title.lower() and role_val.lower() == role_selected.lower() and app_val.lower() == app_selected.lower():
            return True
        else:
            return False

    def user_create_status(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'inviteuserstatus'))))
            note = self.driver.find_element(By.CSS_SELECTOR,
                                            Config.read_config('InvitationManagement', 'inviteuserstatus')).text
            if note.__contains__('successful'):
                return True
            else:
                return False
        except:
            return False

    def __validate_template_file(self):
        downloads_path = str(Path.home() / Config.read_config('InvitationManagement', 'download_filepath'))
        template_filepath = downloads_path + "\\" + Config.read_config('InvitationManagement',
                                                                       'download_template_filename')
        c_time = os.path.getctime(template_filepath)
        file_createdTime = datetime.fromtimestamp(c_time)
        currentTime = datetime.today() - timedelta(minutes=5)
        if file_createdTime >= currentTime:
            return template_filepath

    def download_template(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'download_template'))))
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config('InvitationManagement', 'download_template')).click()
            time.sleep(5)
            template_filepath = self.__validate_template_file()
            if template_filepath is not None:
                os.remove(template_filepath)
                return True
        except:
            return False

    def upload_template(self):
        upload_temp = WebDriverWait(self.driver, timeout=20)
        upload_temp.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'upload_template'))))
        self.driver.find_element(By.CSS_SELECTOR,
                                 Config.read_config('InvitationManagement', 'upload_template')).click()
        time.sleep(5)
        upload_template_file = Config.read_config('InvitationManagement', 'upload_file')
        path = os.getcwd().replace("\\SSOApplication\\lib_folder", "\\SSOApplication")
        upload_template_filepath = path+"\\"+upload_template_file
        if upload_template_filepath is not None:
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config('InvitationManagement', 'choose_file')). \
                send_keys(upload_template_filepath)

            upload_file = WebDriverWait(self.driver, timeout=30)
            upload_file.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'upload_file_submit'))))
            self.driver.find_element(By.CSS_SELECTOR,
                                     Config.read_config('InvitationManagement', 'upload_file_submit')).click()

            file_status = WebDriverWait(self.driver, timeout=20)
            file_status.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'upload_file_status'))))
            note = self.driver.find_element(By.CSS_SELECTOR,
                                            Config.read_config('InvitationManagement', 'upload_file_status')).text

            os.remove(upload_template_filepath)  # Delete the template file from the local system

            if note.__contains__('successful'):
                return True
            else:
                error_msg = self.driver.find_element(By.CSS_SELECTOR,
                                                     Config.read_config('InvitationManagement',
                                                                        'upload_file_error_status')).text

                return False
        else:
            return False

    def __search_user(self):
        try:
            search = WebDriverWait(self.driver, timeout=20)
            search.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'search_bar'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'search_bar')). \
                send_keys(Config.read_config('InvitationManagement_InputData', 'delete_mail_id'))
            return True
        except:
            return False

    def delete_user(self):
        try:
            if self.__search_user():
                # wait = WebDriverWait(self.driver, timeout=20, poll_frequency=5)
                # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config('InvitationManagement', 'search_table'))))
                time.sleep(5)
                self.driver.find_element(By.CSS_SELECTOR,
                                         Config.read_config('InvitationManagement', 'search_table')).click()
                # wait = WebDriverWait(self.driver, timeout=20, poll_frequency=5)
                # wait.until(EC.visibility_of_element_located(EC.visibility_of_element_located((By.CSS_SELECTOR,
                #                          Config.read_config('InvitationManagement', 'delete_btn')))))
                time.sleep(5)
                self.driver.find_element(By.CSS_SELECTOR,
                                         Config.read_config('InvitationManagement', 'delete_btn')).click()
                return True
            else:
                return False
        except:
            return False


    def __number_of_records(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config("IM_Refresh_Option",
                                                                                             "number_of_records"))))

        record = self.driver.find_element(By.CSS_SELECTOR, Config.read_config("IM_Refresh_Option",
                                                                              "number_of_records")).text
        return record

    def refresh(self):
        time.sleep(3)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config("IM_Refresh_Option",
                                                                                             "refresh_btn"))))
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config("IM_Refresh_Option", "refresh_btn")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            False

    def toggle(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config("IM_Toggle_Option",
                                                                                             "toggle_btn"))))
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config("IM_Toggle_Option", "toggle_btn")).click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config("IM_Toggle_Option", "toggle_check_btn")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def sort_Email_Address(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("IM_Sorting_Fields",
                                                                                      "sort_email_address"))))
        self.driver.find_element(By.XPATH, Config.read_config("IM_Sorting_Fields", "sort_email_address")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def sort_Tenants(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("IM_Sorting_Fields",
                                                                                      "sort_tenants"))))
        self.driver.find_element(By.XPATH, Config.read_config("IM_Sorting_Fields", "sort_tenants")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def sort_Invited_date(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("IM_Sorting_Fields",
                                                                                      "sort_invited_date"))))
        self.driver.find_element(By.XPATH, Config.read_config("IM_Sorting_Fields", "sort_invited_date")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def sort_Invitation_expiry(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("IM_Sorting_Fields",
                                                                                      "sort_invitation_expiry"))))
        self.driver.find_element(By.XPATH, Config.read_config("IM_Sorting_Fields", "sort_invitation_expiry")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def sort_Invitation_status(self):
        time.sleep(5)
        record = self.__number_of_records()
        self.driver.refresh()
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("IM_Sorting_Fields",
                                                                                      "sort_invitation_status"))))
        self.driver.find_element(By.XPATH, Config.read_config("IM_Sorting_Fields", "sort_invitation_status")).click()
        time.sleep(3)
        record1 = self.__number_of_records()
        self.driver.refresh()
        time.sleep(3)
        if record == record1:
            return True
        else:
            return False

    def __plus_btn_data(self, locator):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=15)
            wait_ele.until(EC.visibility_of_element_located((By.XPATH, Config.read_config("IM_Plus_Option",
                                                                                          locator))))
            data = self.driver.find_element(By.XPATH, Config.read_config("IM_Plus_Option", locator)).text
            if data is not None:
                return True
            else:
                return False
        except:
            return False

    def plus_btn(self):
        wait_ele = WebDriverWait(self.driver, timeout=30)
        wait_ele.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Config.read_config("IM_Plus_Option",
                                                                                             "plus_option_btn"))))
        self.driver.find_element(By.CSS_SELECTOR, Config.read_config("IM_Plus_Option", "plus_option_btn")).click()
        time.sleep(3)
        if self.__plus_btn_data("tenant_data"):
            if self.__plus_btn_data("role_data"):
                if self.__plus_btn_data("application_data"):
                    return True
        else:
            return False

class Log_viewer:

    def __init__(self, driver):
        self.driver = driver

    def __click_log_viewer_button(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('Log_viewer', 'log_viewer_btn'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('Log_viewer', 'log_viewer_btn')).click()
            logging.info("Clicked on Log Viewer")
            return True

        except:
            return False

    def __validate_template_file(self):
        downloads_path = str(Path.home() / Config.read_config('Log_viewer', 'download_filepath'))
        log_filepath = downloads_path + "\\" + Config.read_config('Log_viewer', 'log_filename')

        x = datetime.now()
        date = str(x.strftime("%Y")) + "-" + str(x.strftime("%m")) + "-" + str(x.strftime("%d"))
        filepath = log_filepath + date + ".log"
        return filepath

    def __download_log(self):
        try:
            wait_ele = WebDriverWait(self.driver, timeout=20)
            wait_ele.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Config.read_config('Log_viewer', 'download_log'))))
            self.driver.find_element(By.CSS_SELECTOR, Config.read_config('Log_viewer', 'download_log')).click()
            time.sleep(10)
            # filepath = Config.read_config('Log_viewer', 'log_filename')
            filename = self.__validate_template_file()
            isfile = os.path.isfile(filename)
            if isfile is True:
                os.remove(filename)
                return True
            else:
                return False
        except:
            return False

    def log_viewer(self):
        try:
            if self.__click_log_viewer_button():
                if self.__download_log():
                    return True
                else:
                    False
        except:
            return False
