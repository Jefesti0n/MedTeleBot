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