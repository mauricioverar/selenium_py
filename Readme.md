# 🔍 Automatización de búsqueda en Ecosia con Selenium

Este script automatiza una búsqueda en [Ecosia.org](https://www.ecosia.org) utilizando Selenium WebDriver. Es útil para validar flujos visuales, documentar resultados o integrar pruebas básicas de navegación en pipelines QA.


## 🚀 Requisitos

- Python 3.x  
- [Selenium](https://pypi.org/project/selenium/) (`pip install selenium`)  
- [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible con tu versión de Chrome


## 🧩 Instalación

```bash
pip install selenium
```


## 🧪 Ejecución

```bash
python capturador.py
```


## ⚙️ Opciones del navegador

```python
# options.add_argument("--headless")  # Ejecutar sin interfaz gráfica
```

Descomenta esta línea si deseas ejecutar el navegador en segundo plano (sin mostrar la ventana).


## 📂 Flujo del script

1. Abre [Ecosia.org](https://www.ecosia.org)
2. Espera dinámicamente el campo de búsqueda (`name="q"`)
3. Escribe “selenium python” y simula Enter
4. Espera el contenedor de resultados (`id="main"`)
5. Captura una imagen de los resultados como `ecosia_resultados.png`


## 🧠 Buenas prácticas aplicadas

- Uso de `WebDriverWait` con `expected_conditions` para evitar `sleep` fijo
- Manejo de errores con `try/except/finally`
- Captura visual para validación o documentación
- Comentarios estratégicos para facilitar adaptaciones


## 📌 Notas adicionales

- Ideal para pruebas de validación visual, documentación de flujos o demostraciones técnicas.
