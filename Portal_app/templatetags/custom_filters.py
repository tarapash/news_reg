from django import template


register = template.Library()

censor_list = ['term']
# Регистрируем наш фильтр под именем censor, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
    for word in censor_list:
        value = value.replace(word[1:], '*' * len(word[1:])) #Строковый метод str.replace(old, new[, count]) вернет копию строки,
        # в которой все подстроки old будут заменены на new.
    return value # Возвращаемое функцией значение подставится в шаблон.
