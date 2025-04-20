import logging
import datetime
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from telegram import ReplyKeyboardMarkup

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!",
    )


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("Я умею показывать дату и время. "
                                    "Команды /date и /time соответственно.")


async def echo(update, context):
    await update.message.reply_text(f'Я получил сообщение {update.message.text}')


async def get_date(update, context):
    d = datetime.datetime.now()
    await update.message.reply_text(f'Текущая дата: {d.strftime("%d-%m-%Y")}')


async def get_time(update, context):
    d = datetime.datetime.now()
    await update.message.reply_text(f'Текущее время: {d.strftime("%H:%M:%S")}')


def main():

    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("time", get_time))
    application.add_handler(CommandHandler("date", get_date))
    application.run_polling()


if __name__ == '__main__':
    main()
