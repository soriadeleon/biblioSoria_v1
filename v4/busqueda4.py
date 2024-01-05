import re
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #as EC es como queremos que se llame
#Se añade Options para añadir User-Agent para evitar ser detectados como bots
from selenium.webdriver.chrome.options import Options

import undetected_chromedriver as uc


#Importar selectores
#from selectores import obtener_selectores_busqueda
from selectores import obtener_selectores_resultados

#METODOS
from metodos import escribir_busqueda
from metodos import visitar_web
from metodos import obtener_resultados

# try: = prueba estas sentancias del test / expect Excepcion:
try: 


        driver = uc.Chrome()

# Carga de Chrome y configuracion
        
        driver = webdriver.Chrome()
        driver.set_window_size(1111, 631)

# Navegacion a la url
        visitar_web(driver,"https://bibliotecas.jcyl.es/web/es/bibliotecasoria/biblioteca-publica-soria.html")
        
        driver.implicitly_wait(5) #Espera Implicita de 10s maximo para cualquier elemento
                

# Realizar busqueda
        escribir_busqueda(driver, "cadena", "Numancia")
        time.sleep(10)

# (CAMBIO DE PESTAÑA) Pagina de resultados
     
        # Esperar a que se abra la nueva ventana o pestaña
        driver.wait = WebDriverWait(driver, 10)
        driver.wait.until(lambda d: len(driver.window_handles) == 2)  # Esperar a que haya dos ventanas/pestañas abiertas

        # Cambiar el foco a la nueva pestaña
        ventana_buscador = driver.window_handles[0]
        ventana_resultados = driver.window_handles[1]
        driver.switch_to.window(ventana_resultados)

        print("cambio de pestaña OK")
# Encontrar el texto de numero de resultados y copiarlo
        
        pantalla_resultados = obtener_selectores_resultados()
# Se añade espera explicita para que espere a la carga del elemento main_h2_2 y se elimina el time sleep
        elemento = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, pantalla_resultados["txt_resultados"]))
        )
        texto_resultado = elemento.text

        obtener_resultados(driver, pantalla_resultados["txt_resultados"])
      
       
#Se corrige el ASSERT para practicar las vueltas al archivo json
        assert "(398 registros)" == texto_resultado, "No se ha recibido el valor esperado"

except AssertionError as mensajeAssertionError:
    print("Mensaje de error: " , mensajeAssertionError)
except Exception as mensajeException:
    print("Mensaje de error: " , mensajeException)
except FileNotFoundError as mensajeFileNotFoundError:
    print("Mensaje de error: " , mensajeFileNotFoundError)


print(" --- FIN DE TEST --- ")

time.sleep(5)

driver.quit()