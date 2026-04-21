import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")


def text_to_binary(text):
    return " ".join(format(byte, "08b") for byte in text.encode("utf-8"))


def binary_to_text(binary_string):
    parts = binary_string.split()
    data = bytearray()

    for part in parts:
        if len(part) != 8 or any(bit not in "01" for bit in part):
            raise ValueError("Invalid binary input. Use 8-bit chunks like: 01001000 01101001")
        data.append(int(part, 2))

    return data.decode("utf-8")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="speaking in 01"))


@bot.command()
async def encode(ctx, *, text):
    binary = text_to_binary(text)
    await ctx.send(binary)


@bot.command()
async def decode(ctx, *, binary):
    try:
        text = binary_to_text(binary)
        await ctx.send(text)
    except ValueError as e:
        await ctx.send(str(e))
    except UnicodeDecodeError:
        await ctx.send("That binary is valid bytes, but not valid UTF-8 text.")


bot.run(TOKEN)
