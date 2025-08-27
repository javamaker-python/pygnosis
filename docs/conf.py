import os
import sys

project = "Pygnosis"

# Ensure project sources are importable
sys.path.insert(0, os.path.abspath("../src"))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

html_theme = "sphinx_rtd_theme"
templates_path = ["_templates"]
exclude_patterns = []
html_static_path = []
