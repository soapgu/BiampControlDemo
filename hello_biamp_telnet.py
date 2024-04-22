import asyncio, telnetlib3

async def shell(reader, writer):
    while True:
        # read stream until '?' mark is found
        outp = await reader.read(1024)
        if not outp:
            # End of File
            break
        elif 'Welcome' in outp:
            
            writer.write('DEVICE get serialNumber\n')

        # display all server output
        print(f'outp:{outp}', flush=True)

    # EOF
    print()

loop = asyncio.get_event_loop()
coro = telnetlib3.open_connection('172.16.13.52', 23, shell=shell)
reader, writer = loop.run_until_complete(coro)
loop.run_until_complete(writer.protocol.waiter_closed)