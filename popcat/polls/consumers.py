import asyncio
import time

import threading
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

ROOM_GROUP_NAME = 'popcat'
count = 0
last_sent_count = 0
lock = threading.Lock()


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
            add_count()
        else:
            print(text_data)

    async def count(self, event):
        await self.send(text_data=event['count'])


def send_count():
    global last_sent_count
    while True:
        if last_sent_count != count:
            asyncio.run(get_channel_layer().group_send(
                ROOM_GROUP_NAME,
                {
                    'type': 'count',
                    'count': str(count)
                }
            ))
            last_sent_count = count
        time.sleep(0.1)


def add_count() -> None:
    global count
    lock.acquire()
    count += 1
    lock.release()


threading.Thread(target=send_count).start()
