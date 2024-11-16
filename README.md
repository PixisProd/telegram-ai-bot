# GPT Bot

A versatile and intelligent GPT bot for Telegram, developed using [Aiogram 3](https://docs.aiogram.dev/en/latest/) and powered by [FastAPI](https://fastapi.tiangolo.com/) as the server. This bot seamlessly integrates with a GPT-based [Azure Openai](https://azure.microsoft.com/en-us/products/ai-services/openai-service) neural network to deliver intelligent and context-aware conversations, with user registration and activity tracking handled via [SQLAlchemy](https://www.sqlalchemy.org/).

## Features

- **Dual Modes**: Operates as a traditional chatbot for commands or switches to a GPT-powered neural network mode for natural language conversations.
- **User Tracking and Analysis**: Keeps track of each user's questions and responses in neural network mode, offering valuable insights for further analysis.
- **Database Integration**: Automatically registers new users into the database using SQLAlchemy, ensuring a smooth and organized user management system.
- **Context-Aware Interactions**: Leverages the GPT engine to provide coherent and intelligent responses, adapting to the flow of the conversation.
- **Modular Design**: Built with maintainability in mind, the bot's architecture allows for straightforward updates and feature extensions.

## Instalation

1. **First, select the location where you want to install the bot:**
```bash
cd <your-repository-folder>
```
2. **Next, clone the repository:**
```bash
git clone https://github.com/PixisProd/telegram-weather-bot.git
```
3. **Install poetry:**
```bash
pip install poetry
```
4. **Next you need to install the dependencies:**
```bash
poetry install
```
5. **In order for Telegram to see our fastapi server on the local machine, you need to use [ngrok](https://ngrok.com/download).**

## Preparation

1. Create a telegram bot using [BotFather](https://telegram.me/BotFather) and get your bot token, or if you already have a bot, then take an existing one.

2. Then find the `config.py` file in the project and paste your bot's token into the `TELEGRAM_BOT_TOKEN` field.

3. **Open `ngrok.exe` and enter the following command:**
```bash
ngrok http <your-port>
```
4. After you see that in ngrok `Session status` is `online` and lights up green, then the tunnel is ready to work through the port you selected. **Be sure to remember the port you specified.**

5. In the left column you need to find the `Forwarding` field and copy the url that ends with `.ngrok-free.app`.

6. Open the `config.py` file and paste the url we got in the paragraph above into the `NGROK_TUNNEL_URL` field.

7. Register on [Azure Openai](https://azure.microsoft.com/en-us/products/ai-services/openai-service) and follow [instructions](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal) to get endpoint and api key.

8. Open the `config.py` file and paste your endpoint and api key in tuple called `AZURE_API`.

## Bot startup

After all these preparations, we can finally start working with our bot.

1. **Start FastAPI server:** 
```bash
poetry run uvicorn main:app --host 0.0.0.0 --port <your-port>
```
Here `your-port` is the port you specified when creating the tunnel to ngrok.

After all this, your bot is ready to work.

## Conclusion

Feel free to contribute to the project by reporting issues, suggesting features, or submitting pull requests. Your feedback and contributions are always welcome!

_Enjoy the conversation! 🎉_
