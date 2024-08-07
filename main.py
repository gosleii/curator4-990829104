import telebot
bot = telebot.TeleBot('7349729194:AAH83qC4D5Q_N3E-saSZ9ZSD_g_mKY5jzxw')

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, '*СПИСОК КОМАНД*\n /chanel -открытые каналы для подготовки ОГЭ/ЕГЭ \
    \n /motivation - команда на случай, если тебе не хватает мотивации \
    \n /lk_um - переход на сайт Умскул', parse_mode = 'Markdown')

@bot.message_handler(commands=['chanel'])
def chanel_handler(message):
    bot.send_message(message.chat.id, '_Открытые каналы для подготовки к ОГЭ/ЕГЭ:_ \n \
     [Русский язык ЕГЭ](https://t.me/dolgih_umrus) \n [Информатика ЕГЭ](https://t.me/infa_vikusya)', parse_mode = 'Markdown')

@bot.message_handler(commands=['motivation'])
def motivation_handler(message):
    bot.send_message(message.chat.id, 'У тебя все получится! Я в тебя верю!', parse_mode = 'Markdown')

@bot.message_handler(commands=['lk_um'])
def lk_um_handler(message):
    bot.send_message(message.chat.id, '_Нажми, чтобы перейти на сайт_ -> [тык](https://umschool.net/) ', parse_mode = 'Markdown')

bot.infinity_polling()