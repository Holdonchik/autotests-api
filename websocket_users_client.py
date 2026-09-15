import asyncio
import websockets


async def client():
    """Connect to the WebSocket server, send a message and receive responses."""
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        await websocket.send(message)
        for _ in range(5):
            response = await websocket.recv()
            print(f"Server response: {response}")

asyncio.run(client())
