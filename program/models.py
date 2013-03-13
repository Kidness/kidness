# coding: utf-8
from lfc.models import BaseContent
from django.db import models
from django import forms
from django.conf import settings
from portlets.models import Portlet
from django.core.cache import cache
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

# tagging imports
import tagging.models
from tagging.forms import TagField
from lfc.fields.autocomplete import AutoCompleteTagInput

class Trainer(BaseContent):
    preview = models.TextField(u"Короткое описание", blank=True)
    photo = models.ImageField(u"Фото", upload_to="/", blank=True, null=True)
    
    class Meta:
        verbose_name=_(u'Trainer')
        verbose_name_plural=_(u'Trainers')
    
    def form(self, **kwargs):
        """Returns the add/edit form of the Trainer
        """
        return TrainerForm(**kwargs)

class TrainerForm(forms.ModelForm):
    """The add/edit form of the Program content object
    """
    
    class Meta:
        model = Trainer
        fields = ("title", "display_title", "slug", "preview", "description")
    
    def __init__(self, *args, **kwargs):
        super(TrainerForm, self).__init__(*args, **kwargs)
        self.fields['preview'].widget.attrs['class'] = 'rich_text_format'
        self.fields['description'].widget.attrs['class'] = 'rich_text_format'


#class Video(models.Model):
#    name = models.CharField(max_length=1024, blank=True)
#    description = models.TextField(blank=True)
#    location = models.CharField(max_length=1024, blank=True)
#    video = models.FileField(upload_to="/", blank=True, null=True)

class Video(BaseContent):
    location = models.TextField(blank=True)
    video = models.FileField(upload_to="/", blank=True, null=True)
    #preview = models.ImageField(u"Превьюшечка", upload_to="/", blank=True, null=True)
    
    class Meta:
        verbose_name=_(u'Video')
        verbose_name_plural=_(u'Videos')
    
    def form(self, **kwargs):
        """Returns the add/edit form of the Trainer
        """
        return VideoForm(**kwargs)

class VideoForm(forms.ModelForm):
    """The add/edit form of the Video content object
    """
    
    class Meta:
        model = Video
        fields = ("title", "slug", "description", "location", "video")
    
def append_children_pages(pages, prefix, ordered_pages):
    for page in pages:
        ordered_pages.append([page.id, prefix + " " + page.title])
        children_pages = BaseContent.objects.filter(parent=page).order_by("title")
        if children_pages.count() > 0:
            append_children_pages(children_pages, prefix + "--", ordered_pages)
    return ordered_pages
    
class Program(BaseContent):
    preview = models.TextField(u"Короткое описание", blank=True)
    trainers = models.ManyToManyField(Trainer, blank=True, null=True)
    sibling_left = models.ForeignKey("Program", null=True, blank=True, related_name="sibling_left_to")
    sibling_right = models.ForeignKey("Program", null=True, blank=True, related_name="sibling_right_to")
    videos = models.ManyToManyField(Video, blank=True, null=True)
    can_be_signup = models.BooleanField(u"Можно записаться", default=True)
    
    class Meta:
        verbose_name=_(u'Program')
        verbose_name_plural=_(u'Programs')
        
    def form(self, **kwargs):
        """Returns the add/edit form of the Program
        """
        return ProgramForm(**kwargs)
    

class ProgramForm(forms.ModelForm):
    """The add/edit form of the Program content object
    """
    tags = TagField(widget=AutoCompleteTagInput(), required=False)
    
    class Meta:
        model = Program
        fields = ("title", "display_title", "slug", "preview", "description", "can_be_signup", "trainers", "videos", "sibling_left", "sibling_right", "tags")
        
    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
#        self.fields['preview'].widget.attrs['class'] = 'rich_text_format'
        self.fields['description'].widget.attrs['class'] = 'rich_text_format'
        
        programs = BaseContent.objects.filter(content_type="program").order_by("parent__title")
        ordered_programs = [["", "-"]]
        for program in programs:
            ordered_programs.append([program.id, program.parent.title + "->" + program.title])
        self.fields["sibling_left"].choices = ordered_programs
        self.fields["sibling_right"].choices = ordered_programs
        
class ProgramCatalog(BaseContent):
    
    class Meta:
        verbose_name=_(u'ProgramCatalog')
        verbose_name_plural=_(u'ProgramCatalogs')
        
    def form(self, **kwargs):
        """Returns the add/edit form of the ProgramCatalog
        """
        return ProgramCatalogForm(**kwargs)


class ProgramCatalogForm(forms.ModelForm):
    """The add/edit form of the ProgramCatalog content object
    """
    class Meta:
        model = ProgramCatalog
        fields = ("title", "display_title", "slug", "description")


class Article(BaseContent):
    trainers = models.ManyToManyField(Trainer, blank=True)
    text = models.TextField(u'Текст')
    
    class Meta:
        verbose_name=_(u'Article')
        verbose_name_plural=_(u'Articles')
        
    def form(self, **kwargs):
        """Returns the add/edit form of the Article
        """
        return ArticleForm(**kwargs)
    

class ArticleForm(forms.ModelForm):
    """The add/edit form of the Article content object
    """
    tags = TagField(widget=AutoCompleteTagInput(), required=False)
    
    class Meta:
        model = Article
        fields = ("title", "display_title", "slug", "description", "text", "trainers", "tags")

