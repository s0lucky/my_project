from pprint import pprint
import random
import vk_api
from python123 import token_of_group, token_of_service

vk = vk_api.VkApi(token=token_of_group)
vk2 = vk_api.VkApi(token=token_of_service)
while True:
    info_about_messages = vk.method(
        "messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"}
    )

    if info_about_messages["count"] >= 1:
        text_of_last_message = info_about_messages["items"][0]["last_message"]["text"]
        sent = text_of_last_message.split(".")[0]
        user_id = info_about_messages["items"][0]["last_message"]["from_id"]

        if sent == "https://vk":
            domain = text_of_last_message.split("/")[-1]

        info_about_wall = vk2.method(
            "wall.get", {"offset": 0, "count": 1, "domain": domain}
        )

        if text_of_last_message.lower() == "привет":
            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": "Привет, я бот Антон",
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




