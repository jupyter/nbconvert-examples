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
