# Remaking topnode and recursion

nuke.tcl("value [topnode Merge2].name")



#manual process
# the_node.input(0).input(0).input(0).input(0).input(0).input(0).input(0)

def topnode(the_node):
    """eturn the topmost node on the B-stream (input 0)
       go at MOST max_depth nodes (if none, go forever)
       return that node that you found at this depth
       NOTE: first node found is depth 0
    """
    current_node = the_node
    while True:
        if current_node.input(0) is None:
            return current_node
        else:
            current_node = current_node.input(0)


the_node = nuke.selectedNode()
print(topnode(the_node).name())

def topnode_r(the_node):
    """Return the topmost node on the B-stream (input 0)"""

    current_node = the_node
    if current_node.input(0) is None:
        return current_node
    return topnode_r(current_node.input(0))


the_node = nuke.selectedNode()
print(topnode_r(the_node).name())

foo()

def foo():
    return foo()