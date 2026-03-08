from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("test-remote-server")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def current_time() -> str:
    return datetime.now().isoformat()

@mcp.tool()
def greet(name: str) -> str:
    return f"Hello {name}"

# 👇 IMPORTANT for cloud
app = mcp

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )