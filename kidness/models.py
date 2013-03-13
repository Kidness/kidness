# coding: utf-8
from lfc.models import BaseContent
from django.db import models
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import portlets.utils
from portlets.models import Slot

from program.models import Program
from lfc.fields.thumbs import ImageWithThumbsFieldFile


# Create your models here.
class Client(models.Model):#BaseContent):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    ext_id = models.CharField(max_length=255)
    service = models.CharField(max_length=255, choices=[('vk', 'vk'), ('fb', 'fb')])
    path_to_photo = models.CharField(max_length=255)
    photo = models.ImageField(u"Фото", upload_to="/", blank=True, null=True)
    
    def __unicode__(self):
        return self.first_name + u" " + self.last_name


class ClientOpinion(BaseContent):
    client = models.ForeignKey(Client, related_name="opinions") 
    program = models.ForeignKey(Program, related_name="opinions") 
    text = models.TextField(u'Текст отзыва')
    to_publish = models.BooleanField(u"Публиковать на сайте")
    
    class Meta:
        verbose_name=_(u'ClientOpinion')
        verbose_name_plural=_(u'ClientOpinions')
        
    def form(self, **kwargs):
        """Returns the add/edit form of the ProgramCatalog
        """
        return ClientOpinionForm(**kwargs)


class ClientOpinionForm(forms.ModelForm):
    """The add/edit form of the ClientOpinion content object
    """
    class Meta:
        model = ClientOpinion
        fields = ("client", "program", "text", "to_publish")
        inlines = ["client"]

class ClientOpinionCatalog(BaseContent):
    
    class Meta:
        verbose_name=_(u'ClientOpinionCatalog')
        verbose_name_plural=_(u'ClientOpinionCatalogs')
        
    def form(self, **kwargs):
        """Returns the add/edit form of the ClientOpinionCatalog
        """
        return ClientOpinionCatalogForm(**kwargs)


class ClientOpinionCatalogForm(forms.ModelForm):
    """The add/edit form of the ProgramCatalog content object
    """
    class Meta:
        model = ClientOpinionCatalog
        fields = ("title", "slug")


class News(BaseContent):
    news_date = models.DateField(u"Дата", auto_now=True, blank=True)
    
    class Meta:
        verbose_name=_(u'News')
        verbose_name_plural=_(u'News')
        
    def form(self, **kwargs):
        """Returns the add/edit form of the News
        """
        return NewsForm(**kwargs)

class NewsForm(forms.ModelForm):
    """The add/edit form of the News content object
    """
    class Meta:
        model = News
        fields = ("title", "display_title", "slug", "description",  "publication_date" )
        
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = 'rich_text_format'


class ShowCase(BaseContent):
    text_title = models.TextField()
    text_subtitle = models.TextField()
    text_plain = models.TextField() 

    def form(self, **kwargs):
        """Returns the add/edit form of the ShowCase
        """
        return ShowCaseForm(**kwargs)
    
    class Meta:
        verbose_name=_(u'ShowCase')
        verbose_name_plural=_(u'ShowCases')

class ShowCaseForm(forms.ModelForm):
    """The add/edit form of the ShowCase content object
    """
    class Meta:
        model = ShowCase
        fields = ("title", "slug", "text_title", "text_subtitle", "text_plain")
    
    def __init__(self, *args, **kwargs):
        super(ShowCaseForm, self).__init__(*args, **kwargs)
#        self.fields['text_title'].widget.attrs['class'] = 'rich_text_format'
#        self.fields['text_subtitle'].widget.attrs['class'] = 'rich_text_format'
#        self.fields['text_plain'].widget.attrs['class'] = 'rich_text_format'

class MainPageBlock(BaseContent):
    text_title = models.TextField()
    text_plain = models.TextField() 
#    external_link = models.CharField(u"Внешняя ссылка", max_length=255, blank=True, null=True)
    linked_page = models.ForeignKey(BaseContent, related_name="main_page_block", blank=True, null=True)
    open_link_in_lightbox = models.BooleanField(u"Открывать в lignbox", blank=True, default=False)
    
    def form(self, **kwargs):
        """Returns the add/edit form of the MainPageBlock
        """
        return MainPageBlockForm(**kwargs)

    class Meta:
        verbose_name=_(u'MainPageBlock')
        verbose_name_plural=_(u'MainPageBlocks')
    
    def portlet(self):
        slot = Slot.objects.get(name="Left")
        portlets_ = portlets.utils.get_portlets(slot, self)
        if portlets_:
            portlet = portlets_[0]
            try:
                portlet_rendered = portlet.render({})
                return portlet_rendered
            except (Exception,), inst:
                pass
                #print inst

class MainPageBlockForm(forms.ModelForm):
    """The add/edit form of the MainPageBlock content object
    """
    class Meta:
        model = MainPageBlock
        fields = ("title", "slug", "text_title", "text_plain", "linked_page", "open_link_in_lightbox")
    
    def __init__(self, *args, **kwargs):
        super(MainPageBlockForm, self).__init__(*args, **kwargs)
        self.fields['text_title'].widget.attrs['class'] = 'rich_text_format'
        self.fields['text_plain'].widget.attrs['class'] = 'rich_text_format'


#class ClientForm(BaseContent):
#    header = models.CharField(u"Подзаголовок", max_length=512, blank=True, null=True)
#    subheader = models.CharField(u"Подзаголовок", max_length=1024, blank=True, null=True)
#    
#    def form(self, **kwargs):
#        """Returns the add/edit form of the ClientForm
#        """
#        return ClientFormForm(**kwargs)
#
#    class Meta:
#        verbose_name=_(u'ClientForm')
#        verbose_name_plural=_(u'ClientForms')
#
#class ClientFormForm(forms.ModelForm):
#    """The add/edit form of the ClientForm content object
#    """
#    class Meta:
#        model = ClientForm
#        fields = ("header", "subheader", )
#    
#    def __init__(self, *args, **kwargs):
#        super(ClientFormForm, self).__init__(*args, **kwargs)
#        self.fields['subheader'].widget.attrs['class'] = 'rich_text_format'
#        
#
#class CustomizedText(models.Model):
#    text = models.TextField()
#    customized_text = models.TextField()
#    
#    @staticmethod
#    def customize(cls, text):
#        customTexts = CustomizedText.objects.filter(text=text)
#        if customTexts:
#            return customTexts[0].customized_text
#        return text
##    class Meta:
##        verbose_name=_(u'Адаптированный текст')
##        verbose_name_plural=_(u'Адаптированный текст')      
#    
#    class Admin:
#        list_display   = ('text', 'customized_text' )


class Anouncement(BaseContent):
    linked_page = models.ForeignKey(BaseContent, related_name="anouncement_block", blank=True, null=True )
    
    def form(self, **kwargs):
        """Returns the add/edit form of the Anouncement
        """
        return AnouncementForm(**kwargs)

    class Meta:
        verbose_name=_(u'Anouncement')
        verbose_name_plural=_(u'Anouncements')

def append_children_pages(pages, prefix, ordered_pages):
        for page in pages:
            ordered_pages.append([page.id, prefix + " " + page.title])
            children_pages = BaseContent.objects.filter(parent=page).order_by("title")
            if children_pages.count() > 0:
                append_children_pages(children_pages, prefix + "--", ordered_pages)
        return ordered_pages
    
class AnouncementForm(forms.ModelForm):
    """The add/edit form of the Anouncement content object
    """
    class Meta:
        model = Anouncement
        fields = ("title", "description", "tags", "linked_page")
    
    
    def __init__(self, *args, **kwargs):
        super(AnouncementForm, self).__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        if instance:
            pages = BaseContent.objects.filter(parent__isnull=True).order_by("title")
            self.fields["linked_page"].choices = append_children_pages(pages, "", [])
    


class TrackingEvent(BaseContent):
    category = models.CharField(blank=True, max_length=1024)
    analitic_action = models.CharField(blank=True, max_length=1024)
    
    def form(self, **kwargs):
        """Returns the add/edit form of the TrackingEvent
        """
        return TrackingEventForm(**kwargs)

class TrackingEventForm(forms.ModelForm):
    """The add/edit form of the Anouncement content object
    """
    class Meta:
        model = TrackingEvent
        fields = ("title", "category", "analitic_action")
    

    