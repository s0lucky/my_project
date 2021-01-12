from pprint import pprint
import vk_api, random
from python123 import token_of_group, token_of_service
import requests

vk = vk_api.VkApi(token=token_of_group)
vk2 = vk_api.VkApi(token=token_of_service)
owner_id = -200707570

while True:

    info_about_wall = vk2.method(
        "wall.get", {"offset": 0, "count": 1, "owner_id": owner_id}
    )

    info_about_messages = vk.method(
        "messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"}
    )

    if info_about_messages["count"] >= 1:
        # ответ
        text_of_last_message = info_about_messages["items"][0]["last_message"]["text"]
        user_id = info_about_messages["items"][0]["last_message"]["from_id"]

        if text_of_last_message.lower() == "привет":
            # привет
            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": "Привет, я бот Антон",
                    "random_id": random.randint(1, 1000),
                },
            )
        elif text_of_last_message.lower() == "что ты умеешь?":

            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": "Я могу выполнить следующие команды:"
                               " "
                               "1)картинка"
                               " "
                               "2)проанализировать группу",
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

        elif text_of_last_message.lower() == "проанализировать группу":
            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": "Что вы хотите получить?"
                               "1)Пост с максимальным количеством лайков"
                               "2)Пост с максимальным количеством комментариев"
                               "3)Пост с максимальным количеством репостов",
                    "random_id": random.randint(1, 1000),
                },
            )

        elif text_of_last_message.lower() == "1":
            count_of_likes = str(info_about_wall["items"][0]["likes"]["count"])

            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": count_of_likes + "👍🏻",
                    "random_id": random.randint(1, 1000),
                },
            )

        elif text_of_last_message.lower() == "2":
            count_of_comments = info_about_wall["items"][0]["comments"]["count"]

            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": count_of_comments,
                    "random_id": random.randint(1, 1000),
                },
            )

        elif text_of_last_message.lower() == "3":
            count_of_reposts = info_about_wall["items"][0]["reposts"]["count"]

            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": count_of_reposts,
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


# VkApi - класс
# requests - запросы
# VkUpload -  класс для работы с медиафайлами
# items - диалоги
# messages.getConversations - возвращает список бесед пользователя.
# messages.send - ответить на сообщение пользователя
# offset - параметр смещения
# count - параметр максимальное число результатов, которые нужно получить
# filter(unanswered) - фильтр бесед, помеченных как неотвеченные(только для групп вк)


# info_about_man = vk.method(
#   "users.get", {"user_ids": 1, "fields": "city"}
# )
# city_of_man = info_about_man[0]["city"]["title"]
# pprint(city_of_man)




