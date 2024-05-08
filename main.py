import telebot
from telebot import types


bot = telebot.TeleBot('your token')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Начать")
    markup.add(item1)
    bot.reply_to(message, 'Привет!\nЧтобы перейти на основной канал, поддержите наших партнёров Вашей царской подпиской!', reply_markup=markup)
    
@bot.message_handler(func=lambda message: message.text == 'Начать')
def userStart(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Первый канал', url='your link'))
    markup.add(types.InlineKeyboardButton('Второй канал', url=''your link'))
    markup.add(types.InlineKeyboardButton('Третий канал', url=''your link'))
    bot.reply_to(message, 'Вот они, наши лучшие друзья, каналы которых Вам обязательно понравятся! Когда подпишитесь, нажмите: /subscribe', reply_markup=markup)

@bot.message_handler(commands=['subscribe'])
def subscribe_user(message):
    subscribed_channels = ['@channel', '@channel', '@channel']
    subscribed_all = True  
    for channel in subscribed_channels:
        try:
            member = bot.get_chat_member(channel, message.chat.id)
            if member.status == 'left':
                bot.send_message(message.chat.id, f'Вы не подписаны на канал {channel}!')
                subscribed_all = False  
            else:
                bot.send_message(message.chat.id, f'Вы подписаны на канал {channel}!')
        except telebot.apihelper.ApiException as e:
            if 'user not found' in str(e).lower():
                bot.send_message(message.chat.id, f'Ошибка: пользователь не найден при проверке подписки на канал {channel}!')
            else:
                bot.send_message(message.chat.id, f'Произошла ошибка при проверке подписки на канал {channel}: {e}')

    if subscribed_all:
        main_channel_link = 'your link'
        bot.send_message(message.chat.id, f'Вы подписались на все каналы, спасибо Вам! Вот ссылка на основной канал: {main_channel_link}')
        
bot.polling(none_stop=True)
