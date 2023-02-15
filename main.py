import telebot
from telebot import types

bot = telebot.TeleBot("token")

feedback = types.ReplyKeyboardMarkup(resize_keyboard=True)
feedback.add(types.KeyboardButton("Обратная связь"))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Вы интересуетесь *Английским для инглишманов*?\nНажмите на кнопку "Меню", чтобы записаться на занятия или увидеть другую полезную информацию', parse_mode="Markdown", reply_markup=feedback)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет!', reply_markup=feedback)
    elif message.text == 'Обратная связь':
        reply = telebot.types.InlineKeyboardMarkup()
        reply.add(telebot.types.InlineKeyboardButton(text='Связаться с Владимиром', callback_data='yes', url='ссылка на Владимира'))
        bot.reply_to(message, "Чтобы получить обратную связь, нажмите на кнопку под сообщением", reply_markup=reply)
    else:
        bot.send_message(message.chat.id, 'Извините, я не понимаю, о чем вы говорите. Нажмите на кнопку "Меню", чтобы воспользоваться функционалом бота', reply_markup=feedback)


@bot.callback_query_handler(func=lambda call: True)
def get_feedback(call):
    if call.data == 'yes':
        bot.send_message(457378203, 'Привет!', reply_markup=feedback)


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    bot.reply_to(message, "Извините, я не понимаю, зачем мне это", reply_markup=feedback)


bot.polling(none_stop=True)
