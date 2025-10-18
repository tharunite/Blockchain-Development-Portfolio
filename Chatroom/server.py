import asyncio
async def handle_connections(reader,writer):
    writer.write("Hello new user, write something... \n".encode())
    data= await reader.readuntil(b'\n')
    writer.write('You sent: '.encode()+data)
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_connections,'0.0.0.0',8888)
    print('Server is booted')
    async with server:
        await server.serve_forever()
asyncio.run(main())
