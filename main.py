import telebot
from numpy import array_split
from telebot import types
from Data import symptoms_data
from Data.specialists import specialists_dict
from Data.symptoms_data import *

bot = telebot.TeleBot('6953770870:AAGRSQccl2ATuRs8qyhmopUD7n6zY8-Pe7g')


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

    markup = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton('Да', callback_data='yes')
    no = types.InlineKeyboardButton('Нет', callback_data='no')
    markup.row(yes, no)

    bot.send_message(call.message.chat.id, 'У вас есть другие жалобы?', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start_survey(message):
    standart_InlineKeyboard_Markup(primary_survey)
    bot.send_message(message.chat.id, 'Уточните симптоматику', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'pain')
def pain(call):
    standart_InlineKeyboard_Markup(pain_survey)
    bot.send_message(call.from_user.id, 'Уточните симптоматику', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'abdominal_pain')
def abdominal_pain(call):
    standart_InlineKeyboard_Markup(abdominal_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=markup)


@bot.callback_query_handler(func=lambda
        call: call.data == 'left_hypochondrium' or call.data == 'right_hypochondrium' or call.data == 'upper_abdominal'
              or call.data == 'periumbilical' or call.data == 'left_flank' or call.data == 'right_flank')
def hypochondrium_pain(call):
    symptom_of_final_order(call, Гастроэнтеролога=1, Хирурга=1)


@bot.callback_query_handler(func=lambda call: call.data == 'lower_abdominal_pain')
def lower_abdominal_pain(call):
    symptom_of_final_order(call, Хирурга=1, Уролога=1, Гинеколога=1)


@bot.callback_query_handler(func=lambda call: call.data == 'chest_pain')
def abdominal_pain(call):
    standart_InlineKeyboard_Markup(symptoms_data.chest_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'heart')
def lower_abdominal_pain(call):
    symptom_of_final_order(call, Кардиолога=2, Терапевта=1)


@bot.callback_query_handler(func=lambda call: call.data == 'right_chest' or call.data == 'lower_chest')
def lower_abdominal_pain(call):
    symptom_of_final_order(call, Терапевта=1)


@bot.callback_query_handler(func=lambda call: call.data == 'headache')
def headache(call):
    standart_InlineKeyboard_Markup(headache_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=markup)


@bot.callback_query_handler(
    func=lambda call: call.data == 'forehead' or call.data == 'occipit' or call.data == 'temporal')
def parts_of_the_head(call):
    symptom_of_final_order(call, Терапевта=1, Невролога=1)


@bot.callback_query_handler(func=lambda call: call.data == 'no')
def do_final_score(call):
    sort_specialists_list = sorted(specialists_dict.items(), key=lambda x: x[1],
                                   reverse=True)
    print(sort_specialists_list)  # Тестирование.
    bot.send_message(call.message.chat.id,
                     f'Вам стоит посетить {sort_specialists_list[0][0]}, также, возможно, {sort_specialists_list[1][0]}')


@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def go_back_to_start_survey(call):
    standart_InlineKeyboard_Markup(primary_survey)
    bot.send_message(call.from_user.id, 'Уточните симптоматику', reply_markup=markup)


bot.polling(none_stop=True)
