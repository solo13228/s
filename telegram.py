import telebot

token="701088670:AAHYBKURWiuKhGNBGPt6DE6ja2jJIP4z82s"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def first(message):
    key = telebot.types.ReplyKeyboardMarkup(True, False)
    key.row('💈О нас', '💰Цены')
    key.row('💇‍♂️Барберы', '📱Контакты')
    send = bot.send_message(message.from_user.id, 'Выберите раздел:', reply_markup=key)


@bot.message_handler(content_types=['text'])
def first(message):
    if message.text == '💈О нас':
        bot.send_message(message.from_user.id, '💈GOLDEN BEAUTY COWORKING💈\n🏡Пространство для барберов, женских парикмахеров и мастеров прочих индустрий красоты с возможностью почасовой аренды.\n\n💡Мы предоставляем оборудованные рабочие места для барберов, женских парикмахеров, бровистов, визажистов и маникюристов от 100 рублей в час.\n\n👌Идеальное расположение:\nКоворкинг находится в самом центре города, на Левобулачной 24, близко к автобусной остановке, а также имеется парковка рядом.\n\n👌Оборудованное рабочее место\nМы позаботились о том, чтобы Вам и Вашим клиентам было максимально комфортно и оборудовали каждое рабочее место всем необходимым! Долой «диванные» процедуры и кухонные столы!\n\n👌Удобные тарифы\nВы сами выбираете сколько часов и по каким дням Вы будете принимать клиентов, ориентируясь в первую очередь на свои потребности, арендуйте от 1 часа до месяца.\n\n👌Быстрое бронирование\nВам не нужно «висеть» на телефоне, чтобы записаться к нам. Достаточно просто забронировать место через виджет онлайн-записи\n\nhttps://vk.com/app5581020_-174285119\n\nДля клиентов наших резидентов у нас также имеются комфортный диван для отдыха, чай/ вода, Playstation 4, скучать не придется')
    elif message.text == '💰Цены':
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('Кресло барбера', 'Маникюрный стол')
        key.row('Место для визажиста/бровиста', '\u2B05Нaзад')
        send = bot.send_message(message.from_user.id, 'Выберите услугу:', reply_markup=key)
    elif message.text == 'Кресло барбера':
        bot.send_message(message.from_user.id, '✨Кресло барбера:\n1 час - 150 руб.\n2 часа - 300 руб.\n3 часа - 400 руб.\n4 часа - 500 руб.\n5 часов - 600 руб.\n6 часов - 700 руб.\n7, 8 часов - 800 руб.\nОт 9 часов - 900 руб.\n15 дней - 7900 руб.\n30 дней -15 000 руб.')
    elif message.text == 'Маникюрный стол':
        bot.send_message(message.from_user.id, '✨Маникюрный стол:\n1 час – 100 руб.\n2 часа – 200 руб.\n3 часа – 300 руб.\n4 часа – 380 руб.\n5 часов – 460 руб.\n6 часов – 540 руб.\n7, 8 часов – 700 руб.\nОт 9часов – 750 руб.\n15 дней – 5000 руб.\n30 дней – 8000 руб.')
    elif message.text == 'Место для визажиста/бровиста':
        bot.send_message(message.from_user.id, '✨Место для бровиста/визажиста:\n1 час – 100 руб.\n2 часа – 200 руб.\n3 часа – 300 руб.\n4 часа – 380 руб.\n5 часов – 460 руб.\n6 часов – 540 руб.\n7, 8 часов – 700 руб.\nОт 9часов – 750 руб.\n15 дней – 5000 руб.\n30 дней – 8000 руб.')
    elif message.text == '\u2B05Нaзад':
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('💈О нас', '💰Цены')
        key.row('💇‍♂️Барберы', '📱Контакты')
        send = bot.send_message(message.from_user.id, 'Выберите раздел:', reply_markup=key)
    elif message.text == '💇‍♂️Барберы':
        bot.send_message(message.from_user.id, 'Недоступно.')
    elif message.text == '📱Контакты':
        bot.send_message(message.from_user.id, 'Контактные данные:\n\n📞Телефон: +7 905 039-53-55\n🔵Социальные сети:\nVk: https://vk.com/gbcoworking\nInstagram: https://www.instagram.com/golden_beauty_co/\n🌎Адрес:\nКазань, ул. Лево-Булачная, 24\nРаботаем каждый день с 10:00 до 22:00.\nЗаписаться онлайн:\nhttps://vk.cc/8UEHly')
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, 55.7918047, 49.1071271)
    else:
        bot.send_message(message.from_user.id, "Вы ввели неверную команду. Пожалуйста используйте кнопки для навигации.️")

bot.polling(none_stop=True, interval=0, timeout=20)

