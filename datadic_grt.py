# WB DataDic is a plugin for MySQL Workbench to generate data dictionaries.
# Copyright (C) 2011  Luis Felipe Lopez Acevedo <introsmedia@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
from datetime import date

from wb import *
import grt

ModuleInfo = DefineModule(name="Datadic",
                          author="Luis Felipe Lopez Acevedo",
                          version="0.2")
@ModuleInfo.plugin("my.plugin.create_datadic",
                   caption="Generate HTML Data Dictionary",
                   input=[wbinputs.currentCatalog()],
                   pluginMenu="Catalog")
@ModuleInfo.export(grt.INT, grt.classes.db_Catalog)

def create_datadic(catalog):
    # Get table objects from the model
    #
    schema = catalog.defaultSchema
    tables = schema.tables
    
    # Organize table objects alphabeticaly
    #
    sorted_tables = sorted(tables, key=lambda table: table.name)
    
    # Add header to the markup and replace header variables
    #
    markup = get_header()
    markup = markup.replace("[PROJECTNAME]", schema.name)
    markup = markup.replace("[EDITION]", str(date.today()))
    
    # Add alphabetic index links
    #
    markup += "<h2>Alphabetic Index</h2>\n"
    markup += "<ul>\n"
    for table in sorted_tables:
        markup += "<li><a href='#{0}'>{0}</a></li>\n".format(table.name)
    markup += "</ul>\n"
    
    # Format table objects in HTML.
    #
    for table in sorted_tables:
        markup += "<table id='{0}'>\n".format(table.name)
        markup += "<caption>{0}</caption>\n".format(table.name)
        markup += "<tr><td colspan='10'>{0}</td></tr>\n".format(table.comment)
        markup += get_colnames()
        sorted_columns = sorted(table.columns,
                                key=lambda column: column.name)
        for column in sorted_columns:
            markup += "<tr>\n"
            markup += "    <td>{0}</td>\n".format(column.name)
            markup += "    <td>{0}</td>\n".format(column.formattedType)

            # Checks for Primary Key
            if table.isPrimaryKeyColumn(column):
                markup += "    <td>&#10004;</td>\n"
            else:
                markup += "    <td>&nbsp;</td>\n"
            
            # Checks for Not Null attribute
            if column.isNotNull == 1:
                markup += "    <td>&#10004;</td>\n"
            else:
                markup += "    <td>&nbsp;</td>\n"
            
            # TODO Checks for Unique attribute
            if False:
                markup += "    <td>&#10004;</td>\n"
            else:
                markup += "    <td>&nbsp;</td>\n"
            
            # Checks for Binary, Unsigned and Zero Fill attributes
            flags = list(column.flags)
            
            if flags.count("BINARY"):
                markup += "    <td>&#10004;</td>\n"
            else:
                markup += "    <td>&nbsp;</td>\n"
            
            if flags.count("UNSIGNED"):
                markup += "    <td>&#10004;</td>\n"
            else:
                markup += "    <td>&nbsp;</td>\n"
            
            if flags.count("ZEROFILL"):
                markup += "    <td>&#10004;</td>\n"
            else:
                markup += "    <td>&nbsp;</td>\n"
            
            # Checks for Auto Increment attribute
            if column.autoIncrement == 1:
                markup += "    <td>&#10004;</td>\n"
            else:
                markup += "    <td class='attr'>&nbsp;</td>\n"
                
            
            markup += "    <td>{0}</td>\n".format(column.comment)
            markup += "</tr>\n"
    
    markup += "</table>\n"
    
    # Add footer to the markup
    #
    markup += get_footer()
    
    # Write the HTML file to disk
    #
    dir_path = os.environ["HOME"] + "/{0}-datadic".format(schema.name)
    file_path = (dir_path + "/index.html")
    
    if os.path.exists(dir_path) != True:
        os.mkdir(dir_path)
    
    html_file = open(file_path, "w")
    html_file.write(markup)
    html_file.close()
    
    print("DONE: Data Dictionary saved in {0}".format(dir_path))
    
    return 0


def get_header():
    """Returns the top part of the HTML document."""
    header = """<!DOCTYPE html>\n\
<html>\n\
<head>\n\
    <meta charset="UTF-8" />\n\
    <meta name="author" content="WB DataDic" />\n\
    <meta name="description" content="[PROJECTNAME] Data Dictionary." />\n\
    <title>[PROJECTNAME] Data Dictionary</title>\n\
    <style type="text/css">\n\
    table{\n\
        width: 100%;\n\
        margin-bottom: 30px;\n\
    }\n\
    abbr{\n\
        cursor: help;\n\
    }\n\
    table, td, th{\n\
        border-style: solid;\n\
        border-width: 1px;\n\
    }\n\
    table caption{\n\
        font-size: 120%;\n\
        font-weight: bold;\n\
    }\n\
    caption{\n\
        color: black;\n\
    }\n\
    td, th{\n\
        border-color: silver;\n\
    }\n\
    tr:hover{\n\
        color: #333;\n\
        background-color: #F2F2F2;\n\
    }\n\
    th{\n\
        background-color: silver;\n\
    }\n\
    td{\n\
        color: gray;\n\
    }\n\
    ul{\n\
        font-style: italic;\n\
    }\n\
    #title-sect{\n\
        color: gray;\n\
        text-align: right;\n\
    }\n\
    </style>\n\
</head>\n\
<body>\n\
<div id="title-sect">\n\
<h1>[PROJECTNAME] Data Dictionay</h1>\n\
<p>\n\
<em>[EDITION]</em>\n\
</p>\n\
</div>\n\
"""
    return header


def get_colnames():
    """Returns the default column names for each table."""
    colnames = ("<tr>\n" +
                "    <th>Attribute</th>\n" +
                "    <th>Data Type</th>\n" +
                "    <th><abbr title='Primary Key'>PK</abbr></th>\n" +
                "    <th><abbr title='Not Null'>NN</abbr></th>\n" +
                "    <th><abbr title='Unique'>UQ</abbr></th>\n" +
                "    <th><abbr title='Binary'>BIN</abbr></th>\n" +
                "    <th><abbr title='Unsigned'>UN</abbr></th>\n" +
                "    <th><abbr title='Zero Fill'>ZF</abbr></th>\n" +
                "    <th><abbr title='Auto Increment'>AI</abbr></th>\n" +
                "    <th>Description</th>\n" +
                "</tr>\n")
    return colnames


def get_footer():
    """Returns the bottom part of the HTML document."""
    return "</body>\n</html>"
