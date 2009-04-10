import os
import timeit

from mnemosyne.libmnemosyne import initialise, finalise, config
from mnemosyne.libmnemosyne.component_manager import component_manager
from mnemosyne.libmnemosyne.component_manager import database
from mnemosyne.libmnemosyne.component_manager import card_type_by_id
from mnemosyne.libmnemosyne.component_manager import ui_controller_main

number_of_facts = 6000
create_from_scratch = False  

def initialise_program():
    # 0.085 from scratch
    initialise(os.path.abspath("dot_benchmark"))

def create_database():
    # 106 sec for 6000
    config()["upload_logs"] = False

    for i in range(number_of_facts):
        fact_data = {"q": "question" + str(i),
                     "a": "answer" + str(1)}
        if i % 2:
            card_type = card_type_by_id("1")
        else:
            card_type = card_type_by_id("2")            
        ui_controller_main().create_new_cards(fact_data, card_type,
                               grade=0, cat_names=["default" + str(i)])
    database().save(config()["path"])

def load_database():
    # 0.054 sec for 6000
    database().load(config()["path"])

def activate():
    # 0.128 sec for 6000
    database().set_cards_active([(card_type_by_id("1"),
                                 card_type_by_id("1").fact_views[0])],
        [database().get_or_create_category_with_name("default1")])
    
def finalise_program():
    # 0.005 sec
    config()["upload_logs"] = False
    finalise()
    
# Run these functions and time them.

t = timeit.Timer("initialise_program()",
                 "from __main__ import initialise_program")
t2 = t.timeit(1)
print "init time:", t2


if create_from_scratch:
    t = timeit.Timer("create_database()",
                     "from __main__ import create_database")
    t2 = t.timeit(1)
    print "creation time:", t2


t = timeit.Timer("load_database()",
                 "from __main__ import load_database")
t2 = t.timeit(1)
print "loading time:", t2


t = timeit.Timer("activate()",
                 "from __main__ import activate")
t2 = t.timeit(1)
print "activation time:", t2

t = timeit.Timer("finalise_program()",
                 "from __main__ import finalise_program")
t2 = t.timeit(1)
print "finalise time:", t2