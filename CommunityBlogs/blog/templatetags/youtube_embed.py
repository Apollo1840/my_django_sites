import re
from django.utils.safestring import mark_safe
from django import template

register = template.Library()


@register.filter
def youtube_embed(value):
    """
    Convert YouTube URLs in content to embedded iframes.
    """
    youtube_regex = (
        r'(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]+)'
    )
    matches = re.findall(youtube_regex, value)
    if matches:
        for match in matches:
            video_id = match[3]
            embed_url = f'https://www.youtube.com/embed/{video_id}'
            value = value.replace(
                match[0],
                f'<iframe width="560" height="315" src="{embed_url}" frameborder="0" allowfullscreen></iframe>'
            )
    return mark_safe(value)
