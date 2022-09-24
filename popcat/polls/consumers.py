import asyncio
import time

import threading
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

ROOM_GROUP_NAME = 'popcat'
count = 0


class PopcatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add(
            ROOM_GROUP_NAME,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            ROOM_GROUP_NAME,
            self.channel_name
        )
        pass

    async def receive(self, text_data=None, bytes_data=None):
        if text_data == '1':
            global count
            count += 1
        else:
            print(text_data)

    async def count(self, event):
        await self.send(text_data=event['count'])


def send_count():
    while True:
        asyncio.run(get_channel_layer().group_send(
            ROOM_GROUP_NAME,
            {
                'type': 'count',
                'count': str(count)
            }
        ))
        time.sleep(0.1)


threading.Thread(target=send_count).start()
