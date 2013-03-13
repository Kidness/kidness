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

from kidness.models import ClientOpinionCatalog, ClientOpinion, News, ShowCase, MainPageBlock, Anouncement, TrackingEvent

name = "Kidness"

def install():
    """Installs the kidness application.
    """
    # Register Templates
    
    register_content_type(ClientOpinion, name = "ClientOpinion", global_addable=False)
    register_content_type(ClientOpinionCatalog, name = "ClientOpinionCatalog", global_addable=True)
    register_sub_type(ClientOpinion, "ClientOpinionCatalog")
    
    register_content_type(News, name="News", global_addable=False, templates=["NewsTemp",])
    register_sub_type(News, "Page")
    
    register_content_type(ShowCase, name="ShowCase", global_addable=False)
    register_sub_type(ShowCase, "Page")
    
    register_content_type(MainPageBlock, name="MainPageBlock", global_addable=False)
    register_sub_type(MainPageBlock, "Page")
    
    register_content_type(Anouncement, name="Anouncement", global_addable=False)
    register_sub_type(Anouncement, "Page")
    
    register_content_type(TrackingEvent, name="TrackingEvent", global_addable=False)
    register_sub_type(TrackingEvent, "Page")


def uninstall():
    """Uninstalls the kidness application.
    """
    # Unregister templates
    unregister_template("ClientOpinion")
    unregister_template("ClientOpinionCatalog")
    unregister_template("News")
    unregister_template("ShowCase")
    unregister_template("MainPageBlock")
    unregister_template("Anouncement")
    unregister_template("TrackingEvent")
    
    
    