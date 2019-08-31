import telebot
from telebot import types
bot = telebot.TeleBot('702348641:AAGCGNuGwQSnudy_PamkpL0ft4FJXpks1yI')

generalmarkup = types.ReplyKeyboardMarkup(row_width=2)
btnplay = types.KeyboardButton('🎰 Играть')
btnbalance = types.KeyboardButton('💰Баланс')
generalmarkup.add(btnplay, btnbalance)

@bot.message_handler(content_types=['text'])
def send_text(message):
    kb = types.InlineKeyboardMarkup()
    inlinepay = types.InlineKeyboardButton(text='Пополнить', callback_data='pay')
    inlinewithdraw = types.InlineKeyboardButton(text='Вывести', callback_data='withdraw')
    kb.add(inlinepay, inlinewithdraw)
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Пополняй баланс и покажи на что ты способен!', reply_markup=generalmarkup)
    elif message.text == '🎰 Играть':
        bot.send_message(message.chat.id,
"""Напишите сумму ставки.
В случае победы ваша ставка *утраивается!*""", parse_mode='markdown')
    elif message.text == '💰Баланс':
        bot.send_message(message.chat.id, 'Ваш баланс: *0 рублей*', parse_mode='markdown', reply_markup=kb)
@bot.callback_query_handler(func=lambda call: True)
def inline(call):
    if call.data == 'pay':
        bot.send_message(call.message.chat.id, 'Выберите сумму или введите свою:')
    elif call.data == 'withdraw':
        bot.send_message(call.message.chat.id, 'На вашем счёте недостаточно средств для вывода! Минимальная сумма вывода: *1000 рублей*', parse_mode='markdown')
bot.polling()