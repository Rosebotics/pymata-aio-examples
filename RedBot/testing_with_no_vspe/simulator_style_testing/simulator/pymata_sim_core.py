import asyncio

from pymata_socket import PymataSocket


class SimCore():
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.pysock = PymataSocket('127.0.0.1', 8888, self.loop)
        self.r_buffer = ""

    async def write(self, data):
        await self.pysock.write(data)

    async def read(self):
        reply = await self.pysock.read(self.r_buffer)
        return reply

    async def startup(self):
        await self.pysock.start()

    def startupX(self):
        loop.run_until_complete(sc.startup())

    def writeX(self, data):
        loop.run_until_complete(sc.write(data))

    def readX(self):
        x_buffer = loop.run_until_complete(sc.read())
        return x_buffer

my_buffer = ""
sc = SimCore()
loop = asyncio.get_event_loop()
sc.startupX()
sc.writeX('Hello')
data = sc.readX()
print(data)
