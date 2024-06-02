# -*- coding: utf-8 -*-
import asyncio
import os
import botpy
from botpy import logging
from botpy.message import Message
_log = logging.get_logger()
appid="102109988"
secret="17DJPVcjqx4BIQYgow4CLUdmv4DNXhr1"
class MyClient(botpy.Client):
    async def on_ready(self):
        print(f"开始运行机器人{self.robot.name}")
    async def on_at_message_create(self, message: Message):
        _log.info(message.author.avatar)
        if "sleep" in message.content:
            await asyncio.sleep(10)
        _log.info(message.author.username)
        await message.reply(content=f"是的，我是傻逼")


if __name__ == "__main__":
    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=appid,secret=secret)

#112.49.140.37
