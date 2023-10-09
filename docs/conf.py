# Project information

project = "code-to-pdf"
copyright = "2023, Victor Bonnelle"
author = "Victor Bonnelle"
release = "1.2.0"

# General configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Options for HTML output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
