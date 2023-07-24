---
Simple Telegram bot, made using Python and Telebot. It was made to test augmented web app technology. Used for a language school.

In order for this bot to work, you need to create your own telegram bot, and then insert its token into the appropriate field in the program. 
```
bot = telebot.TeleBot("token")
```
You also need to change the URL in the field for communication.
```
reply.add(telebot.types.InlineKeyboardButton(text='Связаться с Владимиром', callback_data='yes', url='ссылка на Владимира'))
```

---
