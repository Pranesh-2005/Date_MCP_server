import aiohttp
import asyncio
from datetime import datetime
from mcp.server.fastmcp import FastMCP
import sys
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("date-mcp")

mcp = FastMCP("DateTime Location MCP")

@mcp.tool()
async def get_current_datetime() -> str:
    """Returns the current system date and time."""
    now = datetime.now()
    return f"📅 Date: {now.strftime('%Y-%m-%d')}\n🕒 Time: {now.strftime('%H:%M:%S')}"

@mcp.tool()
async def get_my_location() -> str:
    """
    Returns your public IP address and estimated geographic location (via IP).
    Uses the ipinfo.io free API.
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://ipinfo.io/json", timeout=5) as response:
                response.raise_for_status()
                data = await response.json()
                city = data.get("city", "Unknown")
                region = data.get("region", "")
                country = data.get("country", "")
                loc = data.get("loc", "")
                ip = data.get("ip", "Unknown")

                return (
                    f"🌐 Public IP: {ip}\n📍 Location: {city}, {region}, {country}\n"
                    f"🗺️ Coordinates: {loc}"
                )
    except Exception as e:
        return f"❌ Failed to get location: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")