from selenium import webdriver
#El driver que usaremos para poder interactuar con el navegador
from selenium.webdriver import Chrome
#Ayuda a gestionar de forma automática las configuraciones del webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

from dotenv import load_dotenv
import os
import time


class Scrap:
    def __init__(self,url):
        try:
            self.url            = url
            self.headless       = True
            self.configuracion  = self.config()
            self.user           = os.getenv("USER")
            self.password       = os.getenv("PASSWORD")
        except Exception as e:
            print(f'Error en constructor: {repr(e)}')
    
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
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    scrap1 = Scrap("https://www.saucedemo.com/")
    scrap1.realizar_scrap()