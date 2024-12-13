# the_grade = nuke.selectedNode()

my_code = """
do_some_warnings()
#import datetime
#print("Hello {}".format(datetime.datetime.now()))

"""



nuke.toNode('Grade3').knob('knobChanged').setValue(my_code)

def do_some_warnings(the_node=None, the_knob=None):
    this_node = the_node or nuke.thisNode()
    
    this_knob = the_knob or nuke.thisKnob()
    
    if this_knob.name() == "multiply":
        
        if this_node.knob('multiply').value() > 1.2:
            this_node.knob('label').setValue("TOOO HOT")
        else:
            this_node.knob('label').setValue("")

do_some_warnings(nuke.toNode('Grade4'), nuke.toNode('Grade4').knob('multiply'))

#def do_some_warnings():
#    this_node = nuke.thisNode()
#    
#    this_knob = nuke.thisKnob()
#    
#    if this_knob.name() == "multiply":
#        
#        if this_node.knob('multiply').value() > 1.2:
#            this_node.knob('label').setValue("TOOO HOT")
#        else:
#            this_node.knob('label').setValue("")





