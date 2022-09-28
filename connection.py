from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.vk_api import VkApiGroup
token = 'токен сообщества'
group_id = 'id сообщества'

vk_session = VkApiGroup(token=token)  # тут мы создаем сессию, для этого нужен token твоего сообщества
vk = vk_session.get_api()  # получаем само api ВК для сессии, чтобы в дальнейшем взаимодействовать с ним через код
longpoll = VkBotLongPoll(vk_session, group_id)  # получаем longpoll, чтобы принимать все события
