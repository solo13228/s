import vk_api
import time
import json
import random

vk = vk_api.VkApi(token="bde6447a7cdf0856b5f91f7de8280225870bc464038513a58d7b6949b290f67fe5306e41b9bced984ae46")
vk._auth_token()


def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard = {
    "one_time": False,
    "buttons": [

    [get_button(label="О нас", color="primary"), get_button(label="Цены", color="positive")],
    [get_button(label="Барберы", color="negative"), get_button(label="Контакты", color="default")]

    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body == "Привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет, друг!", "random_id": random.randint(1, 2147483647)})
            elif body == "О нас":
                vk.method("messages.send", {"peer_id": id, "message": "💈GOLDEN BEAUTY COWORKING💈\n🏡Пространство для барберов, женских парикмахеров и мастеров прочих индустрий красоты с возможностью почасовой аренды.\n\n💡Мы предоставляем оборудованные рабочие места для барберов, женских парикмахеров, бровистов, визажистов и маникюристов от 100 рублей в час.\n\n👌Идеальное расположение:\nКоворкинг находится в самом центре города, на Левобулачной 24, близко к автобусной остановке, а также имеется парковка рядом.\n\n👌Оборудованное рабочее место\nМы позаботились о том, чтобы Вам и Вашим клиентам было максимально комфортно и оборудовали каждое рабочее место всем необходимым! Долой «диванные» процедуры и кухонные столы!\n\n👌Удобные тарифы\nВы сами выбираете сколько часов и по каким дням Вы будете принимать клиентов, ориентируясь в первую очередь на свои потребности, арендуйте от 1 часа до месяца.\n\n👌Быстрое бронирование\nВам не нужно «висеть» на телефоне, чтобы записаться к нам. Достаточно просто забронировать место через виджет онлайн-записи\n\nhttps://vk.com/app5581020_-174285119\n\nДля клиентов наших резидентов у нас также имеются комфортный диван для отдыха, чай/ вода, Playstation 4, скучать не придется😉", "random_id": random.randint(1, 2147483647)})
            elif body == "Барберы":
                vk.method("messages.send", {"peer_id": id, "message": "Недоступно.", "random_id": random.randint(1, 2147483647)})
            elif body == "Контакты":
                vk.method("messages.send", {"peer_id": id, "message": "Контактные данные:\n\n📞Телефон: +7 905 039-53-55\n🔵Социальные сети:\nVk: https://vk.com/gbcoworking\nInstagram: https://www.instagram.com/golden_beauty_co/\n🌎Адрес:\nКазань, ул. Лево-Булачная, 24\n⏰Работаем каждый день с 10:00 до 22:00.\n📌Записаться онлайн:\nhttps://vk.cc/8UEHly", "random_id": random.randint(1, 2147483647)})
            elif body == "Цены":
                vk.method("messages.send", {"peer_id": id, "message": "✨Тарифы на рабочие места!\n\n✨Кресло барбера:\n1 час - 150 руб.\n2 часа - 300 руб.\n3 часа - 400 руб.\n4 часа - 500 руб.\n5 часов - 600 руб.\n6 часов - 700 руб.\n7, 8 часов - 800 руб.\nОт 9 часов - 900 руб.\n15 дней - 7900 руб.\n30 дней -15 000 руб.\n\n✨Маникюрный стол:\n1 час – 100 руб.\n2 часа – 200 руб.\n3 часа – 300 руб.\n4 часа – 380 руб.\n5 часов – 460 руб.\n6 часов – 540 руб.\n7, 8 часов – 700 руб.\nОт 9часов – 750 руб.\n15 дней – 5000 руб.\n30 дней – 8000 руб.\n\n✨Место для бровиста/визажиста:\n1 час – 100 руб.\n2 часа – 200 руб.\n3 часа – 300 руб.\n4 часа – 380 руб.\n5 часов – 460 руб.\n6 часов – 540 руб.\n7, 8 часов – 700 руб.\nОт 9часов – 750 руб.\n15 дней – 5000 руб.\n30 дней – 8000 руб.", "random_id": random.randint(1, 2147483647)})
            elif body == "Начать":
                vk.method("messages.send", {"peer_id": id, "message": "💈GOLDEN BEAUTY COWORKING💈\nПространство для барберов, женских парикмахеров и мастеров прочих индустрий красоты с возможностью почасовой аренды!\n⁉️Для ознакомления используйте кнопки.", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
            elif body == "начать":
                vk.method("messages.send", {"peer_id": id, "message": "💈GOLDEN BEAUTY COWORKING💈\nПространство для барберов, женских парикмахеров и мастеров прочих индустрий красоты с возможностью почасовой аренды!\n⁉️Для ознакомления используйте кнопки.", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
            elif body == "Начать.":
                vk.method("messages.send", {"peer_id": id, "message": "💈GOLDEN BEAUTY COWORKING💈\nПространство для барберов, женских парикмахеров и мастеров прочих индустрий красоты с возможностью почасовой аренды!\n⁉️Для ознакомления используйте кнопки.", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Неизвестная команда. Введите команду Начать.", "random_id": random.randint(1, 2147483647)})
        time.sleep(0.5)
    except Exception as E:
        time.sleep(1)