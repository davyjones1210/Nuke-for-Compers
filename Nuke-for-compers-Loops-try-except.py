#all_nodes = nuke.allNodes()
#
#for node in all_nodes:
#    if node.knob('which'):
#        node.knob('which').setValue(0)
#
#
#all_nodes[0].knob('label')
#
#def my_function_name(nodes, other_values, delete_everything=False):
#    """ Oneline stuff, doc strings
#    Further description
#    More info
#    """
#    node.knob('label').setValue('Hi')
#    return "Hello"
#
#help(my_function_name)

def set_tile_color(the_node, r=1, g=0, b=1):
    """Set the tile color of the_node with the rgb provided
    r,g,b valuesmust be between 0 and 1. Values outside of this range
    will be clipped to 0 and 1.
    """

    # build the nuke tile colour value from 0-1 RGB values
    # It's 32-bit RGBA number (8 bits per channel, R as MSB)
    r = min(r, 1)
    r = max(r, 0)
    r = int(r*255)
    
    g = 1 if g > 1 else g
    g = 0 if g < 0 else g
    g = int(g*255)
    
    b = max(min(b, 1), 0)   # you'll see this a lot acutally..
    b = int(b*255)
    
    a = 1
    a = int(a*255)
    
    new_colour = (r<<24) + (g<<16) + (b<<8) + (a<<0)  # voodoo magic
    the_node['tile_color'].setValue(new_colour)
 
    # return new_colour

# help(set_tile_color)

blur = nuke.toNode('Blur1')

set_tile_color(blur)