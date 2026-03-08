from fastmcp import FastMCP

mcp = FastMCP("test-remote-server")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def greet(name: str):
    return f"Hello {name}"

# Start server
if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )