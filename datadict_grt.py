# WB Datadict - MySQL Workbench plugin to generate data dictionaries.
#
# Public domain 2011 sirgazil. All rights waived.

import os
import datetime
import webbrowser

from wb import *
import grt
import mforms as gui


# CONSTANTS
# =========

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="author" content="WB Datadict">
  <meta name="description" content="[PROJECTNAME] Data Dictionary.">
  <title>[PROJECTNAME] Data Dictionary</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
  <script>
    // Highlight table corresponding to the current fragment in the URL.
    $(document).ready(function(){
      $("a").click(function() {
        var elem = $(this);
        // Remove all classes from tables.
        $("table").removeClass( "focused" )
        // Get a.href value and extract its fragment id.
        var id = elem.attr("href");
        // Highlight table using fragment id.
        $(id).addClass( "focused" );
      });
    });
  </script>
  <style type="text/css">
    a {
        text-decoration: none;
    }
    abbr {
        cursor: help;
    }
    header {
        color: #6A6A6A;
        text-align: right;
    }
    table {
        border-collapse: collapse;
        margin-bottom: 30px;
        width: 100%;
    }
    table caption {
        font-size: 120%;
        font-weight: bold;
    }
    table, td, th {
        border-color: silver;
        border-style: solid;
        border-width: 1px;
    }
    caption {
        color: black;
    }
    td, th {
        padding: 1em;
    }
    tr:hover {
        color: #333;
        background-color: #F2F2F2;
    }
    th {
        background-color: #F5F5F5;
    }
    td {
        color: #6A6A6A;
    }
    ul {
        font-style: italic;
    }
    .centered {
        text-align: center;
    }
    .field {
        color: #4C4C4C;
        font-weight: bold;
    }
    .focused {
        outline-color: aqua;
        outline-style: solid;
        outline-width: thin;
    }
  </style>
</head>

<body>
  <header>
    <h1>[PROJECTNAME]<br> Data Dictionary</h1>
    <p>
      <em>[EDITION]</em>
    </p>
    <p>
      <em>[DESCRIPTION]</em>
    </p>
  </header>

  [INDEX]

  [MAIN]
</body>
</html>
"""



# PLUGIN
# ======

ModuleInfo = DefineModule(name="WB Datadict",
                          author="sirgazil",
                          version="1.1.0")
@ModuleInfo.plugin("my.plugin.create_datadict",
                   caption="Generate HTML Data Dictionary",
                   input=[wbinputs.currentCatalog()],
                   pluginMenu="Catalog")
@ModuleInfo.export(grt.INT, grt.classes.db_Catalog)


def create_datadict(catalog):
    # Get default schema
    schema = catalog.defaultSchema

    # Get table objects and sort them alphabetically
    tables = sorted(schema.tables, key=lambda table: table.name)

    # Fill HTML template
    markup = HTML_TEMPLATE
    markup = markup.replace("[PROJECTNAME]", schema.name)
    markup = markup.replace("[DESCRIPTION]", escape(schema.comment))
    markup = markup.replace("[EDITION]", str(datetime.date.today()))
    markup = markup.replace("[INDEX]", html_index(tables))
    markup = markup.replace("[MAIN]", html_main(tables))

    # Write the HTML file to disk
    doc_path = os.path.dirname(grt.root.wb.docPath)

    dialog = gui.FileChooser(gui.SaveFile)
    dialog.set_title("Save HTML data dictionary")
    dialog.set_directory(doc_path)
    response = dialog.run_modal()
    file_path = dialog.get_path()

    if response:
        try:
            html_file = open(file_path, "w")
        except IOError:
            text = "Could not open {0}.".format(file_path)
            gui.Utilities.show_error("Error saving the file", text, "Ok",
                                       "", "")
        else:
            html_file.write(markup)
            html_file.close()

            title = "{0}'s data dictionary".format(schema.name)
            text = "The data dictionary was successfully generated."
            gui.Utilities.show_message(title, text, "Ok", "", "")

            # Open HTML file in the Web browser
            try:
                webbrowser.open_new(file_path)
            except webbrowser.Error:
                print("Warning: Could not open the data dictionary in " +
                      "the Web browser.")

    return 0



# HELPER FUNCTIONS
# ================

def column_as_html(column, table):
    """Return column as an HTML row."""
    markup = "<tr>"
    markup += "<td class='field'>{0}</td>".format(column.name)
    markup += "<td>{0}</td>".format(column.formattedType)

    # Check for Primary Key
    if table.isPrimaryKeyColumn(column):
        markup += "<td class='centered'>&#10004;</td>"
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    # Check for Foreign Key
    if table.isForeignKeyColumn(column):
        markup += "<td class='centered'><a href='#{0}'>&#10004;</a></td>".format(column.name.replace("_id", ""))
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    # Check for Not Null attribute
    if column.isNotNull == 1:
        markup += "<td class='centered'>&#10004;</td>"
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    # Check for Unique attribute
    if is_unique(column, table):
        markup += "<td class='centered'>&#10004;</td>"
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    # Check for Binary, Unsigned and Zero Fill attributes
    flags = list(column.flags)

    if flags.count("BINARY"):
        markup += "<td class='centered'>&#10004;</td>"
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    if flags.count("UNSIGNED"):
        markup += "<td class='centered'>&#10004;</td>"
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    if flags.count("ZEROFILL"):
        markup += "<td class='centered'>&#10004;</td>"
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    # Check for Auto Increment attribute
    if column.autoIncrement == 1:
        markup += "<td class='centered'>&#10004;</td>"
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    # Default value
    markup += "<td>{0}</td>".format(column.defaultValue)

    # Comment
    markup += "<td>{0}</td>".format(escape(column.comment))
    markup += "</tr>"

    return markup


def escape(text):
    """Return text as an HTML-safe sequence."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    text = text.replace("'", "&apos;")
    return text


def html_index(tables):
    """Return index of tables as HTML nav."""
    markup = "<nav>"
    markup += "<h2>Index</h2>"
    markup += "<ul>"
    for table in tables:
        markup += "<li><a href='#{0}'>{0}</a></li>".format(table.name)
    markup += "</ul></nav>"

    return markup


def html_main(tables):
    """Return the main content of the HTML document."""
    markup = "<div>"

    for table in tables:
        markup += table_as_html(table)

    markup += "</div>"

    return markup


def html_table_header():
    """Return the HTML row with header cells used in all tables."""
    markup = ("<tr>" +
              "<th>Column name</th>" +
              "<th>DataType</th>" +
              "<th><abbr title='Primary Key'>PK</abbr></th>" +
              "<th><abbr title='Foreign Key'>FK</abbr></th>" +
              "<th><abbr title='Not Null'>NN</abbr></th>" +
              "<th><abbr title='Unique'>UQ</abbr></th>" +
              "<th><abbr title='Binary'>BIN</abbr></th>" +
              "<th><abbr title='Unsigned'>UN</abbr></th>" +
              "<th><abbr title='Zero Fill'>ZF</abbr></th>" +
              "<th><abbr title='Auto Increment'>AI</abbr></th>" +
              "<th>Default</th>" +
              "<th>Comment</th>" +
              "</tr>")
    return markup


def is_unique(column, table):
    """Return true if the column is UNIQUE."""
    result = False

    for index in table.indices:
        if index.name == "{0}_UNIQUE".format(column.name):
            result = True
            break

    return result


def table_as_html(table):
    """Return table as an HTML table."""
    markup = "<table id='{0}'>".format(table.name)
    markup += "<caption>{0}</caption>".format(table.name)
    markup += "<tr><td colspan='12'>{0}</td></tr>".format(escape(table.comment))
    markup += html_table_header()

    # Format column objects in HTML
    for column in table.columns:
        markup += column_as_html(column, table)

    markup += "</table>"

    return markup
