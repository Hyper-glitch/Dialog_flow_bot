from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from dialog_flow_tools import detect_intent_texts


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
    def answer(update: Update, context: CallbackContext):
        """Send message from user to Dialog Flow and return detected answer to telegram chat."""
        text_from_user = update.message.text
        dialog_flow_answer = detect_intent_texts(text_from_user)
        update.message.reply_text(dialog_flow_answer)

    @staticmethod
    def help_command(update: Update):
        """Send a message when the command /help is issued."""
        update.message.reply_text('Help!')
