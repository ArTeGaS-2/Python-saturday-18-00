import os
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import (Application, MessageHandler, ContextTypes,
                            filter)
TOKEN = os.environ['TOKEN']

# Набір слів - тригерів бану
BAD_WORDS = {"спойлер", "реклама", "гамно"}
# Тривалість бану (в годинах)
BAN_DURATION = timedelta(hours=5)

def is_violation(text: str) -> bool:
    lower = text.lower()
    return any(bad in lower for bad in BAD_WORDS)

async def moderate(update: Update,
                    context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    text = msg.text or ""
