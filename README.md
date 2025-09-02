# Dashboard_app
 Producción de petróleo crudo de Petróleos Mexicanos, miles de barriles diarios



*** Configuracion de entono virtual *** (power shell)
-  python -m venv TTen
-  tten\Scripts\activate

***Librerias p/calidad de codigo***
- Formato automatico
pip install black      #  formatea el codigo segun convenciones estrictas (PEP 8)
pip install autopep8   #  Ajusta el codigo automaticamente

***Analisis de estilo***
pip install flake8          # Detecta errores de estilo, sintaxis, complijidad
pip install pylint          # Revicion exhaustiva con puntuacion y sugerencias
pip install pycodestyle     # Verifica cumplimiento de  PEP8 sin modificar codigo 

***Chequeo de tipos***
pip install mypy            # Verifica tipos estaticos usando anotaciones

***Archivo de requirements.txt***
pip freeze > requirements.txt

***Instalar todas las dependencias***
pip install -r .\requirements.txt

***purga de cache***
pip cache purge

https://www.historico.datos.gob.mx/busca/dataset/produccion-de-petroleo-crudo-de-petroleos-mexicanos


pip install ipykernel    -# - Registra tu entorno virtual como un kernel disponible en Jupyter.
                          # - Es clave para entornos reproducibles, ya que puedes tener múltiples kernels aislados para distintos proyectos.




