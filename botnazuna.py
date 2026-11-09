import os
import random
import threading
import discord
from flask import Flask

# Servidor web pequeño para mantener el bot activo en Render
app = Flask('')


@app.route('/')
def home():
  return '¡Nazuna está viva y funcionando 24/7!'


def run_flask():
  app.run(host='0.0.0.0', port=8080)


# Lanzamos el servidor web en un hilo secundario
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Configuración del bot de Discord
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'¡Bot conectado con éxito como {client.user}!')


@client.event
async def on_member_join(member):
  for channel in member.guild.text_channels:
    if channel.name == '⟦☃️🌕🎄⟧𝐆𝐞𝐧𝐞𝐫𝐚𝐥-𝐍𝐢𝐠𝐡𝐭':
      await channel.send(
          f'¡Hola {member.mention}, Bienvenid@ a **{member.guild.name}**! Espero'
          ' que pases una noche inolvidable y una feliz navidad con nosotros :)'
      )
      break


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  contenido = message.content.lower().strip()
  if 'iloveme' in contenido:
    respuestas = [
        f'¡Claro que sí, {message.author.mention}! Te quiero muchísimo ❤️',
        f'No, {message.author.mention}... la verdad es que no, lo siento... 💔',
    ]
    await message.channel.send(random.choice(respuestas))


# Lee el token de forma segura desde la nube (sin exponerlo en el código)
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)
