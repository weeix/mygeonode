from django import template
from geonode_mapstore_client.templatetags import get_menu_json

register = template.Library()

@register.simple_tag(takes_context=True)
def get_base_right_topbar_menu(context):
    tags = get_menu_json.get_base_right_topbar_menu(context)
    tags += [
       {
           "type": "link",
           "href": "/",
           "label": "Custom 3"
       },
       {
           "type": "link",
           "href": "/",
           "label": "Custom 4"
       },
    ]
    return tags


@register.simple_tag(takes_context=True)
def get_base_left_topbar_menu(context):
    tags = get_menu_json.get_base_left_topbar_menu(context)

    tags += [
        {
           "type": "link",
           "href": "/",
           "label": "Custom 1"
        },
        {
           "type": "link",
           "href": "/",
           "label": "Custom 2"
        },
    ]
    return tags
