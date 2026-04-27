"""BabelDOC - A document translation and processing library.

This package provides tools for translating and processing documents
using various AI-powered backends.

Personal fork notes:
- Forked from funstory-ai/BabelDOC for personal use and experimentation
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("babeldoc")
except PackageNotFoundError:
    __version__ = "0.0.0.dev0"

__author__ = "BabelDOC Contributors"
__license__ = "AGPL-3.0"

# Upstream project: https://github.com/funstory-ai/BabelDOC
__upstream__ = "funstory-ai/BabelDOC"

__all__ = ["__version__", "__author__", "__license__", "__upstream__"]
