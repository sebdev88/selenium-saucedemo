from selenium import webdriver
#El driver que usaremos para poder interactuar con el navegador
from selenium.webdriver import Chrome
#Ayuda a gestionar de forma automática las configuraciones del webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from dotenv import load_dotenv
import os
import time
"""
var     = público
_var    = protegido
__var   = privado
"""

class Scrap:
    def __init__(self,url):
        try:
            self.__url            = url
            self.headless       = True
            self.configuracion  = self.config()
            self.user           = os.getenv("USER")
            self.password       = os.getenv("PASSWORD")
            self.nombre         = os.getenv("NOMBRE")
            self.apellido       = os.getenv("APELLIDO")
            self.postal_code    = os.getenv("POSTALCODE")
        except Exception as e:
            print(f'Error en constructor: {repr(e)}')
    
    @property #Getter
    def url(self):
        return self.__url
    
    @url.setter #Setter
    def url(self, nueva_url):
        self.__url = nueva_url
    
    def config(self):
        try:
            service = Service(ChromeDriverManager().install())
            option = webdriver.ChromeOptions()
            driver = Chrome(service=service, options=option)
            dict_conf = {
                'service': service,
                'option': option,
                'driver': driver
            }
            return dict_conf
        except Exception as e:
            print(f'Error en configuración: {repr(e)}')
        
    def hide(self):
        try:
            if self.headless == True:
                print(f'Headless ya configurado anteriormente')
            else:
                option = webdriver.ChromeOptions()
                option.add_argument("--headless")
                print(f'Headless activado')
        except Exception as e:
            print(f'Error en función hide: {repr(e)}')

    def tamanio(ancho:int, alto:int):
        try:
            option = webdriver.ChromeOptions()
            option.add_argument(f"--window-size={ancho},{alto}")
        except Exception as e:
            print(f'Error en función tamanio: {repr(e)}')

    #Se requiere crear un driver que es la que maneja la web
    def realizar_scrap(self):
        driver = self.configuracion['driver']
        driver.get(self.url)

        #Encontrar elementos de formulario / LOGIN
        user_input = driver.find_element(By.ID, "user-name")
        user_input.send_keys(self.user)
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(self.password)
        logging_button = driver.find_element(By.ID, "login-button")
        time.sleep(4)
        logging_button.click()
        time.sleep(2)

        #AGREGAR AL CARRITO
        add_cart1 = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_cart2 = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")

        add_cart1.click()
        add_cart2.click()

        #CARRITO
        #Copiamos del inspector de código el FULL XPATH con click derecho en código seleccionado del elemento
        carrito = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        carrito.click()

        driver.find_element(By.ID, "checkout").click()

        #CHECKOUT
            #FORM
        driver.find_element(By.ID, "first-name").send_keys(self.nombre)
        driver.find_element(By.ID, "last-name").send_keys(self.apellido)
        driver.find_element(By.ID, "postal-code").send_keys(self.postal_code)
            #SEND
        driver.find_element(By.NAME, "continue").click()
            #FINALIZAR
        driver.find_element(By.ID, "finish").click()



        time.sleep(10)

        driver.quit()

if __name__ == "__main__":
    scrap1 = Scrap("https://www.saucedemo.com/")
    scrap1.realizar_scrap()