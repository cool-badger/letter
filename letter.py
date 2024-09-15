import discord
import asyncio
from discord.ext import tasks

# Вставьте сюда токен вашего бота
TOKEN = '"TOKEN"'

# ID канала, в который будут отправляться команды
CHANNEL_ID =

# Создание объекта intents
intents = discord.Intents.default()
intents.message_content = True  # Включает доступ к содержимому сообщений, если требуется

# Создание клиента с intents
client = discord.Client(intents=intents)

# Проверяем, что пользователь не администратор
def is_not_admin(member):
    return not any(role.permissions.administrator for role in member.roles)

# Функция, выполняющаяся каждые 1 часа
@tasks.loop(hours=1)
async def send_commands():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        # Получаем пользователя
        guild = channel.guild
        member = guild.get_member(client.user.id)
        # Проверяем, является ли пользователь администратором
        if is_not_admin(member):
            await channel.send('.collect')
            await asyncio.sleep(2)  # небольшая задержка между сообщениями
            await channel.send('.dep all')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    send_commands.start()  # Запускаем цикл отправки сообщений

# Запуск клиента
client.run(TOKEN)
