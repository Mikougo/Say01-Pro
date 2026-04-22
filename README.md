# 🔢 Say01 Pro

![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Bot](https://img.shields.io/badge/discord-bot-5865F2)
![Made by](https://img.shields.io/badge/made%20by-Mikougo-orange)

A modern Discord utility bot focused on encoding and decoding text in multiple formats, including binary, hexadecimal, Base64, and Morse code.

---

## ✨ Features

* 🔤 Binary encode and decode
* 🧮 Hex encode and decode
* 📦 Base64 encode and decode
* 📡 Morse code encode and decode
* 🤖 `/auto` command to detect and decode supported formats automatically
* ⚡ Built with modern slash commands using latest `discord.py`

---

## 🧪 Commands

```text
/binencode
/bindecode
/hexencode
/hexdecode
/b64encode
/b64decode
/morseencode
/morsedecode
/auto
```

---

## 🧪 Example Usage

```text
/binencode text:hello
→ 01101000 01100101 01101100 01101100 01101111

/bindecode binary:01101000 01100101 01101100 01101100 01101111
→ hello

/hexencode text:hello
→ 68656c6c6f

/b64encode text:hello
→ aGVsbG8=

/morseencode text:hello world
→ .... . .-.. .-.. --- / .-- --- .-. .-.. -..

/auto data:68656c6c6f
→ Detected hex -> hello
```

---

## 📁 Project Structure

```text
.
├── base.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Say01-Pro.git
cd Say01-Pro
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file for local testing:

```env
DISCORD_TOKEN=your_bot_token_here
```

4. Run the bot:

```bash
python base.py
```

---

## 🚀 Deployment

This bot can be deployed on:

* Railway
* Render
* VPS

Set the environment variable:

```text
DISCORD_TOKEN=your_bot_token_here
```

---

## ⚠️ Important Notes

* Do **NOT** share your bot token
* Do **NOT** upload your `.env` file
* Slash commands may take a short moment to appear after deployment
* Morse code uses `/` between words

---

## 🧠 Supported Formats

### Binary

Uses 8-bit UTF-8 byte chunks.

Example:

```text
01001000 01101001
```

### Hex

Uses standard hexadecimal byte encoding.

Example:

```text
4869
```

### Base64

Uses standard Base64 text encoding.

Example:

```text
SGk=
```

### Morse Code

Uses spaces between letters and `/` between words.

Example:

```text
.... .. / - .... . .-. .
```

---

## 👨‍💻 Author

Made by **Mikougo**

---

## ⭐ Final Note

Say01 Pro started as a simple binary bot and evolved into a multi-format encoding utility with slash commands, auto-detection, and cleaner command design.
