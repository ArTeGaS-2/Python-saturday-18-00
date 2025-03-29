from telegram.ext import (Application, # Ядро
                        CommandHandler, # Обробник команд (/start)
                        MessageHandler, # Обробник повідомлень
                        filters, # Фільтри (текст, команди, пікчі)
                        ContextTypes)
from telegram import Update
import httpx

# Ключ API для Groqcloud
GROCLOUD_API_KEY = ""
# URL API Groqcloud
GROCLOUD_ENDPOINT = "https://api.groqcloud.com/v1/chat"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обробобник команди /start.
    Ініціалізує історію діалогу користувача та відправляє привітяння
    """
    context.user_data["history"] = [{"role": "system",
        "content":"Ти корисний бот. Відповідай Українською."}]
    await update.message.reply_text(
        "Привіт, ти спілкуєшся з моделлю від Groqcloud.")
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обробник текстових повідомлень.
    Додає повідомлення користувача до історії, надсилає запит до API
    Groqcloud та повертає відповідь.
    """
    user_input = update.message.text.strip() # введення користувача
    # Отримуємо історію діалогу або створюємо нову, якщо її немає
    history = context.user_data.get("history",[])
    # Додаємо повідомлення користувача до історії
    history.append({"role": "user", "content": user_input})

    # Формуємо запит до Groqcloud
    payload = {
        "model": "llama-3.2",
        "messages": history,
    }
    headers = {
        "Authorization": f"Bearer {GROCLOUD_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(GROCLOUD_ENDPOINT,
                json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

            reply = data["choices"][0]["message"]["content"].strip()
            history.append({"role": "assistant", "content":reply})
            await update.message.reply_text(reply)
        except Exception as e:
            await update.message.reply_text(f"Виникла помилка: {e}")

def main():
    TOKEN = ""
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, chat))
    app.run_polling()                                  
if __name__ == '__main__':                  
    main()     