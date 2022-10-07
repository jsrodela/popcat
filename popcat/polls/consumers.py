import asyncio
import json
import time

import threading
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

ROOM_GROUP_NAME = 'popcat'
LUCKY = {
    '10': 'SECRET',
    '100': 'HELLO'
}

lucky_numbers = []
for key in LUCKY.keys():
    lucky_numbers.append(int(key))

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
        await self.count(event={'count': str(count)})

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            ROOM_GROUP_NAME,
            self.channel_name
        )
        pass

    async def receive(self, text_data=None, bytes_data=None):
        if text_data == '1':
            result = add_count()
            if result != '':
                await self.win(result)
        else:
            print(text_data)

    async def count(self, event):
        await self.send(text_data=event['count'])

    async def win(self, secret):
        await self.send(text_data='W'+secret)


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


def add_count() -> str:
    global count
    result = ''

    lock.acquire()

    count += 1
    if count in lucky_numbers:
        result = LUCKY[str(count)]

    lock.release()

    return result


threading.Thread(target=send_count).start()
