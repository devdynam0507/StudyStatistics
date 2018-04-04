from django import template

register = template.Library()

@register.filter
def get_item(value, arg):
    try:
        return value[arg]
    except:
        return None

@register.filter
def get_math_data(value, arg):
    try:
        v = value[arg]
        return v['math']
    except:
        return None

@register.filter
def get_science_data(value, arg):
    try:
        v = value[arg]
        return v['science']
    except:
        return None

@register.filter
def get_korean_data(value, arg):
    try:
        v = value[arg]
        return v['korean']
    except:
        return None

@register.filter
def get_english_data(value, arg):
    try:
        v = value[arg]
        return v['english']
    except:
        return None


@register.filter
def get_top_data(value):
    try:
        return value[0]
    except:
        return 0

@register.filter
def get_min_data(value):
    try:
        return value[6]
    except:
        return 0

@register.filter
def get_none_count(value):
    return value['nonecount']

@register.filter
def get_month_data(value, arg):
    try:
        return value[arg]
    except:
        return 0