import os
import base64
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    ":": "---...",
    ";": "-.-.-.",
    "'": ".----.",
    '"': ".-..-.",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    "=": "-...-",
    "+": ".-.-.",
    "_": "..--.-",
    "@": ".--.-.",
    "$": "...-..-",
}

REVERSE_MORSE_CODE = {value: key for key, value in MORSE_CODE.items()}


def text_to_binary(text: str) -> str:
    return " ".join(format(byte, "08b") for byte in text.encode("utf-8"))


def binary_to_text(binary_string: str) -> str:
    parts = binary_string.strip().split()
    data = bytearray()

    for part in parts:
        if len(part) != 8 or any(bit not in "01" for bit in part):
            raise ValueError(
                "Invalid binary input. Use 8-bit chunks like: 01001000 01101001"
            )
        data.append(int(part, 2))

    return data.decode("utf-8")


def text_to_hex(text: str) -> str:
    return text.encode("utf-8").hex()


def hex_to_text(hex_string: str) -> str:
    cleaned = hex_string.strip().replace(" ", "")
    return bytes.fromhex(cleaned).decode("utf-8")


def text_to_base64(text: str) -> str:
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


def base64_to_text(base64_string: str) -> str:
    cleaned = base64_string.strip()
    return base64.b64decode(cleaned, validate=True).decode("utf-8")


def text_to_morse(text: str) -> str:
    words = text.upper().split()
    encoded_words = []

    for word in words:
        encoded_letters = []
        for char in word:
            if char not in MORSE_CODE:
                raise ValueError(f"Unsupported character for Morse code: {char}")
            encoded_letters.append(MORSE_CODE[char])
        encoded_words.append(" ".join(encoded_letters))

    return " / ".join(encoded_words)


def morse_to_text(morse_string: str) -> str:
    words = morse_string.strip().split(" / ")
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_letters = []

        for symbol in letters:
            if symbol not in REVERSE_MORSE_CODE:
                raise ValueError(f"Invalid Morse code symbol: {symbol}")
            decoded_letters.append(REVERSE_MORSE_CODE[symbol])

        decoded_words.append("".join(decoded_letters))

    return " ".join(decoded_words)


def looks_like_binary(data: str) -> bool:
    parts = data.strip().split()
    return bool(parts) and all(
        len(part) == 8 and all(bit in "01" for bit in part)
        for part in parts
    )


def looks_like_hex(data: str) -> bool:
    cleaned = data.strip().replace(" ", "")
    if not cleaned or len(cleaned) % 2 != 0:
        return False
    return all(char in "0123456789abcdefABCDEF" for char in cleaned)


def looks_like_base64(data: str) -> bool:
    cleaned = data.strip()
    if not cleaned:
        return False

    allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    if any(char not in allowed for char in cleaned):
        return False

    try:
        base64.b64decode(cleaned, validate=True)
        return True
    except Exception:
        return False


def looks_like_morse(data: str) -> bool:
    cleaned = data.strip()
    if not cleaned:
        return False
    allowed = {".", "-", "/", " "}
    return all(char in allowed for char in cleaned)


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Logged in as {bot.user}")
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Sync failed: {e}")

    await bot.change_presence(activity=discord.Game(name="speaking in 01"))


@bot.tree.command(name="binencode", description="Convert text into binary")
@app_commands.describe(text="Text to convert into binary")
async def binencode(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(f"`{text_to_binary(text)}`")


@bot.tree.command(name="bindecode", description="Convert binary into text")
@app_commands.describe(binary="Binary string in 8-bit chunks")
async def bindecode(interaction: discord.Interaction, binary: str):
    try:
        await interaction.response.send_message(f"`{binary_to_text(binary)}`")
    except ValueError as e:
        await interaction.response.send_message(str(e), ephemeral=True)
    except UnicodeDecodeError:
        await interaction.response.send_message(
            "That binary is valid bytes, but not valid UTF-8 text.",
            ephemeral=True,
        )


@bot.tree.command(name="hexencode", description="Convert text into hexadecimal")
@app_commands.describe(text="Text to convert into hex")
async def hexencode(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(f"`{text_to_hex(text)}`")


@bot.tree.command(name="hexdecode", description="Convert hexadecimal into text")
@app_commands.describe(hex_input="Hex string to decode")
async def hexdecode(interaction: discord.Interaction, hex_input: str):
    try:
        await interaction.response.send_message(f"`{hex_to_text(hex_input)}`")
    except ValueError:
        await interaction.response.send_message(
            "Invalid hex input. Use only hexadecimal characters.",
            ephemeral=True,
        )
    except UnicodeDecodeError:
        await interaction.response.send_message(
            "That hex is valid bytes, but not valid UTF-8 text.",
            ephemeral=True,
        )


@bot.tree.command(name="b64encode", description="Convert text into Base64")
@app_commands.describe(text="Text to convert into Base64")
async def b64encode(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(f"`{text_to_base64(text)}`")


@bot.tree.command(name="b64decode", description="Convert Base64 into text")
@app_commands.describe(b64_input="Base64 string to decode")
async def b64decode(interaction: discord.Interaction, b64_input: str):
    try:
        await interaction.response.send_message(f"`{base64_to_text(b64_input)}`")
    except Exception:
        await interaction.response.send_message(
            "Invalid Base64 input or not valid UTF-8 text.",
            ephemeral=True,
        )


@bot.tree.command(name="morseencode", description="Convert text into Morse code")
@app_commands.describe(text="Text to convert into Morse code")
async def morseencode(interaction: discord.Interaction, text: str):
    try:
        await interaction.response.send_message(f"`{text_to_morse(text)}`")
    except ValueError as e:
        await interaction.response.send_message(str(e), ephemeral=True)


@bot.tree.command(name="morsedecode", description="Convert Morse code into text")
@app_commands.describe(morse_input="Morse code to decode. Use / between words")
async def morsedecode(interaction: discord.Interaction, morse_input: str):
    try:
        await interaction.response.send_message(f"`{morse_to_text(morse_input)}`")
    except ValueError as e:
        await interaction.response.send_message(str(e), ephemeral=True)


@bot.tree.command(
    name="auto",
    description="Auto-detect binary, hex, Base64, or Morse code. Otherwise encode as binary"
)
@app_commands.describe(data="Input to detect or encode")
async def auto(interaction: discord.Interaction, data: str):
    data = data.strip()

    if looks_like_binary(data):
        try:
            result = binary_to_text(data)
            await interaction.response.send_message(f"Detected **binary** -> `{result}`")
            return
        except Exception:
            pass

    if looks_like_hex(data):
        try:
            result = hex_to_text(data)
            await interaction.response.send_message(f"Detected **hex** -> `{result}`")
            return
        except Exception:
            pass

    if looks_like_base64(data):
        try:
            result = base64_to_text(data)
            await interaction.response.send_message(f"Detected **Base64** -> `{result}`")
            return
        except Exception:
            pass

    if looks_like_morse(data):
        try:
            result = morse_to_text(data)
            await interaction.response.send_message(f"Detected **Morse** -> `{result}`")
            return
        except Exception:
            pass

    await interaction.response.send_message(
        f"Didn't detect binary, hex, Base64, or Morse, so I encoded it as binary:\n`{text_to_binary(data)}`"
    )


if not TOKEN:
    raise ValueError("DISCORD_TOKEN is missing.")

bot.run(TOKEN)
