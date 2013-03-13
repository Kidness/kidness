# -*- encoding: utf-8 -*-
# django imports
from django.conf import settings
from django.core.cache import cache
from django.template import Library, Node, TemplateSyntaxError
from django.utils.translation import ugettext as _
import re

# portlets imports
import portlets.utils

register = Library()

@register.filter
def month_as_text(num):
    months = {
              1: u"января",
              2: u"февраля",
              3: u"марта",
              4: u"апреля",
              5: u"мая",
              6: u"июня",
              7: u"июля",
              8: u"августа",
              9: u"сентября",
              10: u"октября",
              11: u"ноября",
              12: u"декабря",
              }
    return months[int(num)]

register.tag('month_as_text', month_as_text)


def increment_var(parser, token):

    parts = token.split_contents()
    if len(parts) < 2:
        raise TemplateSyntaxError("'increment' tag must be of the form:  {% increment <var_name> %}")
    return IncrementVarNode(parts[1])

register.tag('++', increment_var)

class IncrementVarNode(Node):

    def __init__(self, var_name):
        self.var_name = var_name

    def render(self,context):
        try:
            value = context[self.var_name]
            context[self.var_name] = value + 1
            return u""
        except:
            raise TemplateSyntaxError("The variable does not exist.")


@register.filter
def bytes_to_kilobytes(num):
    return "%.1f Kb"%(round(num/1000.0,1),)

