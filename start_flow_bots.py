import os

from dotenv import load_dotenv

from dialog_flow_tools import detect_intent_texts
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
    google_app_creds = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    project_id = 'useful-assistant-bot-mgib'
    session_id = '123456789'
    texts = ['пРИвет!']
    language_code = 'ru'

    detect_intent_texts(project_id=project_id, session_id=session_id, texts=texts, language_code=language_code)
    # start_tg_dialog_bot(telegram_token)


if __name__ == '__main__':
    main()
