from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def contact_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Share contact📲', request_contact=True)

    kb.add(button)
    return kb

def translate_button():
    kb =ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Translate🔄')
    
    kb.add(button)

    return kb

def language_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    ru = KeyboardButton('Ru')
    ar = KeyboardButton('Ar')
    en = KeyboardButton('En')
    es = KeyboardButton('Es')
    uz = KeyboardButton('Uz')
    

    kb.add(ru,  en,es, uz,  )

    return kb