# Workbench Data Dictionary

A plugin for MySQL Workbench Community Edition 6.x. This plugin allows
you to generate an HTML data dictionary from a selected schema.

## Installation

1. Clone this repo to a working directory on your machine.
2. Open MySQL Workbench and select **Scripting** -> **Install Plugin/Module...**
3. Select the `datadict_grt.py` script, click OK, and restart Workbench
4. Open Workbench and a Model with an EED - Enhanced Entity Diagram
5. Select **File** -> **Export** -> **Export as PNG** and save to an output folder with `schema_erd.png` as filename
6. Select **Tools** -> **Catalog** -> **Generate HTML Data Dictionary**
7. Save file as `mySchemaName.html` in same output folder as `schema_erd.png`
8. Copy the `legend.png` image to output folder
9. Open the file with your web browser and enjoy ;)

#### Many thanks to the original author and contributors to this project.

The original mercurial repository can be found here with additional documentation:

License: Public domain 2011 [sirgazil](https://sirgazil.bitbucket.io/). All rights waived.

Website: https://sirgazil.bitbucket.io/en/artifacts/wb-datadict/

Manual: [English](https://sirgazil.bitbucket.io/en/doc/wb-datadict/1.1.0/manual/), [Español](https://sirgazil.bitbucket.io/es/doc/wb-datadict/1.1.0/manual/)
