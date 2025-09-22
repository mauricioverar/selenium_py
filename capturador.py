from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.options import Options
# import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
#options.add_argument("--headless")  #comentar para mostrar navegador

driver = webdriver.Chrome(options=options)

try:
    # driver.get("https://www.google.com")
    driver.get("https://www.ecosia.org")

    # Esperar hasta que la página se cargue completamente ***
    # time.sleep(3)
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    search_box.send_keys("selenium python")
    search_box.send_keys(Keys.RETURN)

    # Esperar a que aparezcan los resultados
    WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.ID, "search"))
        EC.presence_of_element_located((By.ID, "main"))
    )

    # Captura de pantalla del resultado ***
    # driver.save_screenshot("google2.png")
    driver.save_screenshot("ecosia_resultados.png")

except Exception as e:
    print(f"Error: {e}")
finally:
    # input("Presiona Enter para cerrar el navegador...")
    driver.quit()
