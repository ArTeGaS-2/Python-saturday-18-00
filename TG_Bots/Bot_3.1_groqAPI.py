import httpx
from telegram import Update
from telegram.ext import (Application, CommandHandler,
                           MessageHandler, ContextTypes,
                             filters)
import os
# Ключ API для Groqcloud
GROCLOUD_API_KEY = os.environ['GROCLOUD_API_KEY']
# URL API Groqcloud - приклад, адаптуємо згідно з документацією.
GROCLOUD_ENDPOINT='https://api.groq.com/openai/v1/chat/completions'

MAX_HISTORY = 20 # Обмеження історії чату

async def start(update: Update, context:ContextTypes.DEFAULT_TYPE):
    """
    Обробник команди /start.
    Ініціалізує історію діалогу для користувача та відправляє
    вітальне повідомлення.
    """
    context.user_data["history"] = [{"role": "system",
        "content":"Ти корисний асистент. Відповідаєш Українською."}]
    await update.message.reply_text(
        "Привіт! Починаємо спілкування. Напиши щось.")
    
async def chat(update: Update, context:ContextTypes.DEFAULT_TYPE):
    """
    Обробник текстових повідомлень.
    Додає повідомлення користувача до історії, надсилає запит
    до API Groqcloud та повертає відповідь.
    """
    user_input = update.message.text.strip()

    if "history" not in context.user_data:
        context.user_data["history"] = [
            {"role": "system",
             "content": "Ти корисний асистент. Відповідаєш Українською."}]
    
    history = context.user_data["history"]

    # Додаємо повідомлення користувача до історії
    history.append({"role": "user", "content": user_input})

    if len(history) > 1 + MAX_HISTORY * 2:
        system_msg, *dialog = history
        history[:] = [system_msg] + dialog[-MAX_HISTORY * 2:]

    # Формуємо JSON_payload для запиту до Groqcloud
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": history
    }
    headers = {
        "Authorization": f"Bearer {GROCLOUD_API_KEY}",
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                GROCLOUD_ENDPOINT, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            reply = data["choices"][0]["message"]["Content"].strip()
            history.append[{"role": "assistant", "content": reply}]

            await update.message.reply_text(reply)
        except Exception as e:
            await update.message.reply_text(f"Виникла проблема: {e}")

def main():                         
    TOKEN = os.environ['TOKEN']       
    app = Application.builder().token(TOKEN).build()    

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, chat))

    app.run_polling()

if __name__ == "__main__":
    main()


