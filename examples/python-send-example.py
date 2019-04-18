#!/usr/bin/env python

import asyncio
import websockets
import pathlib
import ssl

api_gateway = "{YOUR-API-ID}.execute-api.{YOUR-REGION}.amazonaws.com/prod"

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

custom_headers={
'authorization': '123456',
'tenant_id': '1337',
'customer_name': 'my customers name'
}

async def hello(uri):
    async with websockets.connect(uri, ssl=ssl_context, extra_headers=custom_headers) as websocket:
        await websocket.send("{\"message\":\"sendmessage\", \"data\":\"Hello World!\"}")

asyncio.get_event_loop().run_until_complete(
    hello(api_gateway))
