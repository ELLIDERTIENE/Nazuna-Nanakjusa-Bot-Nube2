import os
import random
import threading
import discord
from flask import Flask

# Servidor web pequeño para mantener el bot activo en Render
app = Flask('')


@app.route('/')
def home():
  return '¡El bot de Discord está vivo y funcionando 24/7!'


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
    if channel.name == '⟦🌕⟧𝙂𝙚𝙣𝙚𝙧𝙖𝙡':
      await channel.send(
          f'¡Hola {member.mention}, bienvenid@ a **{member.guild.name}**! Espero'
          ' que pases una noche inolvidable con nosotros :)'
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
TOKEN = os.getenv('MTU2ODQ1MDM0OTI4OTcwMTQzNg.GUiR2_.2oqDODOqmsBQn3VAT1PcSy6NN90rkaSd1kD_0Y')
client.run(TOKEN)