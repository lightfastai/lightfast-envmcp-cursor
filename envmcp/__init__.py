"""
envmcp - A lightweight way to use environment variables in your Cursor MCP
server definitions.
"""

from .core import find_env_file, load_env_mcp, parse_env_file
from .executor import execute_command


__version__ = "0.1.0"
__all__ = ["execute_command", "find_env_file", "load_env_mcp", "parse_env_file"]
