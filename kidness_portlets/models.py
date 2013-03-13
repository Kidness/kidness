# coding: UTF-8
import re
import random

# django imports
from django import forms
from django.db import models
from django.template.loader import render_to_string
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

# tagging imports
import tagging

from tagging.forms import TagField

from lfc.fields.autocomplete import AutoCompleteTagInput
from lfc.models import BaseContent, Image

# portlets imports
from portlets.models import Portlet

from kidness.models import News, Anouncement, TrackingEvent

from program.models import Article, Program


class NewsPortlet(Portlet):
    random = models.BooleanField(u'Random order',default=False)
    show_more = models.BooleanField(u'Read more',default=True)
    quantity = models.IntegerField(u"Количество", default=0)
    
    def render(self, context):
        """Renders the portlet as HTML.
        """
        items = News.objects.all()
        if self.random:
            random.shuffle(items)
        
        if self.quantity:
            items = items[:self.quantity]  
        return render_to_string("lfc/portlets/news_portlet.html", {
            "title" : self.title,
            "items" : items,
            "show_more": self.show_more
        })

    def form(self, **kwargs):
        """Returns the form of the portlet.
        """
        return NewsPortletForm(instance=self, **kwargs)

class NewsPortletForm(forms.ModelForm):
    """Add/Edit form for the news portlet.
    """
    class Meta:
        model = NewsPortlet


class ArticlePortlet(Portlet):
    random = models.BooleanField(u'Random order',default=False)
    show_more = models.BooleanField(u'Read more',default=True)
    quantity = models.IntegerField(u"Количество", default=0)
    
    def render(self, context):
        """Renders the portlet as HTML.
        """
        items = Article.objects.all()
        if self.random:
            random.shuffle(items)
        
        if self.quantity:
            items = items[:self.quantity]  
        return render_to_string("lfc/portlets/articles_portlet.html", {
            "title" : self.title,
            "items" : items,
            "show_more": self.show_more
        })

    def form(self, **kwargs):
        """Returns the form of the portlet.
        """
        return ArticlePortletForm(instance=self, **kwargs)

class ArticlePortletForm(forms.ModelForm):
    """Add/Edit form for the news portlet.
    """
    class Meta:
        model = ArticlePortlet


class AnouncementPortlet(Portlet):
    random = models.BooleanField(u'Random order',default=False)
    quantity = models.IntegerField(u"Количество", default=0)
    tags = models.CharField(blank=True, max_length=100)
    
    def render(self, context):
        """Renders the portlet as HTML.
        """
        
        tags_list = []
        for tag in self.tags.split(","):
            tag = tag.strip()
            tags_list.append(tag)
            
        items = Anouncement.objects.filter(tags__in=tags_list)
#        if self.random:
#            random.shuffle(items)
        
        if self.quantity:
            items = items[:self.quantity]  
        return render_to_string("lfc/portlets/anouncements_portlet.html", {
            "title" : self.title,
            "items" : items
        })

    def form(self, **kwargs):
        """Returns the form of the portlet.
        """
        return AnouncementPortletForm(instance=self, **kwargs)

class AnouncementPortletForm(forms.ModelForm):
    """Add/Edit form for the Anouncement portlet.
    """
    class Meta:
        model = AnouncementPortlet


class TagsBlockPortlet(Portlet):
    tags = models.CharField(u"Tags", max_length=255)
    
    def render(self, context):
        """Renders the portlet as HTML.
        """
        tags_list = []
        for tag in self.tags.split(","):
            tag = tag.strip()
            tags_list.append(tag)
            
        return render_to_string("lfc/portlets/tags_block_portlet.html",  {
            "tags_list": tags_list
        })

    def form(self, **kwargs):
        """Returns the form of the portlet.
        """
        return TagsBlockPortletForm(instance=self, **kwargs)

class TagsBlockPortletForm(forms.ModelForm):
    """Add/Edit form for the news portlet.
    """
    class Meta:
        model = TagsBlockPortlet


class SignupButtonPortlet(Portlet):
    program =  models.ForeignKey(Program, blank=True, null=True)
    button_image = models.ForeignKey(Image, blank=True, null=True)
    dialog_header = models.CharField(blank=True, max_length=512)
    dialog_subheader = models.CharField(blank=True, max_length=1024)
    tracking_event =  models.ForeignKey(TrackingEvent, blank=True, null=True)
    tracking_event_success =  models.ForeignKey(TrackingEvent, blank=True, null=True, related_name="success_event")
    thankyou_text = models.CharField(blank=True, max_length=512)
    dialog_button_image = models.ForeignKey(Image, blank=True, null=True, related_name="dialog_button_image")
    block_text = models.CharField(blank=True, max_length=1024)
    
    def render(self, context):
        """Renders the portlet as HTML.
        """
        return render_to_string("lfc/portlets/signup_button_portlet.html", {
            "id": self.id,
            "program": self.program,
            "button_image": self.button_image,
            "dialog_header": self.dialog_header,
            "dialog_subheader": self.dialog_subheader,
            "tracking_event": self.tracking_event,
            "tracking_event_success": self.tracking_event_success,
            "thankyou_text": self.thankyou_text,
            "dialog_button_image": self.dialog_button_image,
            "block_text": self.block_text
            })

    def form(self, **kwargs):
        """Returns the form of the portlet.
        """
        return SignupButtonPortletForm(instance=self, **kwargs)

class SignupButtonPortletForm(forms.ModelForm):
    """Add/Edit form for the news portlet.
    """
    class Meta:
        model = SignupButtonPortlet
    
    def __init__(self, *args, **kwargs):
        super(SignupButtonPortletForm, self).__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        if instance:
            programs = BaseContent.objects.filter(content_type="program").order_by("parent__title")
            ordered_programs = [["", "-"]]
            for program in programs:
                ordered_programs.append([program.id, program.parent.title + "->" + program.title])
            self.fields["program"].choices = ordered_programs
            
            images = Image.objects.filter(content_id=1).order_by("title")
            portal_images = [["", "стандартная"]]
            for image in images:
                portal_images.append([image.id, image.title])
            self.fields["button_image"].choices = portal_images
            self.fields["dialog_button_image"].choices = portal_images


class AddThisBlockPortlet(Portlet):
    def render(self, context):
        """Renders the portlet as HTML.
        """
        return render_to_string("lfc/portlets/addthis_block_portlet.html", {})

    def form(self, **kwargs):
        """Returns the form of the portlet.
        """
        return AddThisBlockPortletForm(instance=self, **kwargs)

class AddThisBlockPortletForm(forms.ModelForm):
    """Add/Edit form for the AddThisBlockPortlet.
    """
    class Meta:
        model = AddThisBlockPortlet