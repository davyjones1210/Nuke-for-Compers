
nuke.message('Hello world!')

 help(nuke.menu)


#for menu in the_menu.items():
#    print(menu.name())
#the_menu.items()[4].items()
#the_menu.items()[4].name()
the_menu = nuke.menu("Nodes")
the_item = the_menu.addCommand("HI", "nuke.message('Hello world!')")

the_menu = nuke.menu("Nodes")
the_shortcut_menu = the_menu.findItem("Image/Constant")

# the_real_menu = the_menu.findItem("Color/Math")
the_item = the_real_menu.addCommand("HI", "nuke.message('Bonjour-hi')")

the_item.script()
the_item.setScript("nuke.message('Hello world!')")
the_item.setScript("nuke.message('Bonjour-hi')")

the_real_menu = the_menu.findItem("Color/Math")
the_real_menu.removeItem("HI2")

the_shortcut_menu.setShortcut('')




#for item in the_menu:
#    if item.name() == "Color":
#        break
