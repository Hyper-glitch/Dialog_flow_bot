import os

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv

from telegram_bot import TelegramFlowBot


def start_tg_bot(telegram_token):
    tg_flow_instance = TelegramFlowBot(telegram_token)
    tg_flow_instance.add_command_handler(action='start', callback_function=tg_flow_instance.start)
    tg_flow_instance.add_message_handler(callback_function=tg_flow_instance.answer)
    tg_flow_instance.start_bot()


def start_vk_bot(vk_token):
    vk_session = vk_api.VkApi(token=vk_token)
    longpoll = vk_api.longpoll.VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            if event.to_me:
                print('Для меня от: ', event.user_id)
            else:
                print('От меня для: ', event.user_id)
            print('Текст:', event.text)


def main():
    """The main logic for starting dialog flow bot."""
    load_dotenv()
    telegram_token = os.getenv('TG_TOKEN')
    vk_token = os.getenv('VK_GROUP_TOKEN')
    # start_tg_bot(telegram_token)
    start_vk_bot(vk_token)


if __name__ == '__main__':
    main()
