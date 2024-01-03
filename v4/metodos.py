#metodos.py

#Librerias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Definicion de FUNCIONES (recibe un elemento, de tipo texto)

#    DRIVER

#    CARGA CHROME

def configurar_navegador(driver):
    driver = webdriver.Chrome()
    driver.set_window_size(1111, 631)

def visitar_web(driver,url):
    driver.get(url)

#    BUSCADOR

def escribir_busqueda(driver,elemento,texto):
    driver.find_element(By.ID, elemento)
    driver.find_element(By.ID, elemento).click()
    #driver.find_element(By.CLASS_NAME, elemento).clear()
    driver.find_element(By.ID, elemento).send_keys(texto+Keys.ENTER)

#   RESULTADOS

def obtener_resultados(driver,elemento):
    txt_numeroResultados = driver.find_element(By.CLASS_NAME, elemento)
    texto_resultados = txt_numeroResultados.text
    print("Elementos totales:", texto_resultados)
    #driver.find_element(By.CLASS_NAME, elemento).clear()
   

    
    
    
