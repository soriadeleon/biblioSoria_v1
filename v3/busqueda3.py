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

# try: = prueba estas sentancias del test / expect Excepcion:
try: 

# Configurar opciones del navegador con un User-Agent personalizado
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

        options = Options()
        options.add_argument(f"user-agent={user_agent}")

# Carga de Chrome y configuracion
        driver = webdriver.Chrome()
        driver.set_window_size(1111, 631)

# Navegacion a la url
        driver.get("https://bibliotecas.jcyl.es/web/es/bibliotecasoria/biblioteca-publica-soria.html")
        driver.implicitly_wait(5) #Espera Implicita de 10s maximo para cualquier elemento

#Carga del fichero json para obtener las palabras del buscador
        #Indicamos el archivo que queremos abrir
        with open('datos.json',"r") as mi_archivo: #se indica el archivo y se le da nombre
            lector = json.load(mi_archivo) #Se define un lector en una variable
                        
            for renglon in lector:         #Itterar el archivo renglon por renglon
                var_palabraclave = renglon['palabra clave']
                

# Realizar busqueda
        txt_busqueda = driver.find_element(By.ID, "cadena")
        txt_busqueda.click
        #Por dificultades al localizar e interacturar con el botón de busqueda
        #VAR_PALABRACLAVE proporciona el texto desde el fichero JSON
        #    se opta por interaccionar con el mediante pulsación ENTER
        txt_busqueda.send_keys(var_palabraclave+Keys.ENTER)
          
        #aceptar
        print("Busqueda OK")
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
        
# Se añade espera explicita para que espere a la carga del elemento main_h2_2 y se elimina el time sleep
        elemento = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "main_h2_2"))
        )
        
        txt_numeroResultados = driver.find_element(By.CLASS_NAME, "main_h2_2")
        txt_numeroResultados.text
        

        print("Elementos totales: " , txt_numeroResultados.text)
#Se corrige el ASSERT para practicar las vueltas al archivo json
        assert "(398 registros)" == txt_numeroResultados.text, "No se ha recibido el valor esperado"



except AssertionError as mensajeAssertionError:
    print("Mensaje de error: " , mensajeAssertionError)
except Exception as mensajeException:
    print("Mensaje de error: " , mensajeException)
except FileNotFoundError as mensajeFileNotFoundError:
    print("Mensaje de error: " , mensajeFileNotFoundError)


print(" --- FIN DE TEST --- ")

time.sleep(5)

driver.quit()