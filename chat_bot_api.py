from pprint import pprint
import vk_api, random
from python123 import tok

# vk - переменная сессии
# VkApi - класс
vk = vk_api.VkApi(token=tok)


while True:
    messages = vk.method(
        "messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"}
    )
    if messages["count"] >= 1:
        text_of_last_message = messages["items"][0]["last_message"]["text"]
        user_id = messages["items"][0]["last_message"]["from_id"]
        if text_of_last_message.lower() == "привет":
            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": "Привет, я бот Валера",
                    "random_id": random.randint(1, 1000),
                },
            )
        elif text_of_last_message.lower() == "картинка":
            uploader = vk_api.upload.VkUpload(vk)
            image = uploader.photo_messages("4.jpg")
            owner_id = str(image[0]["owner_id"])
            media_id = str(image[0]["id"])
            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "attachment": "photo" + owner_id + "_" + media_id,
                    "random_id": random.randint(1, 1000),
                },
            )

        else:
            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": "Я тебя не понимаю",
                    "random_id": random.randint(1, 1000),
                },
            )

# VkUpload -  класс для работы с медиафайлами
# items - диалоги
# messages.getConversations - возвращает список бесед пользователя.
# messages.send - ответить на сообщение пользователя
# offset - параметр смещения
# count - параметр максимальное число результатов, которые нужно получить
# filter(unanswered) - фильтр бесед, помеченных как неотвеченные(только для групп вк)
