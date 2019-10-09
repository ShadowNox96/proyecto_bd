# proyecto_bd
Punto de venta para un negocio de repuestos. Desarrollado en Python y bd en mysql

REQUISITOS
  - Tener instalado virtual env
  - Tener instalado el conector de mysql con django
  - Tener XAMMP o WAMMP
  - Crear una base de datos llamada "sistemagestionventas" (se pude cambiar en el archivo setings.py al igual que la cadena de conexion)
  
  
  
CORRER EL PROYECTO
  - Abrir la consola de comandos de windows o linux.
  - Dirigirnos a la ruta del proyecto.
  - Entrar a la carpeta Entorno_Virtual.
  - Dentro de la carpeta entramos a la carpeta Scripts 
  - Escribimos en la consola activate
  * Se nos activara el entorno virtual.
  - Volvemos con cd .. hasta la ruta raiz del proyecto
  - Entramos a la carpeta Sistema_Gestion_Ventas 
  * Dentro de la carpeta tendremos el archivo llamado manage.py entonces ejecutamos:  
    - manage.py makemigrations(para crear la migracion)
    - manage.py migrate (para migrar los modelos)
    - manage.py runserver (correr el proyecto)
