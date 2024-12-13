#help(nuke.nodeCopy)
#
#nuke.nodeCopy("C:/Users/kunal.dekhane/best_blur_rig.nk")
#nuke.nodePaste("C:/Users/kunal.dekhane/best_blur_rig.nk")
#
#nuke.createNode('RotoPaint', inpanel=False)
##help(nuke.toNode('Group1').begin)
#
##This begin-end is really finnicky and messy and there is a better way below in part 2
#
#nuke.toNode('Group1').begin()
#
#nuke.toNode('Transform1')['disable'].setValue(False)
#nuke.toNode('Blur1')['disable'].setValue(False)
##nuke.nodePaste("C:/Users/kunal.dekhane/best_blur_rig.nk")
#nuke.createNode('RotoPaint', inpanel=False)
#nuke.toNode("potato")['disable'].setValue(True)
#
#nuke.toNode('Group1').end()
#
#
#nuke.root().begin()#Use this to start your work back in the root context
#
#nuke.toNode('Grade1')['disable'].setValue(True)
##nuke.nodePaste("C:/Users/kunal.dekhane/best_blur_rig.nk")

#Part 2

#Using context manager (with loop)