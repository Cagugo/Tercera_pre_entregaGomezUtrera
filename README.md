# Medical Apparel eCommerce

## Requisitos

- Python 3.x
- Django

## Instalación

1. Clona el repositorio.
2. Navega al directorio del proyecto.
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Aplica las migraciones:
    ```bash
    python manage.py migrate
    ```

## Ejecución

- Ejecutar y Probar la Aplicación

- Ejecutar el Servidor de Desarrollo

- Iniciar el Servidor:

- Ejecuta el servidor de desarrollo con el comando:
python manage.py runserver

- Probar los Formularios de Inserción
1 Acceder a las Páginas de Inserción:
Abre tu navegador y accede a las siguientes URLs para probar los formularios de inserción:
http://127.0.0.1:8000/add-mask/
http://127.0.0.1:8000/add-surgical-cap/
http://127.0.0.1:8000/add-custom-order/

2 Rellenar y Enviar los Formularios:
Completa los formularios con los datos correspondientes y presiona el botón de enviar.

3 Verificar la Inserción en la Base de Datos:
Verifica que los datos se hayan guardado correctamente accediendo a las listas de productos (por ejemplo, en /masks/ y /caps/).
Probar el Formulario de Búsqueda

- Acceder a la Página de Búsqueda:
Abre tu navegador y accede a http://127.0.0.1:8000/search/.

- Realizar Búsquedas:
Ingresa términos de búsqueda en el formulario y presiona el botón de búsqueda.

- Verificar Resultados de Búsqueda:
Asegúrate de que los resultados coincidan con los datos ingresados en la base de datos y que se muestren correctamente.