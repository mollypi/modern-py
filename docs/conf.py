"""Sphinx configuration."""
project = "Modern Py"
author = "Molly Depew"
copyright = "2023, Molly Depew"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
