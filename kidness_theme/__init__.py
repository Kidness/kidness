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


name = "Kidness Theme"

def install():
    """Installs the kidness_theme application.
    """
    register_template(name = "TwoColumnsPage", path="kidness_theme/two_column.html")
    # Register Templates
    register_template(name = "ChildrenPrograms_1_2_3", path="kidness_theme/children_programs_1_2_3.html")
    register_template(name = "ChildrenPrograms_4_5_6", path="kidness_theme/children_programs_4_5_6.html")
    register_template(name = "ChildrenPrograms_7_8_9", path="kidness_theme/children_programs_7_8_9.html")
    register_template(name = "ChildrenPrograms_10_11_12", path="kidness_theme/children_programs_10_11_12.html")
     
    register_template(name = "Program_1_2_3", path="kidness_theme/program_1_2_3.html")
    register_template(name = "Program_4_5_6", path="kidness_theme/program_4_5_6.html")
    register_template(name = "Program_7_8_9", path="kidness_theme/program_7_8_9.html")
    register_template(name = "Program_10_11_12", path="kidness_theme/program_10_11_12.html")
     
    register_template(name = "PregnantPrograms_1", path="kidness_theme/pregnant_programs_1.html")
    register_template(name = "PregnantPrograms_2", path="kidness_theme/pregnant_programs_2.html")
    register_template(name = "PregnantPrograms_3", path="kidness_theme/pregnant_programs_3.html")
     
    register_template(name = "PregnantProgram_1", path="kidness_theme/program_pregnant_1.html")
    register_template(name = "PregnantProgram_2", path="kidness_theme/program_pregnant_2.html")
    register_template(name = "PregnantProgram_3", path="kidness_theme/program_pregnant_3.html")
     
    register_template(name = "SelectProgram", path="kidness_theme/select_age.html")
    register_template(name = "SelectTerm", path="kidness_theme/select_term.html")
    register_template(name = "Catalog", path="kidness_theme/catalog.html")
     
    register_template(name = "Index", path="kidness_theme/index.html")
    register_template(name = "About", path="kidness_theme/about.html")
    register_template(name = "Contacts", path="kidness_theme/contacts.html")
     
    register_template(name = "Partners", path="kidness_theme/partners.html")
    register_template(name = "Articles", path="kidness_theme/articles.html")
    register_template(name = "NewsTemp", path="kidness_theme/news.html")


def uninstall():
    """Uninstalls the kidness_theme application.
    """
    # Unregister templates
#    unregister_template("ChildrenPrograms_1_2_3")
#    unregister_template("ChildrenPrograms_4_5_6")
#    unregister_template("ChildrenPrograms_7_8_9")
#    unregister_template("ChildrenPrograms_10_11_12")
#    
#    unregister_template("Program_1_2_3")
#    unregister_template("Program_4_5_6")
#    unregister_template("Program_7_8_9")
#    unregister_template("Program_10_11_12")
#    
#    unregister_template("PregnantPrograms_1")
#    unregister_template("PregnantPrograms_2")
#    unregister_template("PregnantPrograms_3")
#    
#    unregister_template("PregnantProgram_1")
#    unregister_template("PregnantProgram_2")
#    unregister_template("PregnantProgram_3")
#    
#    unregister_template("SelectProgram")
#    unregister_template("SelectTerm")
#    unregister_template("Catalog")
##    unregister_template("Index")
##    unregister_template("About")
#    unregister_template("Contacts")
#    unregister_template("Partners")
#    unregister_template("TwoColumnsPage")
#    unregister_template("Articles")
##    unregister_template("NewsTemp")
    
    
    
    
    