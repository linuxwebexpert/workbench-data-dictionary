.. Manual de WB Datadict documentation master file, created by
   sphinx-quickstart on Wed Jul 27 22:16:35 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Manual de WB Datadict
#####################

WB Datadict es un *plugin* para `MySQL Workbench`_ Community Edition
6.x.  Este *plugin* le permite generar un diccionario de datos en
formato HTML a partir de un esquema de la base de datos.

:Licencia:  Dominio público
:Sitio web: http://sirgazil.bitbucket.org/es/artifacts/wb-datadict/


.. figure:: https://multimedialib.files.wordpress.com/2015/10/wb-datadict-101.png
   :align: center
   :alt: Figura 1.

   Figura 1. Pantallazo del plugin siendo usado en MySQL Workbench CE
   6.x.



Instalación
===========

1. Descargue `wb-datadict-1.1.0.tar.gz`_.
2. Descomprima el archivo.
3. Abra MySQL Workbench.
4. En el menú principal de la aplicación, seleccione la opción
   **Scripting → Install Plugin/Module**.
5. Busque el directorio de WB Datadict (extraído en el paso 2) y
   seleccione el archivo ``datadict_grt.py``.

   Debería ver un mensaje como este::

       Plugin Installed
       Plugin /path/to/datadict_grt.py was installed, please restart Workbench to use it.

6. Reinicie MySQL Workbench.



Uso
===

1. Abra un modelo de base de datos o cree uno nuevo (File → New Model).
2. En el menú principal de la aplicación, seleccione la opción
   **Tools → Catalog → Generate HTML Data Dictionary** para generar el
   diccionario (vea la *Figura 1*).

Note que si su Modelo tiene varios esquemas, primero tiene que
seleccionar el esquema a partir del cual quiere generar el diccionario
de datos. Así:

1. Seleccione la pestaña **MySQL Model**.
2. En la sección **Physical Schemas**, seleccione la pestaña del esquema
   deseado.
3. Genere el diccionario de datos.

Después de esto, se genera un diccionario en formato HTML y se abre su
navegador web para mostrarlo.



Ejemplo
=======

.. figure:: https://multimedialib.files.wordpress.com/2016/07/wb-datadict-110-sakila.png
   :align: center
   :alt: Figura 2.

   Figura 2. Pantallazo de un diccionario de datos generado a partir de
   una versión comentada de la base de datos «Sakila», que viene con
   MySQL Workbench CE 6.x.



Historial de versiones
======================

Versión 1.1.0, julio 28, 2016
    * Se agregó columna para indicar clave foránea (FK, Foreign Key),
      que enlaza a la tabla relacionada.
    * Se corrigió el indicador de unicidad (UQ, Unique), que antes
      no mostraba ningún estado, así estuviera marcado en el modelo.
    * Se mejoró la estructura HTML y estilo CSS del documento generado.
    * Se agregó resaltado de tablas cuando se presionan enlaces que
      llevan a ellas.

Versión 1.0.1, octubre 30, 2015
    * Se corrigieron errores de validación de HTML5.
    * Se corrigió un error tipográfico en el documento generado
      («Dictionary» en vez de «Dictionay»).
    * Se agregó escape de caracteres especiales de HTML.

Versión 1.0.0, septiembre 11, 2014
    * Se actualizó el *plugin* para funcionar con MySQL Workbench 6.x.
    * Se actualizó información de contacto del autor.
    * Se cedió el *plugin* al dominio público.

Versión 0.8, diciembre 24, 2011
    * Se agregó la funcionalidad de mostrar el diccionario generado en
      el navegador web.
    * Se eliminó el orden alfabético de columnas para respetar el orden
      usado en el diagrama EER.



.. REFERENCIAS
.. _MySQL Workbench: http://mysqlworkbench.org/
.. _wb-datadict-1.1.0.tar.gz: https://bitbucket.org/sirgazil/wb-datadict/downloads/wb-datadict-1.1.0.tar.gz
