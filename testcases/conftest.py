import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import os, sys
conf_path = os.getcwd()
sys.path.append(conf_path)
sys.path.append(conf_path.replace(r'\testcases', '') + r'\lib_folder')
from lib_folder.login_page import Login, UserManagement, InvitationManagement, Log_viewer

@pytest.fixture(scope="session")
def setup():
    options = Options()
    options.headless = True
    # driver = webdriver.Chrome(executable_path=r'C:\Users\47790147\PycharmProjects\SSOApplication\chromedriver.exe')
    driver = webdriver.Chrome(executable_path=r"C:\Users\47790147\PycharmProjects\SSOApplication\chromedriver.exe", chrome_options=options)
    driver.maximize_window()
    driver.get("https://sso.msa.apps.yokogawa.build/")
    driver.implicitly_wait(10)
    login_obj(driver)
    yield driver
    import time; time.sleep(10)
    driver.close()

def login_obj(setup):
    lg = Login(setup)
    lg.login_main()

@pytest.fixture(scope="class")
def user_mgnt_obj(setup):
    usmgnt = UserManagement(setup)
    usmgnt.click_user_management_option()
    return usmgnt

@pytest.fixture(scope="class")
def invt_mgnt_obj(setup):
    return InvitationManagement(setup)

@pytest.fixture(scope="class")
def log_view_obj(setup):
    return Log_viewer(setup)

# pytest -vs .\testcases\test_login_page.py --html=sample.html