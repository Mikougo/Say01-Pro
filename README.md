# 🔢 Say01 Pro

![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Bot](https://img.shields.io/badge/discord-bot-5865F2)
![Made by](https://img.shields.io/badge/made%20by-Mikougo-orange)

A simple yet powerful Discord bot that converts text into binary and decodes binary back into readable text.

---

## ✨ Features

* 🔤 Encode text into binary (UTF-8)
* 🔢 Decode binary back into text
* ⚡ Fast and lightweight
* 🛡️ Input validation for safe decoding
* 🤖 Easy-to-use commands

---

## 🧪 Example Usage

```text
!encode yobru
→ 01111001 01101111 01100010 01110010 01110101

!decode 01111001 01101111 01100010 01110010 01110101
→ yobru
```

---

## 📁 Project Structure

```text
.
├── base.py
├── requirements.txt
├── .gitignore
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

3. Set your bot token:

* Create a `.env` file (for local use only)

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

Set your environment variable:

```text
DISCORD_TOKEN=your_bot_token_here
```

---

## ⚠️ Important Notes

* Do **NOT** share your bot token
* Do **NOT** upload your `.env` file
* Ensure binary input is in 8-bit chunks (e.g. `01001000`)

---

## 🧠 Future Ideas

* Hexadecimal encoding (`!hex`)
* Base64 support
* Auto-detect encode/decode
* Message formatting improvements
* Fun “secret message” mode 😏

---

## 👨‍💻 Author

Made by **Mikougo**

---

## ⭐ Final Note

A simple idea turned into a clean and useful utility bot.
Perfect for learning encoding, decoding, and command handling 🚀
