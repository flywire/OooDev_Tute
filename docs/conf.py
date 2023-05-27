# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Tute'
copyright = '2023, flywire'
author = 'flywire'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx_rtd_dark_mode",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
#     "sphinx_toolbox.collapse",
#     "sphinx_toolbox.more_autodoc.autonamedtuple",
#     "sphinx_toolbox.more_autodoc.typevars",
#     "sphinx_toolbox.more_autodoc.autoprotocol",
#     "sphinx_toolbox.more_autodoc.overloads",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
#     "sphinx.ext.extlinks",
#     "sphinx.ext.intersphinx",
#     "sphinx_autodoc_typehints",
    "sphinx_tabs.tabs",
#     "sphinx_design",
#     "sphinxcontrib.spelling",
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = []

# copybutton_exclude = '.linenos, .gp, .go'
copybutton_prompt_text = r">>> ?|\.\.\. ?|\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'
numfig = True
