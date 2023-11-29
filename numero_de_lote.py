from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)


def bajar_pagina():
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, 2):
        driver.execute_script("window.scrollTo(0, {});".format(i))


def ventana():
    driver.maximize_window()
    driver.get("https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus")
    driver.find_element(By.ID, 'submit').click()
    bajar_pagina()
    time.sleep(1)


def ciudad():
    find_office_name = \
        driver.find_element(By.ID, 'form')
    select_city = Select(find_office_name)
    select_city.select_by_visible_text('Madrid')
    driver.find_element(By.ID, 'btnAceptar').click()
    time.sleep(1)


def oficina():
    select_oficina = Select(driver.find_element(By.ID, 'sede'))
    select_oficina.select_by_visible_text('CNP SAN FELIPE TIE, SAN FELIPE, 7')
    time.sleep(0.5)


def tramites():
    select_tramite_name = Select(driver.find_element(By.ID, "tramiteGrupo[0]"))
    select_tramite_name.select_by_visible_text("POLICIA - RECOGIDA DE TARJETA DE IDENTIDAD DE EXTRANJERO (TIE)")
    driver.find_element(By.ID, 'btnAceptar').click()
    time.sleep(2)


ventana()
ciudad()
oficina()
tramites()

lote = driver.find_element(By.XPATH, '//*[@id="mainWindow"]/div/div/section/div[2]/form/div[1]/h3').text
print(lote)

# driver.quit()
