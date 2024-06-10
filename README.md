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


- Para ingresar al Admin de la BD:
Acceder al link: http://127.0.0.1:8000/admin
Usuario: carlos
Password: 123456

- Probar los Formularios de Inserción
1 Acceder a las Páginas de Inserción:
Abre tu navegador y accede a las siguientes URLs para probar los formularios de inserción:
** http://127.0.0.1:8000/add-mask/

Ejemplo de prueba para agregar un mascarilla rellenando el formulario:
Máscara:
Nombre: Máscara N95
Descripción: Máscara N95 de alta calidad
Precio: 10.00
Imagen: Sube una imagen de ejemplo.

** http://127.0.0.1:8000/add-surgical-cap/

Ejemplo de prueba para agregar un Gorro quirúrgico rellenando el formulario:
Nombre: Gorro Azul
Descripción: Gorro quirúrgico azul
Precio: 5.00
Imagen: Sube una imagen de ejemplo.


** http://127.0.0.1:8000/add-custom-order/

Ejemplo de prueba para agregar una Orden personalizada rellenando el formulario:
Tipo de Producto: Máscara
Texto Personalizado: Personalización para Cliente A


2 Rellenar y Enviar los Formularios:
Completa los formularios con los datos correspondientes y presiona el botón de enviar.

3 Verificar la Inserción en la Base de Datos:
Verifica que los datos se hayan guardado correctamente accediendo a las listas de productos (por ejemplo, en /masks/ y /caps/).
Probar el Formulario de Búsqueda

- Acceder a la Página de Búsqueda:
** Abre tu navegador y accede a http://127.0.0.1:8000/search/.

** Realizar Búsquedas:
Ingresa un término de búsqueda que coincida con los productos en tu base de datos.
Verifica que los resultados se muestren correctamente y que los enlaces a los detalles del producto funcionen.

- Verificar Resultados de Búsqueda:
Asegúrate de que los resultados coincidan con los datos ingresados en la base de datos y que se muestren correctamente.