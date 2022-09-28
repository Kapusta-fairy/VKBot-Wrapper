from actions import send_text, send_stick, send_file  # импортируем функции из actions


def response_definition(chat_id: int, msg: str):  # сюда мы передали данные из main
    """Подбирает подходящий ответ и отправляет его в actions"""

    if msg == 'тест':  # если сообщение = тест, то
        return send_text(chat_id, 'тестовый ответ')  # передаем в send_text id чата и текст для ответа

    elif msg == 'стикер':
        return send_stick(chat_id, 60804)  # передаем в send_text id чата и id стикера

    elif msg == 'гифка':
        return send_file(chat_id, 'doc465630601_633778583')  # передаем в send_text id чата и id файла
