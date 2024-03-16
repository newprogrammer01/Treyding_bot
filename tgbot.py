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
updater=Updater(token=TOKEN)
dp=updater.dispatcher


dp.add_handler(CommandHandler('start',start))
dp.add_handler(MessageHandler(Filters.text('Asosiy menuga qaytish 🔙'),start))
dp.add_handler(CallbackQueryHandler(query))
dp.add_handler(MessageHandler(Filters.text('Telegramdagi kanallar 👥'),kanal_uz))
updater.start_polling()
updater.idle()