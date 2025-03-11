from telegram.ext import (Application, # Ядро
                        CommandHandler, # Обробник команд (/start)
                        MessageHandler, # Обробник повідомлень
                        filters) # Фільтри (текст, команди, пікчі)

TOKEN = 'key'
 # @BotFather у тг

async def start(update, context):
    await update.message.reply_text('Привіт! Я твій новий бот.')

async def echo(update, context):
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, echo))
    app.run_polling()      # @BotFather     # /start
                                            # /newbot
if __name__ == '__main__':                  # Lira
    main()                                  # LiraSmartBot