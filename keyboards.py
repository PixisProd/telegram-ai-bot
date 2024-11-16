from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_start_keyboard():
    kb = ReplyKeyboardBuilder()
    kb.button(text='AI mode 🤖')
    kb.adjust(1)
    return kb.as_markup()

def get_ai_mode_keyboard():
    kb = ReplyKeyboardBuilder()
    kb.button(text='Leave AI mode ❌')
    kb.adjust(1)
    return kb.as_markup()