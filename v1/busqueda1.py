import re
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #as EC es como queremos que se llame

import undetected_chromedriver as uc


# try: = prueba estas sentancias del test / expect Excepcion:
try: 

# CARGA INICIAL DEL NAVEGADOR
        
# Carga de Chrome y configuracion
        driver = uc.Chrome()

        driver = webdriver.Chrome()
        driver.set_window_size(1111, 631)

# Navegacion a la url
        driver.get("https://bibliotecas.jcyl.es/web/es/bibliotecasoria/biblioteca-publica-soria.html")
        driver.implicitly_wait(5) #Espera Implicita de 10s maximo para cualquier elemento

# BUSCADOR
# Realizar busqueda
        driver.find_element(By.ID, "cadena")
        driver.find_element(By.ID, "cadena").click
        driver.find_element(By.ID, "cadena").send_keys("Numancia"+Keys.ENTER)

          
        #aceptar
        print("Busqueda OK")
        time.sleep(10)

# CAMBIO DE PESTAÑA    
# Esperar a que se abra la nueva ventana o pestaña
        driver.wait = WebDriverWait(driver, 10)
        driver.wait.until(lambda d: len(driver.window_handles) == 2)  # Esperar a que haya dos ventanas/pestañas abiertas

# Cambiar el foco a la nueva pestaña
        ventana_buscador = driver.window_handles[0]
        ventana_resultados = driver.window_handles[1]
        driver.switch_to.window(ventana_resultados)

        print("cambio de pestaña OK")

        
# PAGINA DE RESULTADOS
# Encontrar el texto de numero de resultados y copiarlo

        time.sleep(10)
        driver.find_element(By.CLASS_NAME, "main_h2_2")
        driver.find_element(By.CLASS_NAME, "main_h2_2").text
        print("Elementos totales: " , driver.find_element(By.CLASS_NAME, "main_h2_2").text)

# Falla a proposito
        assert "(398 registro)" == driver.find_element(By.CLASS_NAME, "main_h2_2").text, "No se ha recibido el valor esperado"

        
        

        time.sleep(3)

except AssertionError as mensajeAssertionError:
    print("Mensaje de AssertionError: " , mensajeAssertionError)
except Exception as mensajeException:
    print("Mensaje de Exception: " , mensajeException)
except FileNotFoundError as mensajeFileNotFoundError:
    print("Mensaje de FileNotFoundError: " , mensajeFileNotFoundError)


print(" ------------------- ")
print(" ---             --- ")
print(" --- FIN DE TEST --- ")
print(" ---             --- ")
print(" ------------------- ")

time.sleep(5)

driver.quit()