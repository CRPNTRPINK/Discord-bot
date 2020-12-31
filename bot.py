import discord
import yandexdisk
import random
import os
import delete
import time

client = discord

delete.del_file()


class MyClient(discord.Client):

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(client))

    async def on_message(self, message):
        print(message.content)
        if message.author == client.user:
            return
        if message.content.lower() == '$update':
            yandexdisk.set_publish()
            await message.channel.send('Пачка обновилась')
        try:
            if message.content.lower() == '!webm':
                file = yandexdisk.get_random()
                with open(file, 'rb') as f:
                    picture = discord.File(f)
                await message.channel.send(file=picture)
        except Exception:
            file = yandexdisk.get_random()
            with open(file, 'rb') as f:
                picture = discord.File(f)
            await message.channel.send(file=picture)


if __name__ == '__main__':
    client = MyClient()
    client.run('NzkyODQ5NTMxNTM5NTU0MzYz.X-jsqg.V9Ur1nH-TatI12uuvUZ1R7_3rHs')
