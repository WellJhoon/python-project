import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from MainStuff.main_page import Mainpage

class TestSearh():

    @pytest.fixture
    def Test_inicialP(self):

        #******************* configuraciones de selenium *******************

        option = webdriver.ChromeOptions()
        option.add_argument("start-maximized")

        option.add_experimental_option("detach", True) # chrome to stay open

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        self.wait = WebDriverWait(self.driver,10)

        # ****************************************************************************************************

        self.page = Mainpage(self.driver,self.wait)
        self.page.ir_pagina_busc()

    def test_login_fail(self,Test_inicialP):
        self.page.login_fail('aasasasas','asasdsassa')

    def test_login_succes(self,Test_inicialP):
        self.page.login_succes('jhon@gmail.com','1234')

    def test_blocked_users_fail(self,Test_inicialP):
        self.page.blocked_users_fail('bryancastillo@gmail.com','ththrthrt')

    def test_blocked_users_succes(self,Test_inicialP):
        self.page.blocked_users_succes('jhon@gmail.com','1234')

    def test_contact_empty_fail(self,Test_inicialP):
        self.page.contact_empty_fail('jhon@gmail.com','1234', '', '', '', '')

    def test_contact_empty_succes(self,Test_inicialP):
        self.page.contact_empty_succes('jhon@gmail.com','1234', 'Carlos', 'Castillo', '8494535632', 'Santo Domingo')

    def test_search_fail(self, Test_inicialP):
        self.page.search_fail('jhon@gmail.com', '1234', 'Ronaldo')

    def test_search_succes(self,Test_inicialP):
        self.page.search_succes('jhon@gmail.com','1234', 'jhon', 'Carlos', 'Castillo', '8494535632', 'Santo Domingo')

    def test_storage_empty_fail(self, Test_inicialP):
        self.page.storage_empty_fail('jhon@gmail.com', '1234')

    def test_storage_empty_succes(self,Test_inicialP):
        self.page.storage_empty_succes('jhon@gmail.com','1234', 'Carlos', 'Castillo', '849453632', 'Santo Domingo')

    def test_add_contact_fail(self,Test_inicialP):
        self.page.add_contact_fail('jhon@gmail.com','1234', 'josess39@gmail.com', 'Castillo', '8494535632', 'Santo Domingo')

    def test_add_contact_succes(self,Test_inicialP):
        self.page.add_contact_succes('jhon@gmail.com','1234', 'Johan', 'Castillo', '83556323', 'Puerto Plata')

    def test_dark_mode_fail(self,Test_inicialP):
        self.page.dark_mode_fail('jhon@gmail.com','1234', 'Alex')

    def test_dark_mode_succes(self,Test_inicialP):
        self.page.dark_mode_succes('jhon@gmail.com','1234')

    def test_logOut_fail(self,Test_inicialP):
        self.page.logOut_fail('jhon@gmail.com','1234', 'jhon')

    def test_logOut_succes(self,Test_inicialP):
        self.page.logOut_succes('jhon@gmail.com','1234')

    def test_user_correct_fail(self, Test_inicialP):
        self.page.user_correct_fail('jhongrg', '1234')

    def test_user_correct_succes(self, Test_inicialP):
        self.page.user_correct_succes('jhon@gmail.com', '1234')

    def test_isNaN_number_fail(self,Test_inicialP):
        self.page.isNaN_number_fail('jhon@gmail.com','1234', 'Johan', 'Castillo', 'gfg23423', 'Puerto Plata')

    def test_isNaN_number_succes(self,Test_inicialP):
        self.page.isNaN_number_succes('jhon@gmail.com','1234', 'Johan', 'Castillo', '82943213', 'Puerto Plata')