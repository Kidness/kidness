# django imports
from django.utils.translation import ugettext_lazy as _

# lfc imports
from lfc.utils.registration import register_content_type
from lfc.utils.registration import unregister_content_type
from lfc.utils.registration import register_sub_type
from lfc.utils.registration import register_template
from lfc.utils.registration import unregister_template

# portlets imports
from portlets.utils import register_portlet
from portlets.utils import unregister_portlet

from kidness_portlets.models import NewsPortlet, ArticlePortlet, AnouncementPortlet, SignupButtonPortlet, TagsBlockPortlet, AddThisBlockPortlet

name = "Kidness Portlets"

def install():
    """Installs the Kidness Portlets parts application.
    """
    # Register Portlets
    #register_portlet(NewsPortlet, "NewsPortlet")
    #register_portlet(ArticlePortlet, "ArticlePortlet")
    #register_portlet(AnouncementPortlet, "AnouncementPortlet")
    register_portlet(SignupButtonPortlet, "SignupButtonPortlet")
    register_portlet(TagsBlockPortlet, "TagsBlockPortlet")
    register_portlet(AddThisBlockPortlet, "AddThisBlockPortlet")

def uninstall():
    pass
    #unregister_portlet(NewsPortlet)
    #unregister_portlet(ArticlePortlet)
    #unregister_portlet(AnouncementPortlet)
    #unregister_portlet(SignupButtonPortlet)
    #unregister_portlet(TagsBlockPortlet)
    #unregister_portlet(AddThisBlockPortlet)
    
    
    
    
    