import asyncio
from textwrap import dedent

class ConnectionPool:
    def __init__(self):
        self.connection_pool = set()

    def send_welcome_message(self, writer):

        message = (
            "==================================================\n"
            f"Welcome {writer.nickname}!\n\n"
            f"There are {len(self.connection_pool) - 1} user(s) here beside you\n\n"
            "Help:\n"
            "- Type anything to chat\n"
            "- /list will list all the connected users\n"
            "- /quit will disconnect you\n"
            "=================================================="
        )
        writer.write(f"{message}\n".encode())


    def broadcast(self, writer, message):
        for user in self.connection_pool:
            if user != writer:
                user.write(f"{message}\n".encode())

    def broadcast_user_join(self, writer):
        self.broadcast(writer, f"*** {writer.nickname} has joined the chat ***")

    def broadcast_user_quit(self, writer):
        self.broadcast(writer, f"*** {writer.nickname} has left the chat ***")

    def broadcast_new_message(self, writer, message):
        self.broadcast(writer, f"[{writer.nickname}]: {message}")

    def list_users(self, writer):
        message = "===\nCurrently connected users:"
        for user in self.connection_pool:
            if user == writer:
                message += f"\n - {user.nickname} (you)"
            else:
                message += f"\n - {user.nickname}"
        message += "\n==="
        writer.write(f"{message}\n".encode())

    def add_new_user(self, writer):
        self.connection_pool.add(writer)

    def remove_user(self, writer):
        self.connection_pool.remove(writer)


async def handle_connection(reader, writer):
    writer.write("> Choose your nickname: ".encode())
    await writer.drain()

    try:
        nickname_data = await reader.readuntil(b"\n")
    except asyncio.IncompleteReadError:
        writer.close()
        await writer.wait_closed()
        return

    writer.nickname = nickname_data.decode().strip()
    connection_pool.add_new_user(writer)
    connection_pool.send_welcome_message(writer)
    await writer.drain()

    connection_pool.broadcast_user_join(writer)

    while True:
        try:
            data = await reader.readuntil(b"\n")
        except asyncio.IncompleteReadError:
            connection_pool.broadcast_user_quit(writer)
            break

        message = data.decode().strip()
        if message == "/quit":
            connection_pool.broadcast_user_quit(writer)
            break
        elif message == "/list":
            connection_pool.list_users(writer)
        else:
            connection_pool.broadcast_new_message(writer, message)

        await writer.drain()

        if writer.is_closing():
            break

    writer.close()
    await writer.wait_closed()
    connection_pool.remove_user(writer)


async def main():
    server = await asyncio.start_server(handle_connection, "0.0.0.0", 8888)
    print("Chat server running on port 8888...")
    async with server:
        await server.serve_forever()

connection_pool = ConnectionPool()

asyncio.run(main())
