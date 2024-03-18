from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters,CallbackQueryHandler 
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup,ChatAdministratorRights, ChatPermissions
import os
TOKEN=os.environ['TOKEN']
import json
import sys
from flask import Flask
app=Flask(__name__)
@app.route('/')


def start(update:Update, context:CallbackContext):
    bot=context.bot
    user_id=update.message.from_user.id
    chat_id=update.message.chat_id
    first_name=update.message.from_user.first_name
    last_name=update.message.from_user.last_name
    text= f'Assalomu alaykum {first_name}'
    if update.message.chat.type=='private':
        bot.send_message(chat_id=chat_id,text=text)
        text=f'{first_name} tilni tanlang\n{first_name} bыберите язык'
        uzbek_tili=InlineKeyboardButton("Uzbek tili 🇺🇿", callback_data='uzbek_tili')
        rus_tili=InlineKeyboardButton('Pусский язык 🇷🇺', callback_data='rus_tili')
        
        button=InlineKeyboardMarkup([[uzbek_tili, rus_tili]])
        bot.sendMessage(chat_id=chat_id, text=text, reply_markup=button)

def query(update:Update, context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    data=query.data
    bot=context.bot
    first_name=query.message.from_user.first_name
    if data=='uzbek_tili':
        keyboard=ReplyKeyboardMarkup([
            ['Telegramdagi kanallar 👥', 'Telegramdagi gruppalar 👥'],
            ['Web saytlar 🕸', 'Traderlarning instagram profillari 🧓'],
            ['You tobe kanallar 👥','Bot haqida 🤖','Asosiy menuga qaytish 🔙']
        ], resize_keyboard=True)
        text=f"{first_name} bu bot sizga treyding sohasini urganishingizga yordam beradi. "
        bot.sendMessage(chat_id=chat_id, reply_markup=keyboard,text=text)
    elif data=='rus_tili':
        keyboard=ReplyKeyboardMarkup([
            ['Telegram-каналы 👥','Группы в Telegram 👥'],
            ['Сайты 🕸','Инстаграм-профили трейдеров 🧓'],
            ['Вы слушаетесь каналов 👥','О боте 🤖', 'Вернитесь в главное меню 🔙']
        ], resize_keyboard=True)
        text="этот бот поможет вам изучить торговую индустрию."
        bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text=text)

    return 'Ok'

def kanal_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    #bot.sendMessage(chat_id=chat_id, text='https://t.me/hbsdarslari')
    keyboard=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='1-kanal', url='https://t.me/hbsdarslari')],
        [InlineKeyboardButton(text='2-kanal', url='https://t.me/TreydingFeruzbekAliev')],
        [InlineKeyboardButton(text='3-kanal', url='https://t.me/treyding_darsliklar')],
        [InlineKeyboardButton(text='4-kanal', url='https://t.me/Ake_Forex_Treyding_Shokh')]
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text="Botimiz sizga shu kanallarni tavsiya qiladi")

def web_sayt_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    keyboard=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='1-sayt', url='https://tradersunion.com/uz/brokers/forex/view/pocketoption/')],
        [InlineKeyboardButton(text='2-sayt', url='https://tradersunion.com/uz/brokers/forex/view/roboforex/')],
        [InlineKeyboardButton(text='3-sayt', url='https://tradersunion.com/uz/brokers/forex/view/exness/')],
        [InlineKeyboardButton(text='4-sayt', url='https://tradersunion.com/uz/brokers/forex/view/libertex/')],
        [InlineKeyboardButton(text='5-sayt',url='https://tradersunion.com/uz/brokers/forex/view/forex4you/')],
        [InlineKeyboardButton(text='6-sayt', url='https://tradersunion.com/uz/brokers/forex/view/ic_markets/')]
    ])
    bot.sendMessage(chat_id=chat_id,reply_markup=keyboard, text='Botimiz sizga ushbu Web saytlarni tavsiya qiladi' )

def group_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    keyboard=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='1-group', url='https://t.me/Yuk_markazi_gruppa_0')],
        [InlineKeyboardButton(text='2-group',url='https://t.me/dado_chat')]
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text='Botimiz sizga ushbu telegram gruppalarini tavsiya qiladi')

def treyder_ins_uz(update:Update, context:CallbackContext):
    bot=context.bot
    chat_id=update.message.chat.id
    keyboard= InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Aziz Halikov', url='https://www.instagram.com/a.halikov?igsh=dWV4ZjdjanE4eTg2')],
        [InlineKeyboardButton(text='Bek trader', url='https://www.instagram.com/bek_trader_?igsh=ZG9zcjdrNXJoeXFn')],
        [InlineKeyboardButton(text='Nur Ismoilov', url='https://www.instagram.com/nur.ismoilov?igsh=MXQ4ejdpenBicjh5NQ==')]
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text="Marhamat!")

def bot_haqida_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendMessage(chat_id=chat_id, text="Sizga ham shunaqa telegram botlari kerak bulsa bizga murojat qiling!")
    bot.sendMessage(chat_id=chat_id, text='https://t.me/Programmer_adminn')

def you_tobe_uz(update:Update, context:CallbackContext):
    bot=context.bot
    chat_id=update.message.chat.id
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='DaDo trader', url='https://youtube.com/@DaDoTrader?si=XE8CmDHmTJKQSQaj')],
        [InlineKeyboardButton(text='noxonfx', url='https://youtube.com/@noxonfx?si=0wlZ0GxywMnP8k69')],
        [InlineKeyboardButton(text='Feruzbek Aliev', url='https://youtube.com/@feruzbekaliev?si=G7xCpgoPRSSv1vgO')]
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text='Marhamat!')

def kanal_ru(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    keyboard=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Канал 1', url='https://t.me/TreydingFeruzbekAliev')],
        [InlineKeyboardButton(text='Канал 2', url='https://t.me/tradingonline777')],
        [InlineKeyboardButton(text='Канал 3', url='https://t.me/tradingonline777')],
        [InlineKeyboardButton(text='Канал 4', url='https://t.me/traders_channels')],
        [InlineKeyboardButton(text='Канал 5', url='https://t.me/TradingMastodonta')],
        [InlineKeyboardButton(text='Канал 6', url='https://t.me/Sliv_trading_kurs')],
        [InlineKeyboardButton(text='Канал 7', url='https://t.me/Trading_Privatki_Signals')]
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text='Наш бот порекомендует вам эти каналы')

def web_sayt_ru(update:Update, context:CallbackContext):
    bot=context.bot
    chat_id=update.message.chat.id
    keyboard=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Сайт 1', url='https://landing.deriv.com/global-markets-spreads-2-ru/?utm_source=google&utm_medium=ppc-paid_search&utm_campaign=cis-uz-prosp-all-fx_spreads-0124-ru-google&utm_term=online%20trading&t=jA_BJFRk2x3RRLQ0YTtceWNd7ZgqdRLk&gclid=Cj0KCQjwqdqvBhCPARIsANrmZhPs4dCiGrR0CxqzztbYW-8WJWl3YKMv6ByKgPtjtoi4-pj-ZSwt8goaAg-AEALw_wcB')],
        [InlineKeyboardButton(text='Сайт 2', url='https://www.xm.com/landing/promo-shares/ru?gid=217888&gad_source=1&gclid=Cj0KCQjwqdqvBhCPARIsANrmZhNzY2XxGy-siwdu2kT1pWtpBUheD0ohz28YEnl7rjKh1xhnFI-7xW4aApRGEALw_wcB')],
        [InlineKeyboardButton(text='Сайт 3', url='https://promo.fxclub.org/lp/ru-ru/lbx-portfolio-b/?utm_source=google&utm_medium=sem&utm_mediumtype=search&utm_campaign=search_uz_generic_invest&utm_term=forex%20trade_b&utm_country=uz&gad_source=1&gclid=Cj0KCQjwqdqvBhCPARIsANrmZhNsi_48ODXRLMcIDjx5BVeVS95kiATjxAlyyUmPEtYda4z-6gCM2-IaAmmGEALw_wcB')],
        [InlineKeyboardButton(text='Сайт 4', url='https://www.fortrade.com/ru/glossary/web-trader-web-trading-platform/')]
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text='Наш бот порекомендует вам эти сайты')

def you_tobe_ru(update:Update, context:CallbackContext):
    bot=context.bot
    chat_id=update.message.chat.id
    keyboard=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Сергей Виноградов', url='https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa1J2XzhaeHFLQXJXc3pCOHNNTllfWkdLOC1nd3xBQ3Jtc0tsemlRS0lnM3BXeEduV3lOVEJveFdqLUhiM3lvSTVuVWtuTHB3M2dKSFFzaHpzNE11RUlPUU92UEN0cDloLTlldHRGY2hMWGFaSWFnRkRWUFhzWDNXWWxiUURJOXlpQjFEZFYwM0ZSM2l4ZEdvUTlFWQ&q=https%3A%2F%2Fgoo.gl%2FWN7Q6Z&v=2Kx2-U6jXw4')],
        [InlineKeyboardButton(text='Батя', url='https://www.youtube.com/@buildmountain')],
        [InlineKeyboardButton(text='CRYPTOR BLOG', url='https://www.youtube.com/@CrypTorBlog')],
        [InlineKeyboardButton(text='Егор Егоров', url='https://www.youtube.com/@EGOROV_official')]
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text='добро пожаловать')

def group_ru(update:Update, context:CallbackContext):
    bot=context.bot
    chat_id=update.message.chat.id
    keyboard=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Группа 1', url='https://t.me/Trading_Privatki_Signals')],
        [InlineKeyboardButton(text='Группа 2', url='https://t.me/tradingonline777')],
        [InlineKeyboardButton(text='Группа 3', url='https://t.me/+-P2mCc8O34M4MTZk')]
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text='добро пожаловать')

def trader_ins_ru(update:Update, context:CallbackContext):
    bot=context.bot
    chat_id=update.message.chat.id
    keyboard=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Профиль 1', url='https://www.instagram.com/big_russian_trader?igsh=bzZ0a2o0eWJzMG5t')],
        [InlineKeyboardButton(text='Профиль 2', url='https://www.instagram.com/trading_russian?igsh=MXFkcWx6eGNheW5paQ==')],
        [InlineKeyboardButton(text='Профиль 2', url='https://www.instagram.com/the_russian_trader?igsh=MWo0YTJtZzJicHgzbw==')]
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text='добро пожаловать')

def bot_haqida_ru(update:Update, context:CallbackContext):
    bot=context.bot
    chat_id=update.message.chat.id
    bot.sendMessage(chat_id=chat_id, text='Свяжитесь с нами, если вам нужны такие Telegram-боты!')
    bot.sendMessage(chat_id=chat_id, text='https://t.me/Programmer_adminn')


updater=Updater(token=TOKEN)
dp=updater.dispatcher


dp.add_handler(CommandHandler('start',start))
dp.add_handler(MessageHandler(Filters.text('Asosiy menuga qaytish 🔙'),start))
dp.add_handler(CallbackQueryHandler(query))
dp.add_handler(MessageHandler(Filters.text('Telegramdagi kanallar 👥'),kanal_uz))
dp.add_handler(MessageHandler(Filters.text('Web saytlar 🕸'), web_sayt_uz))
dp.add_handler(MessageHandler(Filters.text('Bot haqida 🤖'),bot_haqida_uz))
dp.add_handler(MessageHandler(Filters.text('Telegramdagi gruppalar 👥'),group_uz))
dp.add_handler(MessageHandler(Filters.text('Traderlarning instagram profillari 🧓'),treyder_ins_uz))
dp.add_handler(MessageHandler(Filters.text('You tobe kanallar 👥'),you_tobe_uz))
# ruscha varianti
dp.add_handler(MessageHandler(Filters.text('Вернитесь в главное меню 🔙'),start))
dp.add_handler(MessageHandler(Filters.text('Telegram-каналы 👥'),kanal_ru))
dp.add_handler(MessageHandler(Filters.text('Сайты 🕸'),web_sayt_ru))
dp.add_handler(MessageHandler(Filters.text('Вы слушаетесь каналов 👥'),you_tobe_ru))
dp.add_handler(MessageHandler(Filters.text('Группы в Telegram 👥'), group_ru))
dp.add_handler(MessageHandler(Filters.text('Инстаграм-профили трейдеров 🧓'), trader_ins_ru))
dp.add_handler(MessageHandler(Filters.text('О боте 🤖'), bot_haqida_ru))

updater.start_polling()
updater.idle()