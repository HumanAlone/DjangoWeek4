from django import template

register = template.Library()


@register.filter
def ru_pluralize(value_number, arg="дурак,дурака,дураков"):
    args = arg.split(",")
    number = abs(int(value_number))
    modulo_a = number % 10
    modulo_b = number % 100

    if modulo_a == 1 and modulo_b != 11:
        return args[0]
    elif 2 <= modulo_a <= 4 and (modulo_b < 10 or modulo_b >= 20):
        return args[1]
    return args[2]
