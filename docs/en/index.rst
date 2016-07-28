.. WB Datadict Manual documentation master file, created by
   sphinx-quickstart on Wed Jul 27 22:15:43 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

WB Datadict Manual
##################

WB Datadict is a plugin for `MySQL Workbench`_ Community Edition 6.x.
This plugin allows you to generate an HTML data dictionary from the
database schema selected in the application.

:License:  Public domain
:Website:  http://sirgazil.bitbucket.org/en/artifacts/wb-datadict/


.. figure:: https://multimedialib.files.wordpress.com/2015/10/wb-datadict-101.png
   :align: center
   :alt: Figure 1.

   Figure 1. Screenshot of the plugin being used in MySQL Workbench CE
   6.x.



Installation
============

1. Download `wb-datadict-1.1.0.tar.gz`_.
2. Uncompress the file.
3. Open MySQL Workbench.
4. In the main menu of the application, select the option
   **Scripting → Install Plugin/Module**.
5. Browse to the WB Datadict directory (extracted in step 2) and
   select the file ``datadict_grt.py``.

   You should see a message like this::

       Plugin Installed
       Plugin /path/to/datadict_grt.py was installed, please restart Workbench to use it.

6. Restart MySQL Workbench.



Usage
=====

1. Open a database model file or create a new one (File → New Model).
2. Go to **Tools → Catalog → Generate HTML Data Dictionary** (see
   *Figure 1*).

Note that if your Model file has several schemas, first you will have to
select the schema for which you want to generate the data dictionary.
To do so:

1. Click on the **MySQL Model** tab.
2. In the **Physical Schemas** section, click on the tab of a schema.
3. Generate the data dictionary.

After this, an HTML data dictionary will be generated, and displayed in
your Web browser.



Example
=======

.. figure:: https://multimedialib.files.wordpress.com/2016/07/wb-datadict-110-sakila.png
   :align: center
   :alt: Figure 2.

   Figure 2. Screenshot of the data dictionary of a commented version of
   the Sakila database that comes with MySQL Workbench CE 6.x.



Version History
===============

Version 1.1.0, July 28, 2016
    * Added Foreign Key column, which links to the related table.
    * Fixed Unique constraint indicator.
    * Enhanced HTML structure and CSS style.
    * Added table highlighting when clicking on links.

Version 1.0.1, October 30, 2015
    * Fixed HTML5 validation errors.
    * Fixed typo on generated document ("Dictionary" instead of
      "Dictionay").
    * Convert special characters into HTML-safe sequences.

Version 1.0.0, September 11, 2014
    * Updated to work with MySQL Workbench 6.x.
    * Updated author email.
    * Dedicated the plugin to the public domain.

Version 0.8, December 24, 2011
    * Added functionality to open the generated dictionary in the Web
      browser.
    * Removed column sorting to respect the order given in the EER
      diagram.



.. REFERENCES
.. _MySQL Workbench: http://mysqlworkbench.org/
.. _wb-datadict-1.1.0.tar.gz: https://bitbucket.org/sirgazil/wb-datadict/downloads/wb-datadict-1.1.0.tar.gz
