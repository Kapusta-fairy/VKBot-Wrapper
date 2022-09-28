from connection import vk


def send_text(chat_id: int, text: str):  # принимаем в качестве аргументов chat_id и stick_id
    vk.messages.send(chat_id=chat_id, message=text, random_id=0)  # сама отправка сообщения в чат


def send_stick(chat_id: int, stick_id: int):
    vk.messages.send(chat_id=chat_id, sticker_id=int(stick_id), random_id=0)


def send_file(chat_id: int, url: str):
    vk.messages.send(chat_id=chat_id, attachment=url, random_id=0)
