"""
Math Operations MCP Server
GitHub: https://github.com/Soroush77/simple-mcp-server
"""
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, CallToolResult
import json

# Create server instance
app = Server("math-operations")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """Return available mathematical tools"""
    return [
        Tool(
            name="add",
            description="Add two numbers together",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    }
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="multiply",
            description="Multiply two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"}
                },
                "required": ["x", "y"]
            }
        ),
        Tool(
            name="calculate_percentage",
            description="Calculate percentage of a number",
            inputSchema={
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "The base value"
                    },
                    "percentage": {
                        "type": "number",
                        "description": "The percentage to calculate"
                    }
                },
                "required": ["value", "percentage"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> CallToolResult:
    """Execute the requested tool"""
    try:
        if name == "add":
            result = arguments["a"] + arguments["b"]
            operation = f"{arguments['a']} + {arguments['b']} = {result}"

        elif name == "multiply":
            result = arguments["x"] * arguments["y"]
            operation = f"{arguments['x']} × {arguments['y']} = {result}"

        elif name == "calculate_percentage":
            result = (arguments["value"] * arguments["percentage"]) / 100
            operation = f"{arguments['percentage']}% of {arguments['value']} = {result}"

        else:
            raise ValueError(f"Unknown tool: {name}")

        return CallToolResult(
            content=[TextContent(
                type="text",
                text=operation
            )]
        )

    except Exception as e:
        return CallToolResult(
            content=[TextContent(
                type="text",
                text=f"Error: {str(e)}"
            )]
        )


async def main():
    """Run the MCP server with stdio transport"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())