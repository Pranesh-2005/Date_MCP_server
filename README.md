# DateTime Location MCP

A simple Python tool that provides the current date, time, and your approximate geographic location using your public IP address. This project exposes these features as tools for use in the Claude desktop app via the MCP (Modular Command Platform) protocol.

## Features

- **Get Current Date and Time**  
  Returns the current system date and time in a friendly format.

- **Get My Location**  
  Uses your public IP address to estimate your city, region, country, and coordinates.

## Requirements

- Python 3.8 or higher
- [aiohttp](https://pypi.org/project/aiohttp/)
- [mcp](https://github.com/microsoft/mcp) (Modular Command Platform)

## Installation

1. **Clone this repository or copy the files**  
   Place `dateclaude.py` in a folder on your computer.

2. **Install dependencies**  
   Open a terminal in the project folder and run:
   ```sh
   pip install aiohttp mcp
   ```

## Usage

### Run as a Standalone MCP Server

You can run the tool as an MCP server that communicates over standard input/output (stdio):

```sh
python dateclaude.py
```

You should see no output unless there is an error. The server is now ready to accept MCP requests.

### Add to Claude Desktop App

1. **Open Claude Desktop App**  
   Make sure you have the latest version installed.

2. **Go to the "Tools" or "Plugins" Section**  
   (This may be called "Add Tools", "Manage Plugins", or similar.)

3. **Add a New Local Tool**  
   - Choose the option to add a local MCP tool.
   - When prompted for the command or script, enter the full path to your `dateclaude.py` file, for example:
     ```
     python /path/to/dateclaude.py
     ```
   - Set the transport/protocol to `stdio` if required.

4. **Save and Enable the Tool**  
   The Claude app should now detect the two tools:
   - `get_current_datetime`
   - `get_my_location`

5. **Use the Tools in Claude**  
   You can now ask Claude to get the current date/time or your location, and it will use your local MCP tool.

## Troubleshooting

- **Permission Errors:**  
  Make sure Python and the required packages are installed and accessible from your terminal.

- **Network Issues:**  
  The location tool uses the free [ipinfo.io](https://ipinfo.io/) API. If you have no internet connection or a firewall blocks the request, location lookup will fail.

- **Claude App Not Detecting Tool:**  
  Double-check the path and ensure the script is running. Check the Claude app's documentation for MCP tool integration.


---

**Author:** Pranesh S  
**Contact:** praneshmadhan646@gmail.com
