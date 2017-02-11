[![PyPI version](https://badge.fury.io/py/matlab_nbconvert.svg)](https://badge.fury.io/py/matlab_nbconvert)

# Example of a pypi package that creates a new exporter for nbconvert

This is an exporter for `nbconvert` that turns matlab-notebooks into neatly formatted matlab (`.m`) files. The new exporter is included as an "entry point" so can be used directly by nbconvert.

The files required are [described here](http://nbconvert.readthedocs.io/en/latest/external_exporters.html), and your folder structure should look like this:

```
mypackage
├── LICENSE.md
├── setup.py
└── mypackage
    ├── __init__.py
    └── templates
        └── test_template.tpl
```

### Defining your custom exporter in `__init__.py`

Within `__init__.py`, you can define your custom exporter, which can use a custom template:

```
# file __init__.py
from traitlets import default
from nbconvert.exporters.templateexporter import TemplateExporter
import os.path

"""Matlab script Exporter class"""

# Copyright (c) Jan Freyberg
# Distributed under the terms of the MIT License.


class MatlabExporter(TemplateExporter):
    """
    Exports a Python code file.
    """

    @default('file_extension')
    def _file_extension_default(self):
        return '.m'

    template_path = ['.', os.path.join(os.path.dirname(__file__),
                                       "templates")]

    @default('template_file')
    def _template_file_default(self):
        return 'matlab'
```

### Defining your custom template_file

You can include your custom template file, just like when you create a custom template file locally, by including it inside the `templates` folder. In this case, all I do is add a `%%` at the start of each cell, and use `%` instead of `#` as the comment line indicator.

```
{%- extends 'null.tpl' -%}

{% block header %}
%% Exported from Jupyter Notebook
{% endblock header %}

{% block in_prompt %}
%% Cell[{{ cell.execution_count if cell.execution_count else ' ' }}]:
{% endblock in_prompt %}

{% block input %}
{{ cell.source }}
{% endblock input %}

{% block markdowncell scoped %}
%%
{{ cell.source | comment_lines(prefix='% ') }}
{% endblock markdowncell %}
```

### Making sure your package installs properly

Guidelines for what to include in your `setup.py` file can be found elsewhere, [for example here](https://github.com/pypa/sampleproject).

The important things for making an nbconvert exporter are:

1. Make sure your templates get shipped by including `package_data={'': ['templates/*.tpl']}` in your `setup(...)` function.
2. Make sure you create an entrypoint for your package by including `entry_points={'nbconvert.exporters': ['matlab = matlab_nbconvert:MatlabExporter']}` in your `setup(...)` function.


### Installation and Usage

If your `setup.py` function is correct and you follow the rest of the requirements for publishing on pypi, people will be able to install your custom nbconverter exporter by typing `pip install matlab_nbconvert`

Usage: type `jupyter nbconvert --to matlab 'notebookname.ipynb'`, inserting your filename as needed.

All cells in the resulting `.m` files are delimited by the matlab sectioning `%%`, which means you can run your code as sections in Matlab like you would in jupyter. All code cells have the heading "Cell [X]", where X is the output number present in your notebook.
