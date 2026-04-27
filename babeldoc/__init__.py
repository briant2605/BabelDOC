"""BabelDOC - A document translation and processing library.

This package provides tools for translating and processing documents
using various AI-powered backends.
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("babeldoc")
except PackageNotFoundError:
    __version__ = "0.0.0.dev0"

__author__ = "BabelDOC Contributors"
__license__ = "AGPL-3.0"

__all__ = ["__version__", "__author__", "__license__"]
