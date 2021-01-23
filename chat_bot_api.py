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

        if text_of_last_message.lower() == "привет":
            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": "Привет, я бот Антон. Если хочешь проанализировать группу вк, то пришли мне ссылку на неё",
                    "random_id": random.randint(1, 1000),
                },
            )

        if text_of_last_message.lower() == "что ты умеешь?":
            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": "Я могу выполнить следующие команды:\n"
                               "1)проанализировать группу\n"
                    "P.S разработчик другому меня ещё не обучил, прости",
                    "random_id": random.randint(1, 1000),
                },
            )
        if text_of_last_message.lower() == "проанализировать группу":
            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": "Что вы хотите получить?(введи номер)\n" 
                               "1.Пост с максимальным количеством лайков\n"
                               "2.Пост с максимальным количеством комментариев\n"
                               "3.Пост с максимальным количеством репостов",
                    "random_id": random.randint(1, 1000),
                },
            )

        if sent == "https://vk":
            domain = text_of_last_message.split("/")[-1]

            info_about_wall = vk2.method(
                "wall.get", {"offset": 0, "count": 1, "domain": domain}
            )

            count_of_posts = info_about_wall["count"]
            count = count_of_posts
            count_of_posts = str(info_about_wall["count"])
            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": "Спасибо. Кол-во постов на странице : "
                               + count_of_posts
                               + "\nТеперь напиши 'проанализировать группу' или 'что ты умеешь?'",
                    "random_id": random.randint(1, 1000),
                },
            )

        if text_of_last_message.lower() == "1":
            info_about_wall = vk2.method(
                "wall.get", {"offset": 0, "count": count, "domain": domain}
            )

            count_of_likes = []

            for i in range(count):
                count_of_likes.append(i)

            for i in range(count):
                count_of_likes[i] = info_about_wall["items"][i]["likes"]["count"]
                max_count_of_likes = count_of_likes[i]
                if count_of_likes[i] < count_of_likes[i - 1]:
                    max_count_of_likes = count_of_likes[i - 1]
                else:
                    max_count_of_likes = count_of_likes[i]

            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": max_count_of_likes,
                    "random_id": random.randint(1, 1000),
                },
            )

        if text_of_last_message.lower() == "2":

            count_of_comments = []

            for i in range(count):
                count_of_comments.append(i)

            for i in range(count):
                count_of_comments[i] = info_about_wall["items"][i]["comments"]["count"]
                if count_of_comments[i] < count_of_comments[i - 1]:
                    max_count_of_comments = count_of_comments[i - 1]
                else:
                    max_count_of_comments = count_of_comments[i]

            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": max_count_of_comments,
                    "random_id": random.randint(1, 1000),
                },
            )

        if text_of_last_message.lower() == "3":
            count_of_reposts = []

            for i in range(count):
                count_of_reposts.append(i)

            for i in range(count):
                count_of_reposts[i] = info_about_wall["items"][i]["reposts"]["count"]
                if count_of_reposts[i] < count_of_reposts[i - 1]:
                    max_count_of_reposts = count_of_reposts[i - 1]
                else:
                    max_count_of_reposts = count_of_reposts[i]

            vk.method(
                "messages.send",
                {
                    "user_id": user_id,
                    "message": max_count_of_reposts,
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




