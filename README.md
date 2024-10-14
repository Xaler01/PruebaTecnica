# **Prueba Técnica de Automatización**

Este repositorio contiene las soluciones a dos ejercicios prácticos de automatización de pruebas. Uno realizado con Selenium para la tienda web Demoblaze y otro con Karate para la API de PetStore. A continuación se detallan los dos ejercicios:

## **1. Ejercicio de Demoblaze (Selenium con Python)**

### Descripción:
El objetivo de este ejercicio fue automatizar el flujo de compra en el sitio web [Demoblaze](https://www.demoblaze.com/) utilizando Selenium con Python. La prueba cubre la selección de productos, el agregado de estos al carrito, la finalización de la compra y la generación de reportes mediante Allure.

### Estructura del Proyecto:
- **`features/`**: Contiene el archivo `.feature` para la prueba de compra.
- **`steps/`**: Contiene los pasos definidos en Python para interactuar con la web.
- **`pages/`**: Implementación de las clases bajo el patrón Page Object Model (POM) para la separación de la lógica de las páginas web.
- **`reports/`**: Contiene los resultados de las pruebas y reportes generados.
- **`venv/`**: Entorno virtual de Python con las dependencias del proyecto.
  
### Instrucciones para Ejecución:
1. **Crear y activar un entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate

2. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt  

3. **Ejecutar las pruebas:**  

    ```bash
    behave -f allure_behave.formatter:AllureFormatter -o reports/allure_results 

4. **Para generar el reporte Allure, asegúrate de tener instalado Allure:**  

    ```bash
    brew install allure
    allure serve reports/allure_results

## **2. Ejercicio de PetStore (Karate con Java)**

### Descripción:
Este ejercicio se centró en probar los endpoints de la API de PetStore. Se utilizó Karate para ejecutar cuatro escenarios de prueba, los cuales verifican la creación, actualización y recuperación de una mascota.

### Estructura del Proyecto:
- **`src/test/resources/api/petstore/`**: Contiene los archivos `.feature` que describen los escenarios de prueba de la API.
  - `01_add_pet.feature`: Prueba para agregar una nueva mascota.
  - `02_get_pet_Id.feature`: Prueba para obtener la mascota por ID.
  - `03_update_pet.feature`: Prueba para actualizar los detalles de la mascota.
  - `04_get_pet_by_status.feature`: Prueba para obtener mascotas según su estado.
- **`PetStoreTestRunner.java`**: Clase ejecutora de las pruebas con Karate.
- **`karate-reports/`**: Contiene los reportes de las pruebas ejecutadas.

### Instrucciones para Ejecución:
1. Clonar el repositorio y navegar a la carpeta de **PetStore**.
2. Ejecutar las pruebas con Maven:
   ```bash
   mvn test
3. Para visualizar los reportes, abrir el archivo karate-summary.html en la carpeta target/karate-reports/.

### Conclusiones Generales:

Ambos ejercicios, **Demoblaze** y **PetStore**, fueron abordados utilizando diferentes enfoques de automatización. Para **Demoblaze**, se aplicó **Selenium** con el patrón de diseño **Page Object Model (POM)** para la automatización de la interfaz de usuario en un flujo completo de compra. En el ejercicio de **PetStore**, se empleó **Karate** para realizar pruebas de API, cubriendo la creación, actualización y recuperación de mascotas.

En conjunto, estos ejercicios demostraron la versatilidad y eficacia de ambas herramientas para abordar diferentes tipos de pruebas (UI y API) y garantizar la calidad del software. 

#### Para más detalles específicos sobre cada ejercicio, puedes consultar el `README.md` correspondiente en cada carpeta. ####
