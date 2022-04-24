import os

from dotenv import load_dotenv

from telegram_bot import TelegramFlowBot


def start_tg_dialog_bot(telegram_token):
    tg_flow_instance = TelegramFlowBot(telegram_token)
    tg_flow_instance.add_command_handler(action='start', callback_function=tg_flow_instance.start)
    tg_flow_instance.add_message_handler(callback_function=tg_flow_instance.echo)
    tg_flow_instance.start_bot()


def main():
    """The main logic for starting dialog flow bot."""
    load_dotenv()
    telegram_token = os.getenv('TG_TOKEN')

    start_tg_dialog_bot(telegram_token)


if __name__ == '__main__':
    main()
