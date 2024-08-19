
![Entornos_Virtuales_Python_Color](https://github.com/user-attachments/assets/2bc2da00-7cb6-4aa5-a045-c129f2b5cb2f)


Resumen:

  * virtualenv: Buena opción para personalización y proyectos con diferentes versiones de Python.
    
  - Crear un Entorno Virtual con virtualenv = Primero, asegúrate de que virtualenv esté instalado. Si no lo está, puedes instalarlo con:  (pip install virtualenv)
    Luego, crea un entorno virtual: (virtualenv myenv) Esto creará un directorio llamado myenv que contiene el entorno virtual.

  Para activarlo:
  
  En Windows: myenv\Scripts\activate

  En macOS/Linux: source myenv/bin/activate

 -------------------
 
  * venv: Ideal para la mayoría de los proyectos con Python 3.3+ debido a su simplicidad.

  Crear un Entorno Virtual con venv = venv viene integrado con Python 3.3 y posteriores, por lo que no necesitas instalar nada adicional. Para crear un entorno virtual: (python -m venv myenv)

  Esto crea un directorio llamado myenv con el entorno virtual. 
  
  Para activarlo:

  En Windows (myenv\Scripts\activate)

  En macOS/Linux: source myenv/bin/activate

  Deactivate para Salir de los entornos virtuales

-----------------

 * pipenv: Recomendada para la gestión completa del proyecto, incluyendo entornos virtuales y dependencias.

   Crear un Entorno Virtual con pipenv

   Primero, asegúrate de tener pipenv instalado. Puedes instalarlo con:

   pip install pipenv

   Para crear un entorno virtual y manejar las dependencias:

   pipenv install

   Esto creará un entorno virtual y generará un archivo Pipfile que gestiona las dependencias del proyecto.

   Para activar el entorno virtual:

   pipenv shell

   _________

   Resumen:

  •	virtualenv: Buena opción para personalización y proyectos con diferentes versiones de Python

  •	venv: Ideal para la mayoría de los proyectos con Python 3.3+ debido a su simplicidad
	
 •	pipenv: Recomendada para la gestión completa del proyecto, incluyendo entornos virtuales y dependencias

  
       
