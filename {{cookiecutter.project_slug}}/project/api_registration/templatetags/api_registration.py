from django import template

register = template.Library()


@register.filter
def get_email_confirmation_code(activate_url):
    return activate_url.split("/")[5]

