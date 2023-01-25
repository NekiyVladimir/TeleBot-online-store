import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)

Hello = ('Привет', 'Здравствуйте', 'привет')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Здравствуйте')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Акции")
    markup.add(item1)
    item2=types.KeyboardButton("Для маникюра и педикюра")
    markup.add(item2)
    item3 = types.KeyboardButton("Для наращивания ресниц")
    markup.add(item3)
    item4 = types.KeyboardButton("Для бровей")
    markup.add(item4)
    item5 = types.KeyboardButton("Для волос")
    markup.add(item5)
    bot.send_message(message.chat.id,'Выберите что Вам нужно',reply_markup=markup)




@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Акции":
        bot.send_message(message.chat.id,"https://krassa.by/specials/")
    elif message.text in Hello:
        bot.send_message(message.chat.id, "Вас приветствует менеджер магазина KRASSA.BY."
                                          " Режим работы магазина: Пн.-Вс. с 10.00 до 19.00")
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Для маникюра и педикюра",
                                             url='https://krassa.by/dlya-manikyura-i-pedikyura/')
        markup.add(button1)
        button2 = types.InlineKeyboardButton("Для наращивания ресниц",
                                             url='https://krassa.by/dlya-manikyura-i-pedikyura/')
        markup.add(button2)
        button3 = types.InlineKeyboardButton("Для бровей",
                                             url='https://krassa.by/dlya-manikyura-i-pedikyura/')
        markup.add(button3)
        button4 = types.InlineKeyboardButton("Для волос",
                                             url='https://krassa.by/dlya-manikyura-i-pedikyura/')
        markup.add(button4)
        button5 = types.InlineKeyboardButton("Акции",
                                             url='https://krassa.by/specials/')
        markup.add(button5)
        bot.send_message(message.chat.id, "Выберите необходимую категорию товаров".format(message.from_user),
                         reply_markup=markup)
    elif message.text == "Контакты":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Сайт Krassa.by", url='https://krassa.by/contact-us/')
        markup.add(button1)
        bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),reply_markup=markup)


bot.polling(none_stop=True)
#bot.infinity_polling()