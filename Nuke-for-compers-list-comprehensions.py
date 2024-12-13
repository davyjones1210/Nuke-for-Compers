# list comprehension

new_list = [ <expression> for <item> in <old_list> if <condition_is_true>]

# filter
numbers = [10, 14, 10, 91, 50, 15, 33]
big_num = [            91, 50,    33]
double = [20, 28, 20, 182, 100, 30, 66]
double_big = [        182, 100,     66]

big_num = [x for x in numbers if x > 30]
double = [x*2 for x in numbers]
double_big = [x*2 for x in numbers if x > 30]

nodes 	= nuke.selectedNodes()

transforms = [x for x in nodes if x.Class() == "Transform"]
odd_shutter = [x for x in transforms if x['shutter'].value() != 0.5]

odd_shutter_values = [x['shutter'].value() for x in odd_shutter]

odd_shutter_full_name = [x.fullName() for x in odd_shutter]

# if x['shutter'].value() != 0.5]

rotopaints = [ ]

for node in nodes:
    if node.Class() == "RotoPaint":
        rotopaints.append(node)

rotopaints = [node for node in nodes if node.Class() == "RotoPaint"]
