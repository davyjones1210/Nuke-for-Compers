the_node = nuke.selectedNode()

cheese = ["Comte", "Cheddar", "Protoss cannon rush", "Stilton", "Brunost"]

cheese_knob = nuke.Enumeration_Knob("Cheese", "Cheese I like", cheese)

the_node.addKnob(cheese_knob)

cheese_knob.value()

cheese_knob.values()

cheese_knob.getValue()


