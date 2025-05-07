from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.options import Options
import time

# Inicializar el driver con opciones específicas
options = Options()
#options.add_argument("--headless")  #comentar para mostrar navegador
# descomentar --headless para abrir el navegador sin mostrar la interfaz gráfica.

driver = webdriver.Chrome(options=options)  # Iniciar el driver de Chrome ***

try:
  # Ir al sitio web y capturar la pantalla ***
    driver.get("https://www.google.com")

    # Esperar hasta que la página se cargue completamente ***
    time.sleep(3)

    # Captura de pantalla del resultado ***
    driver.save_screenshot("google2.png")

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()  # Cerrar el driver ***
  