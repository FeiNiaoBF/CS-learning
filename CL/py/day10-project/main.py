import logging
import sys
import requests

from telegram import (
        Update,
)
from telegram.ext import (
        filters,
        MessageHandler,
        ApplicationBuilder,
        CommandHandler,
        ContextTypes
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def main():
    bot_start()

def bot_start():
    # get TOKEN
    bot_token = get_API(0)
    application = ApplicationBuilder().token(bot_token).build()

    # setting command handler
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    # help
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    # weather
    weather_handler = CommandHandler('weather', weather)
    application.add_handler(weather_handler)

    # receives messages
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    # running bot
    application.run_polling()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    out_text = "I'm a bot, please talk to me!"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=out_text)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    out_text = "You can use the following commands: \n \
                /start   ---  Start the bot \n \
                /help    ---  Get help \n \
                /weather ---  Get weather report \n \
                "
    await context.bot.send_message(chat_id=update.effective_chat.id, text=out_text)
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    out_text = get_weather_data(get_weather())
    await context.bot.send_message(chat_id=update.effective_chat.id, text=out_text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


# Weather
def get_weather():
    api_key = get_API(1)
    city = get_API(2)
    print(api_key)
    print(city)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def get_weather_data(data):
    try:
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        return f"Today Weather: \n \
                🌡️Temperature: {temperature}°C \n \
                💧Humidity: {humidity}% \n \
                🫧Pressure: {pressure}Pa \n \
                ☀️Weather Report: {report[0]['description']}"
    except Ellipsis as e:
        return "Error: " + str(e)


def get_API(line) -> str:
    try:
        with open('TOKEN', 'r') as file:
            lines = file.readlines()
            return lines[line].strip()
    except FileNotFoundError:
        sys.exit("TOKEN file not found")





if __name__ == '__main__':
    main()
