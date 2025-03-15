from telegram.ext import (Application, # Ядро
                        CommandHandler, # Обробник команд (/start)
                        MessageHandler, # Обробник повідомлень
                        filters, # Фільтри (текст, команди, пікчі)
                        ContextTypes)
from telegram import Update
from openai import OpenAI

# Додавання ключів
client = OpenAI(api_key="") # API ключ
TOKEN = ""                  # Токен боту

# Словник для зберігання історії чату
chat_histories = {}
max_history = 20 # Обмеження на кількість записів

def update_history(chat_id, role, content):
    if chat_id not in chat_histories:
        chat_histories[chat_id] = []
    chat_histories[chat_id].append(
        {"role": role, "content": content})
    # Перевірка: якщо історія перевищує max_history, обрізати 
    # останні до max_history
    if  len(chat_histories[chat_id]) > max_history:
        chat_histories[chat_id] = chat_histories[chat_id][
            -max_history:]
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Напиши мені, і я спробую відповісти.")
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    user_text = update.message.text
    # Додаємо повідомлення користувача до історії
    update_history(chat_id, "user", user_text)
    # Створюємо базовий список повідомлень
    system_message = {
        "role": "system", # Системна роль. інші: user та assistant
        "content": "Ти допоміжний бот." # Системне повідомлення
        }
    history = chat_histories.get(chat_id, [])
    message = [system_message] + history
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Назва моделі в API
            messages=message,    # повідомлення
            max_tokens=150,      # Максимальна довжина повідомлення
            temperature=0.7      # 
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Помилка: {e}"
    # Додаємо відповідь бота до історії
    update_history(chat_id, "assistant", reply)
    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()                                  
if __name__ == '__main__':                  
    main()     

