import os
import random

import vk_api as vk
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from dialog_flow_tools import detect_intent_texts
from telegram_bot import TelegramFlowBot


def start_tg_bot(telegram_token):
    tg_flow_instance = TelegramFlowBot(telegram_token)
    tg_flow_instance.add_command_handler(action='start', callback_function=tg_flow_instance.start)
    tg_flow_instance.add_message_handler(callback_function=tg_flow_instance.answer)
    tg_flow_instance.start_bot()


def start_vk_bot(vk_token):
    vk_session = vk.VkApi(token=vk_token)
    longpoll = vk.longpoll.VkLongPoll(vk_session)
    vk_api = vk_session.get_api()

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            dialog_flow_answer = detect_intent_texts(event.text)

            vk_api.messages.send(
                user_id=event.user_id,
                message=dialog_flow_answer,
                random_id=random.randint(1, 1000),
            )


def main():
    """The main logic for starting dialog flow bot."""
    load_dotenv()
    telegram_token = os.getenv('TG_TOKEN')
    vk_token = os.getenv('VK_GROUP_TOKEN')
    start_tg_bot(telegram_token)
    start_vk_bot(vk_token)


if __name__ == '__main__':
    main()
