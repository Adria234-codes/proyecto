import discord
import random
import os
import time
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"""Hola, soy un bot {bot.user}!""")# esta linea saluda
    await ctx.send(f'Te voy hablar un poco sobre la contaminacion')
    await ctx.send(f'La contaminación es un gran problema a nivel mundial, muchos paises sufren a diario')
    # Enviar una pregunta al usuario
    await ctx.send("Quieres consejos sobre cómo combatir la contaminación? Responde con 'sí' o 'no'.")
# Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("1. No arrojar basura en los rios")
            await ctx.send("2. Dejar de quemar basuras")   
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Quieres saber la definicion de contaminacion, responde si o no")
    response1 = await bot.wait_for('message', check=check)
    if response1:
        if response1.content in ['sí', 'si']:
            await ctx.send("Arrojar basura") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def addmultiply(ctx, left: int, right: int):
    await ctx.send(left * right)
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def joined(ctx, member: discord.Member):
     await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def Bye(ctx):
    await ctx.send(f'Chao,un gusto ser {bot.user}!')
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
@bot.command()
async def XD(ctx):
   
    await ctx.send("XD,Algo te dio risa ")
@bot.command()
async def MEMES(ctx):
    with open('imagenes/MEME.jpeg', 'rb') as f:
    
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def MEMES1(ctx):
    with open('imagenes/MEME1.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def MEMES2(ctx):
    with open('imagenes/MEME2.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def MEMES3(ctx):
    imagenes = os.listdir('imagenes')# Obtenemos la lista de archivos
    with open(f'imagenes/{random.choice(imagenes)}', 'rb') as f:  
            picture = discord.File(f)   
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")
@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)
@bot.command()
async def player(ctx,arg):
    try:
        jugadores = arg.split("",1)[0].lower()
        result = requests.get(""+jugadores)
        if result.text == "Not Found":
            await ctx.send("Jugador no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error",e)
@player.error
async def error_type(ctx,error):
    if isintance(error,command.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un jugador")
