import asyncio
import time

client_reader, client_writer = await asyncio.open_connection('137.112.218.138', 2000)


try:
    client_writer.write("1")
    print("LED On")
    time.sleep(2.0)
    client_writer.write("0")
    print("LED Off")
    time.sleep(2.0)
    client_writer.write("1")
    print("LED On")
    time.sleep(2.0)
    client_writer.write("0")
    print("LED Off")

    amount_received = 0
    while amount_received < 15:
        data = await client_reader.read(100)
        amount_received += len(data)
        print("received " + str(data))

finally:
    client_writer.close()
