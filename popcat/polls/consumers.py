import asyncio
import json
import time

import threading
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

ROOM_GROUP_NAME = 'popcat'
LUCKY = {
    '1000': 'TSN',
    '5678': 'MTR',
    '12345': 'ABC',
    '23579': 'PRM',
    '38645': 'ANY',
    '52525': 'COE',
    '77777': 'LKY',
    '100000': 'FIN'
}

lucky_numbers = []
for key in LUCKY.keys():
    lucky_numbers.append(int(key))

count = 0
last_sent_count = 0
next_lucky_number = 0
lock = threading.Lock()


class PopcatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add(
            ROOM_GROUP_NAME,
            self.channel_name
        )
        await self.accept()
        await self.count(event={'count': str(count)})
        await self.lucky(event={})

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

    async def count(self, event):  # 현재 카운트 전송
        await self.send(text_data=event['count'])

    async def lucky(self, event):  # 다음 럭키넘버 전송
        await self.send(text_data='L' + str(next_lucky_number))

    async def win(self, secret):  #
        await self.send(text_data='W' + secret)


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
    if count == next_lucky_number:
        result = LUCKY[str(count)]
        next_lucky()

    lock.release()

    return result


def next_lucky():
    global next_lucky_number

    try:
        idx = lucky_numbers.index(next_lucky_number)
    except ValueError:
        idx = -1

    if idx + 1 < len(lucky_numbers):
        next_lucky_number = lucky_numbers[idx + 1]
    else:
        next_lucky_number = -1

    # separating as thread to use asyncio.run
    threading.Thread(target=send_lucky).start()


def send_lucky():
    asyncio.run(get_channel_layer().group_send(
        ROOM_GROUP_NAME,
        {
            'type': 'lucky'
        }
    ))


def reset_count():
    global count
    lock.acquire()
    count = 0
    lock.release()


next_lucky()
threading.Thread(target=send_count, daemon=True).start()
