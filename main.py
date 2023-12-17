import telebot
import webbrowser
from telebot import types
import requests
import json

bot = telebot.TeleBot('6439760825:AAEFjoWTUinDSotzXj0rk5MNPKYcAiTnLV4')
API = '8139d34f21455da175dac0944ecd91c0'

#news
@bot.message_handler(commands=['news'])
def news(message):
   markup = types.InlineKeyboardMarkup()
   btn1 = types.InlineKeyboardButton('Перейти на сайт',url='https://www.алмазный-край.рф/novosti/')
   btn2 = types.InlineKeyboardButton('Вернуться обратно', callback_data='end')
   markup.row(btn1,btn2)
   bot.send_message(message.chat.id,'<b>Последние новости:</b>', parse_mode='html',reply_markup=markup)

#info
@bot.message_handler(commands=['info'])
def info(message):
   markup = types.InlineKeyboardMarkup()
   btn1 = types.InlineKeyboardButton('Перейти на сайт',url='https://www.алмазный-край.рф/rayon/informatsiya/o-rayone/')
   btn2 = types.InlineKeyboardButton('Вернуться обратно', callback_data='end')
   markup.row(btn1,btn2)
   bot.send_message(message.chat.id,'<b>Информация:</b>', parse_mode='html',reply_markup=markup)

#events
@bot.message_handler(commands=['events'])
def events(message):
   markup = types.InlineKeyboardMarkup()
   btn1 = types.InlineKeyboardButton('Перейти на сайт',url='https://www.алмазный-край.рф/administratsiya-mo/plany-osnovnykh-meropriyatiy.php')
   btn2 = types.InlineKeyboardButton('Вернуться обратно', callback_data='end')
   markup.row(btn1,btn2)
   bot.send_message(message.chat.id,'<b>Планы мероприятий:</b>',parse_mode='html', reply_markup=markup)

#services
@bot.message_handler(commands=['services'])
def services(message):
   markup = types.InlineKeyboardMarkup()
   btn1 = types.InlineKeyboardButton('Перейти на сайт',url='https://www.алмазный-край.рф/administratsiya-mo/munitsipalnye-uslugi/')
   btn2 = types.InlineKeyboardButton('Вернуться обратно', callback_data='end')
   markup.row(btn1,btn2)
   bot.send_message(message.chat.id,'<b>Услуги:</b>', parse_mode='html',reply_markup=markup)

#emergency
@bot.message_handler(commands=['emergency'])
def emergency(message):
   markup = types.InlineKeyboardMarkup()
   btn2 = types.InlineKeyboardButton('Вернуться обратно', callback_data='end')
   markup.row(btn2)
   bot.send_message(message.chat.id, '<b>Экстренные телефоны </b>\n<i>С мобильного телефона:</i>\n101 – пожарная служба;\n102 – полиция;\n103 – скорая медицинская помощь;\n112 – единый номер для вызова экстренных служб.\n<i>Со стационарного телефона:</i>\n01 – пожарная служба;\n02 – полиция;\n03 – скорая медицинская помощь;\n44-112, 43-112 – единая дежурно-диспетчерская служба.', parse_mode='html',reply_markup=markup)

#feedback
@bot.message_handler(commands=['feedback'])
def feedback(message):
   markup = types.InlineKeyboardMarkup()
   btn2 = types.InlineKeyboardButton('Вернуться обратно', callback_data='end')
   markup.row(btn2)
   bot.send_message(message.chat.id, '<b>Контактная информация:</b> 678170, г. Мирный, улица Ленина,19, тел. 4-96-04, 4-96-03, 4-96-02, электронный адрес: odik@adm-mirny.ru.', parse_mode='html',reply_markup=markup)

#help
@bot.message_handler(commands=['help'])
def help(message):
   bot.send_message(message.chat.id, 'Список команд, чтобы ими воспользоваться достаточно просто кликнуть по ним:\n/info - команда для получения основной информации об администрации города, такой как контактные данные, рабочие часы и другие полезные сведения.\n/news - команда для получения последних новостей и объявлений от администрации города.\n/events - команда для получения информации о предстоящих мероприятиях, организуемых администрацией города.\n/services - команда для получения информации о доступных услугах, предоставляемых администрацией города.\n/feedback - команда для отправки обратной связи или задания вопроса администрации города.\n/emergency - команда для получения информации о контактах экстренных служб и процедурах в случае чрезвычайных ситуаций.')

#можно создать много таких функций для определенных команд
#start
@bot.message_handler(commands=['start'])
def main(message):
   markup = types.ReplyKeyboardMarkup() #15 min ur 3
   btn1 = types.KeyboardButton('Погода')
   markup.add(btn1)
   bot.send_message(message.chat.id, f'Дорогой {message.from_user.first_name},Мы рады приветствовать вас на нашем сайте! Администрация гордится представлять вам нашу платформу, где вы можете общаться, делиться информацией и находить новых друзей. Мы стремимся создать комфортное и безопасное пространство для всех пользователей, поэтому не стесняйтесь обращаться к нам с любыми вопросами или предложениями. Чтоб узнать информацию нажмите или пропишите /help',reply_markup=markup)
   bot.register_next_step_handler(message, get_weather)


@bot.message_handler(content_types=['text'])
def get_weather(message):
   if message.text == 'Погода':
      city = 'Mirny'
      res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
      data = json.loads(res.text)
      bot.reply_to(message, f'Сейчас погода: {data["main"]["temp"]}°')
   #if message.text == 'Погода':
   #   bot.send_message(message.chat.id,'')


@bot.message_handler(content_types=['photo'])
def photo(message):
   bot.reply_to(message, 'Я не могу посмотреть ваше фото...')

@bot.callback_query_handler(func= lambda callback: True)
def callback_m(callback):
   if callback.data == 'end':
         bot.send_message(callback.message.chat.id, 'Список команд, чтобы ими воспользоваться достаточно просто кликнуть по ним:\n/info - команда для получения основной информации об администрации города, такой как контактные данные, рабочие часы и другие полезные сведения.\n/news - команда для получения последних новостей и объявлений от администрации города.\n/events - команда для получения информации о предстоящих мероприятиях, организуемых администрацией города.\n/services - команда для получения информации о доступных услугах, предоставляемых администрацией города.\n/feedback - команда для отправки обратной связи или задания вопроса администрации города.\n/emergency - команда для получения информации о контактах экстренных служб и процедурах в случае чрезвычайных ситуаций.')
   
#не от команд а от пользователя
#@bot.message_handler()
#def info(message):
#   if message.text.lower == 'привет':
#     bot.send_message(message.chat.id, f'Дорогой {message.from_user.first_name},Мы рады приветствовать вас на нашем сайте! Администрация гордится представлять вам нашу платформу, где вы можете общаться, делиться информацией и находить новых друзей. Мы стремимся создать комфортное и безопасное пространство для всех пользователей, поэтому не стесняйтесь обращаться к нам с любыми вопросами или предложениями.')#
# 3   elif message.text.lower == 'id':
#      bot.reply_to(message, f'ID')


bot.polling(non_stop=True)