import os

from dotenv import load_dotenv
from telegram import Update, ForceReply
from telegram.ext import Updater


def start(update: Update):
    """Send a message when the command /start is used."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def echo(update: Update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def start_dialog_flow_bot(telegram_token):
    updater = Updater(telegram_token)


def main():
    """The main logic for starting dialog flow bot."""
    load_dotenv()
    telegram_token = os.getenv('TG_TOKEN')

    start_dialog_flow_bot(telegram_token)


if __name__ == '__main__':
    main()
