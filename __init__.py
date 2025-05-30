"""Top-level package for friends_the_gathering."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """Daniel Ribeirinha-Braga"""
__email__ = "dmrbraga@gmail.com"
__version__ = "0.0.1"

from .src.friends_the_gathering.nodes import NODE_CLASS_MAPPINGS
from .src.friends_the_gathering.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
