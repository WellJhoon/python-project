import time
from selenium.webdriver.support import expected_conditions as EC
from MainStuff.base import Base
from selenium.webdriver.common.by import By

# pytest -v --html=results/report.html ejecutar en la terminal para hacer report

class Mainpage(Base):
    # metodo constructor cuando creamos objeto de esta clase va inicializar con los siguiente atri
    def __init__(self,driver,wait):
        self.url = 'http://127.0.0.1:3000/index.html' # url de la pagina

        super().__init__(driver, wait) # llamando el metodo init de la clase padre

    def ir_pagina_busc(self):
        self.ir_pagina(self.url) # aqui estoy yiendo a la pagina que le pasamos

    def chek_url(self,url):
        assert self.give_url() == url # si la url que le pasamos es igual a la url true si no tira error..


    def login_fail(self,mail,password):

        self.driver.find_element(By.XPATH,"//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div")))
        time.sleep(2)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/fail_login.png')

    def login_succes(self,mail,password):

        self.driver.find_element(By.XPATH,"//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div")))
        time.sleep(2)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/succes_login.png')

    def blocked_users_fail(self,mail,password):

        self.driver.find_element(By.XPATH,"//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div")))
        time.sleep(2)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/blocked_users_fail.png')

    def blocked_users_succes(self, mail, password):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div")))
        time.sleep(2)
        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/blocked_users_succes.png')

    def contact_empty_fail(self, mail, password, name, lastName, number, address):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div")))
        time.sleep(4)

        self.driver.find_element(By.XPATH, "//*[@id='nombre']").send_keys(name)
        self.driver.find_element(By.XPATH, "// *[ @ id = 'apellido']").send_keys(lastName)
        self.driver.find_element(By.XPATH, "//*[@id='telefono']").send_keys(number)
        self.driver.find_element(By.XPATH, "//*[@id='direccion']").send_keys(address)
        self.driver.find_element(By.XPATH, "// *[ @ id = 'btn-agregar']").click()
        time.sleep(3)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/contact_empty_fail.png')

    def contact_empty_succes(self, mail, password, name, lastName, number, address):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div")))
        time.sleep(3)

        self.driver.find_element(By.XPATH, "// *[ @ id = 'nombre']").send_keys(name)
        self.driver.find_element(By.XPATH, "// *[ @ id = 'apellido']").send_keys(lastName)
        self.driver.find_element(By.XPATH, "//*[@id='telefono']").send_keys(number)
        self.driver.find_element(By.XPATH, "//*[@id='direccion']").send_keys(address)
        self.driver.find_element(By.XPATH, "//*[@id='btn-agregar']").click()
        time.sleep(3)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/contact_empty_succes.png')


    def search_fail(self, mail, password, word):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div")))
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//*[@id='buscar']").send_keys(word)
        time.sleep(1)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/search_fail.png')

    def search_succes(self, mail, password, word, name, lastName, number, address):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div")))
        time.sleep(3)

        self.driver.find_element(By.XPATH, "// *[ @ id = 'nombre']").send_keys(name)
        self.driver.find_element(By.XPATH, "// *[ @ id = 'apellido']").send_keys(lastName)
        self.driver.find_element(By.XPATH, "//*[@id='telefono']").send_keys(number)
        self.driver.find_element(By.XPATH, "//*[@id='direccion']").send_keys(address)
        self.driver.find_element(By.XPATH, "//*[@id='btn-agregar']").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "// *[ @ id = 'nombre']").send_keys('Haroldy')
        self.driver.find_element(By.XPATH, "// *[ @ id = 'apellido']").send_keys('Martinez')
        self.driver.find_element(By.XPATH, "//*[@id='telefono']").send_keys('234546234')
        self.driver.find_element(By.XPATH, "//*[@id='direccion']").send_keys('Santo Domingo')
        self.driver.find_element(By.XPATH, "//*[@id='btn-agregar']").click()
        time.sleep(4)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/search_succes1.png')
        self.driver.find_element(By.XPATH, "//*[@id='buscar']").send_keys(word)
        time.sleep(1)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/search_succes2.png')

    def storage_empty_fail(self, mail, password):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div")))
        time.sleep(3)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/storage_empty_fail.png')

    def storage_empty_succes(self, mail, password, name, lastName, number, address):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div")))
        time.sleep(3)

        self.driver.find_element(By.XPATH, "// *[ @ id = 'nombre']").send_keys(name)
        self.driver.find_element(By.XPATH, "// *[ @ id = 'apellido']").send_keys(lastName)
        self.driver.find_element(By.XPATH, "//*[@id='telefono']").send_keys(number)
        self.driver.find_element(By.XPATH, "//*[@id='direccion']").send_keys(address)
        self.driver.find_element(By.XPATH, "//*[@id='btn-agregar']").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "// *[ @ id = 'nombre']").send_keys('Haroldy')
        self.driver.find_element(By.XPATH, "// *[ @ id = 'apellido']").send_keys('Martinez')
        self.driver.find_element(By.XPATH, "//*[@id='telefono']").send_keys('234546234')
        self.driver.find_element(By.XPATH, "//*[@id='direccion']").send_keys('Santo Domingo')
        self.driver.find_element(By.XPATH, "//*[@id='btn-agregar']").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "// *[ @ id = 'nombre']").send_keys('Cristian')
        self.driver.find_element(By.XPATH, "// *[ @ id = 'apellido']").send_keys('Rodriguez')
        self.driver.find_element(By.XPATH, "//*[@id='telefono']").send_keys('23463453')
        self.driver.find_element(By.XPATH, "//*[@id='direccion']").send_keys('Distrito Nacional')
        self.driver.find_element(By.XPATH, "//*[@id='btn-agregar']").click()
        time.sleep(5)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/storage_empty_succes.png')


    def add_contact_fail(self, mail, password, name, lastName, number, address):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div")))
        time.sleep(3)

        self.driver.find_element(By.XPATH, "// *[ @ id = 'nombre']").send_keys(name)
        self.driver.find_element(By.XPATH, "// *[ @ id = 'apellido']").send_keys(lastName)
        self.driver.find_element(By.XPATH, "//*[@id='telefono']").send_keys(number)
        self.driver.find_element(By.XPATH, "//*[@id='direccion']").send_keys(address)
        self.driver.find_element(By.XPATH, "//*[@id='btn-agregar']").click()
        time.sleep(4)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/add_contact_fail.png')


    def add_contact_succes(self, mail, password, name, lastName, number, address):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div")))
        time.sleep(3)

        self.driver.find_element(By.XPATH, "// *[ @ id = 'nombre']").send_keys(name)
        self.driver.find_element(By.XPATH, "// *[ @ id = 'apellido']").send_keys(lastName)
        self.driver.find_element(By.XPATH, "//*[@id='telefono']").send_keys(number)
        self.driver.find_element(By.XPATH, "//*[@id='direccion']").send_keys(address)
        time.sleep(1)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/add_contact_succes1.png')
        self.driver.find_element(By.XPATH, "//*[@id='btn-agregar']").click()
        time.sleep(4)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/add_contact_succes2.png')

    def dark_mode_fail(self, mail, password, name):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//*[@id='nombre']").send_keys(name)
        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/dark_mode_fail1.png')
        self.driver.find_element(By.XPATH, "//*[@id='toogle']").click()
        time.sleep(2)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/dark_mode_fail2.png')

    def dark_mode_succes(self, mail, password):
        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//*[@id='toogle']").click()
        time.sleep(1)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/dark_mode_succes1.png')
        time.sleep(3)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/dark_mode_succes2.png')

    def logOut_fail(self, mail, password, name):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//*[@id='nombre']").send_keys(name)
        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/logOut_fail1.png')
        self.driver.find_element(By.XPATH, "//*[@id='log-Out']").click()
        time.sleep(2)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/logOut_fail2.png')

    def logOut_succes(self, mail, password):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//*[@id='log-Out']").click()
        time.sleep(1)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/logOut_succes.png')

    def user_correct_fail(self, mail, password):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/user_correct_fail1.png')
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        time.sleep(1)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/user_correct_fail2.png')

    def user_correct_succes(self, mail, password):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/user_correct_succes1.png')
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        time.sleep(1)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/user_correct_succes2.png')

    def isNaN_number_fail(self, mail, password, name, lastName, number, address):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div")))
        time.sleep(3)

        self.driver.find_element(By.XPATH, "// *[ @ id = 'nombre']").send_keys(name)
        self.driver.find_element(By.XPATH, "// *[ @ id = 'apellido']").send_keys(lastName)
        self.driver.find_element(By.XPATH, "//*[@id='telefono']").send_keys(number)
        self.driver.find_element(By.XPATH, "//*[@id='direccion']").send_keys(address)
        time.sleep(1)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/isNaN_number_fail1.png')
        self.driver.find_element(By.XPATH, "//*[@id='btn-agregar']").click()
        time.sleep(2)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/isNaN_number_fail2.png')

    def isNaN_number_succes(self, mail, password, name, lastName, number, address):

        self.driver.find_element(By.XPATH, "//*[@id='correo']").send_keys(mail)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div")))
        time.sleep(3)

        self.driver.find_element(By.XPATH, "// *[ @ id = 'nombre']").send_keys(name)
        self.driver.find_element(By.XPATH, "// *[ @ id = 'apellido']").send_keys(lastName)
        self.driver.find_element(By.XPATH, "//*[@id='telefono']").send_keys(number)
        self.driver.find_element(By.XPATH, "//*[@id='direccion']").send_keys(address)
        time.sleep(1)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/isNaN_number_succes1.png')
        self.driver.find_element(By.XPATH, "//*[@id='btn-agregar']").click()
        time.sleep(2)

        self.driver.save_screenshot('C:/Users/Harol/Downloads/pyTestSwagLabs/results/isNaN_number_succes2.png')