from urllib.parse import quote as urlencode
from django import template

register = template.Library()


@register.simple_tag
def choice(product, artist):
    artist_firstname = artist.name.split(' ')[0]
    return f"Oi {artist_firstname}! Me interessei no {product.title}"


@register.simple_tag
def whatsapp(phone, text):
    return f"https://api.whatsapp.com/send?phone={phone}&text={urlencode(text)}"

