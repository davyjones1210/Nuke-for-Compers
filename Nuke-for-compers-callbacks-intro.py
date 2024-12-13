help(nuke.callbacks)


def annoying_callback():
    nuke.message("I have loaded the script")


nuke.callbacks.addOnScriptLoad(annoying_callback)

def on_create():
    print("On create fired: {}".format(nuke.thisNode().fullName()))

def on_user_create():
    print("On user create fired: {}".format(nuke.thisNode().fullName()))

nuke.callbacks.addOnCreate(on_create)

nuke.callbacks.addOnUserCreate(on_user_create)

# nuke.callbacks.removeOnCreate(annoying_callback)

#nuke.callbacks.removeOnUserCreate(on_user_create)

nuke.callbacks.removeOnScriptLoad(annoying_callback)

