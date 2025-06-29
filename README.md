# DateTime Location MCP Tool (for Claude Model Context Protocol)

This Python tool provides the current date, time, and your approximate geographic location using your public IP address. It is designed to be used as a **Model Context Protocol (MCP)** tool with Anthropic's Claude desktop app.

---

## What is MCP (Model Context Protocol)?

**MCP** is a protocol introduced by Anthropic to allow Claude and other AI models to interact with external tools and scripts. By implementing the MCP interface, your tool can be called by Claude to perform actions or fetch data, with communication typically happening over standard input/output (stdio).

---

## Features

- **Get Current Date and Time**  
  Returns the current system date and time in a friendly format.

- **Get My Location**  
  Uses your public IP address to estimate your city, region, country, and coordinates.

---

## Requirements

- Python 3.8 or higher
- [aiohttp](https://pypi.org/project/aiohttp/)
- [mcp](https://github.com/anthropic-ai/mcp) (Anthropic's Model Context Protocol library)

---

## Installation

1. **Download or Clone this Repository**  
   Place `dateclaude.py` in a folder on your computer.

2. **Install Dependencies**  
   Open a terminal in the project folder and run:
   ```sh
   pip install aiohttp mcp
   ```

---

## Usage

### Run as an MCP Tool

Start the tool so it listens for MCP requests from Claude:
```sh
python dateclaude.py
```
The script will wait for requests from Claude via stdio.

---

### Integrate with Claude Desktop App

1. **Open Claude Desktop App**  
   Ensure you have the latest version installed.

2. **Go to the "Tools" or "MCP Plugins" Section**  
   (This may be called "Add Tool", "Manage MCP Tools", or similar.)

3. **Add a New MCP Tool**  
   - Choose to add a local MCP tool.
   - Enter the full path to your `dateclaude.py` file, for example:
     ```
     python /path/to/dateclaude.py
     ```
   - Set the protocol/transport to `stdio` if prompted.

4. **Save and Enable the Tool**  
   Claude should now detect the following tools:
   - `get_current_datetime`
   - `get_my_location`

5. **Use the Tools in Claude**  
   You can now ask Claude to get the current date/time or your location, and it will use your local MCP tool.

---

## Troubleshooting

- **Permission Errors:**  
  Ensure Python and the required packages are installed and accessible from your terminal.

- **Network Issues:**  
  The location tool uses the free [ipinfo.io](https://ipinfo.io/) API. If you have no internet connection or a firewall blocks the request, location lookup will fail.

- **Claude App Not Detecting Tool:**  
  Double-check the path and ensure the script is running. Refer to the Claude app's documentation for MCP tool integration.

---

**Author:** Pranesh S  
**Contact:** praneshmadhan646@gmail.com
