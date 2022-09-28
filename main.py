from vk_api.bot_longpoll import VkBotEventType  # импортируем VkBotEventType для определения типа события
from connection import longpoll  # импортируем longpoll полученный в connection для дальнейшего прослушивания событий
from response import response_definition  # импортируем response, чтобы в дальнейшем отправить туда данные


def run():  # функция для запуска бота
    print('Server started')  # пишем в консоль, что бот начал работу
    for event in longpoll.listen():  # прослушиваем события от вк
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:  # если событие это новое сообщение и из чата,
            msg = event.object.message['text']  # присваиваем переменной msg сообщение получаемое из ивента
            chat_id = event.chat_id  # то же самое с id чата
            response_definition(chat_id, msg)  # отправляем эти данные дальше в response_definition


if __name__ == '__main__':  # если запущен именно этот файл,
    run()  # вызываем run
