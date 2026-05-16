# Math Operations MCP Server

A simple MCP server providing basic mathematical operations.

## Usage with LightLLM

1. In LightLLM UI, enter this GitHub URL:
   `https://github.com/Soroush77/simple-mcp-server`

2. Select transport type: `stdio`

3. Click "Add Server"

## Tools Available

- **add**: Add two numbers (a + b)
- **multiply**: Multiply two numbers (x × y)  
- **calculate_percentage**: Calculate percentage of a value

## Local Testing

```bash
pip install -r requirements.txt
python mcp_server.py