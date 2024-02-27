import telebot
from numpy import array_split
from telebot import types
from Data import symptoms_data
from Data.symptoms_data import *
from TeleBot_Functions import functions
specialists_dict = dict.fromkeys(
    ['Гинеколога', 'Аллерголога', 'Гастроэнтеролога', 'Дерматолога', 'Кардиолога', 'Невролога',
     'Офтальмолога', 'Травматолога', 'Отоларинголога', 'Проктолога', 'Стоматолога', 'Терапевта', 'Уролога',
     'Хирурга', 'Эндокринолога', 'Ревматолога'], 0)
bot = telebot.TeleBot('6953770870:AAGRSQccl2ATuRs8qyhmopUD7n6zY8-Pe7g')
result = []



@bot.message_handler(commands=['start'])
def start_survey(message):
    functions.standart_InlineKeyboard_Markup(primary_survey)
    bot.send_message(message.chat.id, 'Уточните симптоматику', reply_markup=functions.markup)


@bot.callback_query_handler(func=lambda call: call.data == 'pain')
def pain(call):
    functions.standart_InlineKeyboard_Markup(pain_survey)
    bot.send_message(call.from_user.id, 'Уточните симптоматику', reply_markup=functions.markup)


@bot.callback_query_handler(func=lambda call: call.data == 'abdominal_pain')
def abdominal_pain(call):
    functions.standart_InlineKeyboard_Markup(abdominal_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=functions.markup)


@bot.callback_query_handler(func=lambda
        call: call.data == 'left_hypochondrium' or call.data == 'right_hypochondrium' or call.data == 'upper_abdominal'
              or call.data == 'periumbilical' or call.data == 'left_flank' or call.data == 'right_flank')
def hypochondrium_pain(call):
    functions.symptom_of_final_order(call, Гастроэнтеролога=1, Хирурга=1)


@bot.callback_query_handler(func=lambda call: call.data == 'lower_abdominal_pain')
def lower_abdominal_pain(call):
    functions.symptom_of_final_order(call, Хирурга=1, Уролога=1, Гинеколога=1)

@bot.callback_query_handler(func=lambda call: call.data == 'chest_pain')
def abdominal_pain(call):
    functions.standart_InlineKeyboard_Markup(symptoms_data.chest_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=functions.markup)


@bot.callback_query_handler(func=lambda call: call.data == 'heart')
def lower_abdominal_pain(call):
    functions.symptom_of_final_order(call, Кардиолога=2, Терапевта=1)
@bot.callback_query_handler(func=lambda call: call.data == 'right_chest' or call.data =='lower_chest')
def lower_abdominal_pain(call):
    functions.symptom_of_final_order(call, Терапевта=1)

@bot.callback_query_handler(func=lambda call: call.data == 'headache')
def headache(call):
    functions.standart_InlineKeyboard_Markup(headache_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=functions.markup)

@bot.callback_query_handler(func=lambda call: call.data == 'forehead' or call.data =='occipit' or call.data=='temporal')
def parts_of_the_head(call):
    functions.symptom_of_final_order(call, Терапевта=1, Невролога=1)

@bot.callback_query_handler(func=lambda call: call.data == 'limb_pain')
def limb(call):
    functions.standart_InlineKeyboard_Markup(limb_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=functions.markup)

@bot.callback_query_handler(func=lambda call: call.data == 'arm' or call.data == 'leg')
def arm(call):
    functions.standart_InlineKeyboard_Markup(arm_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=functions.markup)
@bot.callback_query_handler(func=lambda call: call.data == 'joint' or call.data== 'other_limb_pain')
def joint(call):
    functions.standart_InlineKeyboard_Markup(joint_injury_survey)
    bot.send_message(call.from_user.id, 'Связана ли текущая боль с травмой?', reply_markup=functions.markup)

@bot.callback_query_handler(func=lambda call: call.data == 'traumatic joint pain')
def traumatic(call):
    functions.symptom_of_final_order(call, Травматолога=1)

@bot.callback_query_handler(func=lambda call: call.data == 'non-traumatic joint pain')
def non_traumatic(call):
    functions.symptom_of_final_order(call, Ревматолога=1)

@bot.callback_query_handler(func=lambda call: call.data == 'other_limb_pain')
def leg(call):
    functions.standart_InlineKeyboard_Markup(other_limb_injury_survey)
    bot.send_message(call.from_user.id, 'Связана ли текущая боль с травмой?', reply_markup=functions.markup)

@bot.callback_query_handler(func=lambda call: call.data == 'traumatic limb pain')
def traumatic(call):
    functions.symptom_of_final_order(call, Травматолога=2)

@bot.callback_query_handler(func=lambda call: call.data == 'no limb injury')
def traumatic(call):
    functions.symptom_of_final_order(call, Терапевта=1, Хирурга=1)



@bot.callback_query_handler(func=lambda call: call.data == 'no')
def do_final_score(call):
    # main_applicant=result[0]
    # result.remove(main_applicant)
    # for applicant in result:
    #     if
    bot.send_message(call.message.chat.id, f'Вам стоит посетить {result[0]}, также, возможно, {result[1]}')


@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def go_back_to_start_survey(call):
    functions.standart_InlineKeyboard_Markup(primary_survey)
    bot.send_message(call.from_user.id, 'Уточните симптоматику', reply_markup=functions.markup)

bot.polling(none_stop=True)
