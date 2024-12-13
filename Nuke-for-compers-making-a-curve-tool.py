# help(nuke.sample)

the_node = nuke.toNode('SAMPLE_ME')

# help(the_node.sample)

w = the_node.width()
h = the_node.height()

x = 0
y = 0
max_lum = 0
where = (0,0)

start = 1001
end = 1010

for frame in range(start, end):
    max_lum = 0
    where = (0,0)
    
    for y in range(0, h):
        for x in range (0, w):
            
            red = the_node.sample("rgba.red", x+0.5, y+0.5, frame=frame)
            green = the_node.sample("rgba.green", x+0.5, y+0.5, frame=frame)
            blue = the_node.sample("rgba.blue", x+0.5, y+0.5, frame=frame)
            
            luminance = 0.2126*red + 0.7152*green + 0.0722*blue
            if luminance > max_lum:
                max_lum = luminance
                where = (x,y)
    
    print(where)
    
nuke.tprint("Hello world!")
sys.stderr.write("\nHellooo")
sys.stdout.write("123123")
    
    
    
