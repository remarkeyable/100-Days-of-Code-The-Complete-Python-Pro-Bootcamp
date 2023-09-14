import qrcode
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, filters, MessageHandler, ContextTypes, CallbackQueryHandler
from typing import Final
import os

KEY: Final = os.environ['KEY]
USERNAME: Final = os.environ['USERNAME']


def generate_qr(data):
    file_path = os.path.abspath(os.getcwd())
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qr.png')
    the_file = f"{file_path}/qr.png"
    return the_file


def generate_qr_wifi(ssid, password):
    wifi_config = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    file_path = os.path.abspath(os.getcwd())
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )
    qr.add_data(wifi_config)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qr.png')
    the_file = f"{file_path}/qr.png"
    return the_file


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Hi hooman. I can generate QR codes for you. Just send me any text or if you want to generate a Wi-Fi QR code, please use the following format:')
    await update.message.reply_text(
        'wifi: SSID/PASSWORD, e.g., wifi: My_wifi/C4t00Wif1. You can copy paste & edit this format below:')
    await update.message.reply_text('wifi: Your_SSID/Your_Password')


async def pref(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.text
    generate = InlineKeyboardButton('Generate Qr', callback_data='generate')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[generate]])
    await update.message.reply_text(text="✔️", reply_markup=keyboard)
    context.user_data["data"] = data


async def pref_cb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = context.user_data.get('data')
    button = update.callback_query.data
    context.user_data["pref"] = button

    if button == 'generate' and 'wifi:' in text:
        parts = text[len("wifi: "):].split('/')
        ssid, password = parts
        image = generate_qr_wifi(ssid=ssid, password=password)
        await context.bot.send_photo(chat_id=update.callback_query.message.chat_id, photo=image)

    elif button == 'generate':
        image = generate_qr(text)
        await context.bot.send_photo(chat_id=update.callback_query.message.chat_id, photo=image)


if __name__ == '__main__':
    app = Application.builder().token(KEY).read_timeout(60).write_timeout(60).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, pref))
    app.add_handler(MessageHandler(filters.TEXT, pref_cb))
    app.add_handler(CallbackQueryHandler(pref_cb))
    app.run_polling(poll_interval=3)
