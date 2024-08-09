from django.template.defaulttags import register


@register.filter
def students_count_declination(value : str) -> str:
    """ Функция склонения слова студент (студент, студента, студентов) """
    __instance = int(value)

    if __instance % 10 == 1 and __instance % 100 != 11:
        return 'студент'
    elif __instance % 10 in [2, 3, 4] and __instance % 100 not in [12, 13, 14]:
        return 'студента'
    else:
        return 'студентов'
