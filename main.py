import telebot
from numpy import array_split
from telebot import types

specialists_dict = dict.fromkeys(
    ['Гинеколога', 'Аллерголога', 'Гастроэнтеролога', 'Дерматолога', 'Кардиолога', 'Невролога',
     'Офтальмолога', 'Травматолога', 'Отоларинголога', 'Проктолога', 'Стоматолога', 'Терапевта', 'Уролога',
     'Хирурга', 'Эндокринолога', 'Ревматолога'], 0)
bot = telebot.TeleBot('6953770870:AAGRSQccl2ATuRs8qyhmopUD7n6zY8-Pe7g')
result = []


def scoring():
    for specialist, score in sorted(specialists_dict.items(), key=lambda x: x[1], reverse=True):
        result.append(specialist)
    return result


primary_survey = {'Боль': 'pain', 'Изменение цвета выделений из половых органов'
: 'female_discharge_alteration', 'Насморк': 'rheum', 'Контактная сыпь': 'contact rush'
                  }

pain_survey = {'Боль в животе': 'abdominal_pain', 'Боль в грудной клетке': 'chest_pain', 'Головная боль': 'headache',
               'Боль в конечностях': 'limb_pain', 'Другая боль': 'other_pain'}
abdominal_pain_survey = {'Слева под ребром': 'left_hypochondrium', 'Справа под ребром': 'right_hypochondrium',
                         'В верху живота': 'upper_abdominal', 'Посередине живота': 'periumbilical',
                         'Слева в боку': 'left_flank', 'Справа в боку': 'right_flank',
                         'Боль в низу живота': 'lower_abdominal_pain'}
chest_pain_survey = {'В области сердца': 'heart', 'Боль в груди справа': 'right_chest',
                     'Боль в нижних отделах грудной клетки': 'lower_chest'}
headache_pain_survey = {'В области лба': 'forehead', 'В области затылка': 'occipit', 'В области висков': 'temporal'}
other_pain = {'Боль в области спины': 'back', 'Боль в области шеи': 'neck', 'Боль в области поясницы': 'lower_back'}

# Временно опросники по ноге и руке одинаковы, как и выводы.
# Позднее требуется либо объединить, либо дополнить функционал.
limb_pain_survey = {'Боль в руке': 'arm', 'Боль в ноге': 'leg'}
arm_pain_survey = {'Боль в одном/нескольких суставах': 'joint', 'Другое': 'other_limb_pain'}
leg_pain_survey = {'Боль в одном/нескольких суставах': 'joint', 'Другое': 'other_limb_pain'}
joint_injury_survey = {'Да':'traumatic joint pain', 'Нет':'no injury'}
other_limb_injury_survey = {'Да':'traumatic limb pain', 'Нет':'no limb injury'}



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
    standart_InlineKeyboard_Markup(chest_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'heart')
def lower_abdominal_pain(call):
    symptom_of_final_order(call, Кардиолога=2, Терапевта=1)
@bot.callback_query_handler(func=lambda call: call.data == 'right_chest' or call.data =='lower_chest')
def lower_abdominal_pain(call):
    symptom_of_final_order(call, Терапевта=1)

@bot.callback_query_handler(func=lambda call: call.data == 'headache')
def headache(call):
    standart_InlineKeyboard_Markup(headache_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'forehead' or call.data =='occipit' or call.data=='temporal')
def parts_of_the_head(call):
    symptom_of_final_order(call, Терапевта=1, Невролога=1)

@bot.callback_query_handler(func=lambda call: call.data == 'limb_pain')
def limb(call):
    standart_InlineKeyboard_Markup(limb_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'arm' or call.data == 'leg')
def arm(call):
    standart_InlineKeyboard_Markup(arm_pain_survey)
    bot.send_message(call.from_user.id, 'Уточните локализацию', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data == 'joint' or call.data== 'other_limb_pain')
def joint(call):
    standart_InlineKeyboard_Markup(joint_injury_survey)
    bot.send_message(call.from_user.id, 'Связана ли текущая боль с травмой?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'traumatic joint pain')
def traumatic(call):
    symptom_of_final_order(call, Травматолога=1)

@bot.callback_query_handler(func=lambda call: call.data == 'non-traumatic joint pain')
def non_traumatic(call):
    symptom_of_final_order(call, Ревматолога=1)

@bot.callback_query_handler(func=lambda call: call.data == 'other_limb_pain')
def leg(call):
    standart_InlineKeyboard_Markup(other_limb_injury_survey)
    bot.send_message(call.from_user.id, 'Связана ли текущая боль с травмой?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'traumatic limb pain')
def traumatic(call):
    symptom_of_final_order(call, Травматолога=2)

@bot.callback_query_handler(func=lambda call: call.data == 'no limb injury')
def traumatic(call):
    symptom_of_final_order(call, Терапевта=1, Хирурга=1)



@bot.callback_query_handler(func=lambda call: call.data == 'no')
def do_final_score(call):
    # main_applicant=result[0]
    # result.remove(main_applicant)
    # for applicant in result:
    #     if
    bot.send_message(call.message.chat.id, f'Вам стоит посетить {result[0]}, также, возможно, {result[1]}')


@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def go_back_to_start_survey(call):
    standart_InlineKeyboard_Markup(primary_survey)
    bot.send_message(call.from_user.id, 'Уточните симптоматику', reply_markup=markup)

bot.polling(none_stop=True)
