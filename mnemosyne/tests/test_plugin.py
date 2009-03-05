#
# test_html_css.py <Peter.Bienstman@UGent.be>
#

from nose.tools import raises

import os

from mnemosyne.libmnemosyne.plugin import Plugin
from mnemosyne.libmnemosyne import initialise, finalise
from mnemosyne.libmnemosyne.component_manager import card_types

class TestPlugin:

    def setup(self):
        os.system("rm -fr dot_test")
        initialise(os.path.abspath("dot_test"))
        
    @raises(AssertionError)
    def test_1(self):
        p = Plugin()

    def test_2(self):

        class MyPlugin(Plugin):
            name = "myplugin"
            description = "MyPlugn"
            provides = "card_type"
            id = "666"
        p = MyPlugin()

        p.activate()

        #print card_types()

        p.deactivate()              
        
    def teardown(self):
         finalise()