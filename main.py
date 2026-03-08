"""
Test MCP Server
A simple MCP server with tools, resources, and prompts.
"""

from fastmcp import FastMCP
from datetime import datetime

# Create MCP server
mcp = FastMCP("test-remote-server")


# -----------------------
# TOOLS
# -----------------------

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together
    """
    return a + b


@mcp.tool()
def current_time() -> str:
    """
    Get current server time
    """
    return datetime.now().isoformat()


@mcp.tool()
def greet(name: str) -> str:
    """
    Greet a user
    """
    return f"Hello {name}! Welcome to the MCP test server."


# -----------------------
# RESOURCES
# -----------------------

@mcp.resource("info://server")
def server_info() -> str:
    """
    Information about this MCP server
    """
    return """
Test MCP Server
Version: 1.0
Author: Kunal
Purpose: Demo MCP server for testing tools and resources
"""


@mcp.resource("data://sample")
def sample_data() -> str:
    """
    Return sample dataset
    """
    return """
Sample Data:
1,Apple
2,Banana
3,Orange
"""


# -----------------------
# PROMPTS
# -----------------------

@mcp.prompt()
def math_prompt() -> str:
    """
    Prompt template for math help
    """
    return "You are a helpful math assistant. Solve the user's math problems clearly."


@mcp.prompt()
def greeting_prompt() -> str:
    """
    Prompt template for greeting users
    """
    return "You are a friendly assistant. Greet the user politely."


# -----------------------
# MAIN
# -----------------------

def main():
    print("🚀 Starting Test MCP Server...")
    mcp.run(
        transport="http",
        host="localhost",
        port=8000
    )


if __name__ == "__main__":
    main()