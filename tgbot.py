from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters,CallbackQueryHandler 
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup,ChatAdministratorRights, ChatPermissions
import os
TOKEN=os.environ['TOKEN']
import json


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
            ['Telegramdagi kanallar 👥'],
            ['Web saytlar 🕸'],
            ['Bot haqida 🤖', 'Asosiy menuga qaytish 🔙']
        ], resize_keyboard=True)
        text=f"{first_name} bu bot sizga treyding sohasini urganishingizga yordam beradi. "
        bot.sendMessage(chat_id=chat_id, reply_markup=keyboard,text=text)
    

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
updater=Updater(token=TOKEN)
dp=updater.dispatcher
def bot_haqida_uz(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendMessage(chat_id=chat_id, text="Sizga ham shunaqa telegram botlari kerak bulsa bizga murojat qiling!")
    bot.sendMessage(chat_id=chat_id, text='@Jasurbek070910')

dp.add_handler(CommandHandler('start',start))
dp.add_handler(MessageHandler(Filters.text('Asosiy menuga qaytish 🔙'),start))
dp.add_handler(CallbackQueryHandler(query))
dp.add_handler(MessageHandler(Filters.text('Telegramdagi kanallar 👥'),kanal_uz))
dp.add_handler(MessageHandler(Filters.text('Web saytlar 🕸'), web_sayt_uz))
dp.add_handler(MessageHandler(Filters.text('Bot haqida 🤖'),bot_haqida_uz))
updater.start_polling()
updater.idle()