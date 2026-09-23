import asyncio

import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    """Receive messages from the client and send a response back."""
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сообщение пользователя: {message}"
        for i in range(1, 6):
            await websocket.send(f"{i} {response}")

async def main():
    """Start the WebSocket server and wait for it to close."""
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket server is running at wss://localhost:8765")
    await server.wait_closed()

asyncio.run(main())
