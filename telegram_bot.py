import os

from dotenv import load_dotenv
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


class TelegramFlowBot:

    def __init__(self, telegram_token: str):
        self.updater = Updater(telegram_token)
        self.dispatcher = self.updater.dispatcher

    def start_bot(self):
        self.updater.start_polling()

    def add_command_handler(self, action: str, callback_function):
        self.dispatcher.add_handler(CommandHandler(action, callback_function))

    def add_message_handler(self, callback_function):
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, callback_function))

    @staticmethod
    def start(update: Update, context: CallbackContext):
        """Send a message when the command /start is used."""
        user = update.effective_user
        update.message.reply_markdown_v2(
            fr'Hi {user.mention_markdown_v2()}\!',
            reply_markup=ForceReply(selective=True),
        )

    @staticmethod
    def echo(update: Update, context: CallbackContext):
        """Echo the user message."""
        update.message.reply_text(update.message.text)

    @staticmethod
    def help_command(update: Update):
        """Send a message when the command /help is issued."""
        update.message.reply_text('Help!')


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TG_TOKEN')

    tg_flow_instance = TelegramFlowBot(telegram_token)
    tg_flow_instance.add_command_handler(action='start', callback_function=tg_flow_instance.start)
    tg_flow_instance.add_message_handler(callback_function=tg_flow_instance.echo)

    tg_flow_instance.start_bot()
