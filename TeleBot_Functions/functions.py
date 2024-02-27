import telebot
from numpy import array_split
from telebot import types
def standart_InlineKeyboard_Markup(symptoms_dict):
    global markup
    markup = types.InlineKeyboardMarkup()
    row_elem = []
    for k, v in symptoms_dict.items():
        k = types.InlineKeyboardButton(str(k), callback_data=str(v))

        row_elem.append(k)
        split_row_elem = array_split(row_elem, len(row_elem) // 2 + (len(row_elem) % 2 != 0))
    for sublist in split_row_elem:
        markup.add(*sublist)


def symptom_of_final_order(call, **kwargs):
    for item in kwargs.items():
        specialists_dict[item[0]] += item[1]
    scoring()
    markup = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton('Да', callback_data='yes')
    no = types.InlineKeyboardButton('Нет', callback_data='no')
    markup.row(yes, no)

    bot.send_message(call.message.chat.id, 'У вас есть другие жалобы?', reply_markup=markup)
def scoring():
    for specialist, score in sorted(specialists_dict.items(), key=lambda x: x[1], reverse=True):
        result.append(specialist)
    return result