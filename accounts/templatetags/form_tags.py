"""Small template filters that make Django forms easier to style with Bootstrap."""
from django import template

register = template.Library()


@register.filter
def add_class(field, css_class):
    """Render a form field with an extra CSS class."""
    existing = field.field.widget.attrs.get("class", "")
    classes = f"{existing} {css_class}".strip()
    return field.as_widget(attrs={"class": classes})
