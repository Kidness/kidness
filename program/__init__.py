# coding: utf-8
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
from django.utils.translation import ugettext_lazy as _
from program.models import *

name = "Program"

def install():
    """Installs the program application.
    """
    # Register Portlets

    # Register Templates
    
    # Register objects
    register_content_type(Trainer, name = "Trainer", global_addable=False)
    register_content_type(Video, name = "Video", global_addable=False)
    register_content_type(Program, name = "Program", templates=["Program_1_2_3", 
                                                                "Program_4_5_6", 
                                                                "Program_7_8_9", 
                                                                "Program_10_11_12",
                                                                "PregnantProgram_1",
                                                                "PregnantProgram_2",
                                                                "PregnantProgram_3"], 
                          default_template="Program_1_2_3", global_addable=False)
    register_content_type(ProgramCatalog, name = "ProgramCatalog", templates=["ChildrenPrograms_1_2_3", 
                                                                              "ChildrenPrograms_4_5_6", 
                                                                              "ChildrenPrograms_7_8_9", 
                                                                              "ChildrenPrograms_10_11_12",
                                                                              "PregnantPrograms_1",
                                                                              "PregnantPrograms_2",
                                                                              "PregnantPrograms_3"], 
                          default_template="ChildrenPrograms_1_2_3", global_addable=True)
    register_content_type(Article, name = "Article", templates=["Articles",], default_template="Articles", global_addable=False)

#    
    register_sub_type(Trainer, "Page")
    register_sub_type(Video, "Page")
    register_sub_type(ProgramCatalog, "Page")
    register_sub_type(Program, "ProgramCatalog")
    register_sub_type(Article, "Page")

def uninstall():
    """Uninstalls the program application.
    """
    # Unregister content type
    unregister_content_type("ProgramCatalog")
    unregister_content_type("Program")
    unregister_content_type("Trainer")
    unregister_content_type("Video")
    unregister_content_type("Article")


