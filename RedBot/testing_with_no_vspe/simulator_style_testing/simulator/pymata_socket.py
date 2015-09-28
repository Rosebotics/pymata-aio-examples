import asyncio

# noinspection PyStatementEffect,PyUnresolvedReferences,PyUnresolvedReferences
class PymataSocket:
    def __init__(self, ip_address, port, loop):
        self.ip_address = ip_address
        self.port = port
        self.loop = loop

    async def start(self):
        self.reader, self.writer =  await asyncio.open_connection(self.ip_address, self.port, loop=self.loop)

    async def write(self, data):
        print('socket_write')
        self.writer.write(data.encode())
        await self.writer.drain()

    async def read(self, buffer):
        buffer = await self.reader.read(100)
        print('client received')
        #print(data)
        return(buffer)

