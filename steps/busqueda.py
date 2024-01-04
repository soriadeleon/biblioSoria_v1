from behave import given
from behave import when
from behave import then

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

 
@given('que ingrese en la web de la Biblioteca de Soria')
def step_given(context):
       context.driver = webdriver.Chrome()
       context.driver.set_window_size(1111, 631)
       context.driver.get("https://bibliotecas.jcyl.es/web/es/bibliotecasoria/biblioteca-publica-soria.html")

@when('realizo la busqueda de "Numancia"')
def step_when(context):
    
        time.sleep(3)
        txt_busqueda = context.driver.find_element(By.ID, "cadena")
        txt_busqueda.click
        txt_busqueda.send_keys('Numancia'+Keys.ENTER)

        print("Busqueda OK")
        
        context.driver.wait = WebDriverWait(context.driver, 10)
        context.driver.wait.until(lambda d: len(context.driver.window_handles) == 2)  # Esperar a que haya dos ventanas/pestañas abiertas

        # Cambiar el foco a la nueva pestaña
        ventana_buscador = context.driver.window_handles[0]
        ventana_resultados = context.driver.window_handles[1]
        context.driver.switch_to.window(ventana_resultados)

        print("cambio de pestaña OK")


@then('compruebo los resultados')
def step_then(context):
      

        elemento = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "main_h2_2"))
        )

        txt_numeroResultados = context.driver.find_element(By.CLASS_NAME, "main_h2_2")
        txt_numeroResultados.text
        

        print("Elementos totales: " , txt_numeroResultados.text)
        time.sleep(1)
        print("--- TEST OK ---")


        context.driver.quit()
        


       
       
