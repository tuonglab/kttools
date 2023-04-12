# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "kttools"
copyright = "2023, Kelvin Tuong"
author = "Kelvin Tuong"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_theme",
    "nbsphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "recommonmark",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

nitpicky = True  # Warn about broken links
needs_sphinx = "2.0"  # Nicer param docs
nitpick_ignore = [("py:class", "type")]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# html_logo = "notebooks/logo.png"
# html_favicon = "notebooks/logo.png"

# html_theme_options = {"logo_only": True}

master_doc = "index"

napoleon_use_param = False
autodoc_member_order = "bysource"
autosummary_generate = True
